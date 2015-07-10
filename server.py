#!/usr/bin/env python

#!/usr/bin/env python
import socket, sys, time, json, threading
import logging, time, os, sys
from pid import Pid
from openbccfg import OpenBCcfg
from jsonrpclib import Server
from abio import TempSensor, AnalogOut, AnalogLambda, FireSensor, Screw, Hmi, GuiData
from innovate_lambda import SerialLambda
from datetime import datetime


q = GuiData()

HOST = '127.0.0.1'   # Symbolic name, meaning all available interfaces
PORT = 8820 # Arbitrary non-privileged port

CFG_PATH = "/cfg/"
CFG_FILE = "openBC.cfg"



CFG = os.path.dirname(os.path.abspath(__file__)) + CFG_PATH + CFG_FILE
OB = OpenBCcfg(CFG) # Read config file.
time.sleep(2)
S = Server(OB.EVOK_URL) # Connection to evok api

TEMP_SCREW_BLOCK_TIMER = time.time() # Read current time, need this for screw controll
TEMP_LOG_BLOCK_TIMER = time.time()

# Make sure all relay is deactivated
for x in xrange(1,9):
	S.relay_set(x, 0)

# Init Log (/tmp/openBC.log)
logging.basicConfig(filename=OB.LOG_BASE_DIR + OB.LOG_FILE_NAME, format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
logging.info('%s', 'Start!')

# Create instances.
TANK = TempSensor(S, OB.TANK_TEMP_SENSOR_ID)
BOILER = TempSensor(S, OB.BOILER_TEMP_SENSOR_ID)
# FALLBACK_TEMP = TempSensor(S, "286B075005000099")
FIRE = FireSensor(S, OB.FIRE_TEMP_SENSOR_ANALOG_PIN)
FAN = AnalogOut(S, OB.FAN_CONTACTOR_PIN, OB.FAN_ANALOG_PIN)
SOND = SerialLambda(S, OB.LAMBDA_SENSOR_CONTACTOR_PIN, OB.LAMBDA_SENSOR_TYPE, OB.LAMBDA_SENSOR_PORT, OB.LAMBDA_SENSOR_BAUD, int(OB.LAMBDA_SENSOR_SYNC_HEADER_ATTEMPT))
SCREW = Screw(S, OB.SCREW_CONTACTOR_PIN)
HMI = Hmi(S, OB.BUTTON_CONTACTOR_PIN)


# PID
p=Pid(10.0,0.0,0)
p.setPoint(30)

HMI.activate_contactor() # Activate HMI buttons


def GuiServer(q):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(10)
	while 1:
		conn, addr = s.accept()
		conn.send(q.get())
	conn.close()

t1 = threading.Thread(target=GuiServer, args=(q,))
t1.start()

logging.info('%s', "Enter main loop")
while True:
	q.put(TANK.get_temp(), BOILER.get_temp(), FIRE.get_temp(), int(FAN.get_rpm()))								# UPPDATE VALUE FOR GUI
	if not S.input_get_value(OB.BUTTON_EMERGENCY_STOP):															# EMRGENCY STOP PRESSED (NC BLOCK)
		logging.info('%s', "Emergency stop pressed")
		FAN.deactivate_contactor()
		SOND.deactivate_contactor()
		SCREW.deactivate_contactor()
		while not S.input_get_value(OB.BUTTON_EMERGENCY_STOP):
			pass
		logging.info('%s', "Emergency stop released")
	else:
		if S.input_get_value(OB.BUTTON_RESET):																	# RESET PRESSED
				logging.info('%s', "Reset pressed")
				for x in xrange(1,9):
					time.sleep(0.1)
					S.relay_set(x, 0)
				os.system("sudo service openbc restart")
		if S.input_get_value(OB.BUTTON_AUTO_MAN): 																# AUTO MODE
			if int(OB.LAMBDA_SENSOR_ENABLED):
				SOND.activate_contactor() 																		# ACTIVATE LAMBDASOND
			if int(OB.FAN_ENABLED):									
				if not FAN.contactor:																			# ACTIVATE FAN
					logging.info('%s', "FAN Activate contactor")
					FAN.activate_contactor()
			if time.time() > (int(TEMP_SCREW_BLOCK_TIMER) + int(OB.BLOCK_TIME)): 								# TIMER BELOW BLOCKTIMER?
				if FIRE.get_temp() <= float(OB.FIRE_SET_TEMP):													# FIRE BELOW SET TEMP?
					if TANK.get_temp() <= float(OB.TANK_SET_TEMP):												# TANK BELOW SET TEMP?
						if BOILER.get_temp() <= float(OB.BOILER_SET_TEMP):										# BOILER BELOW SET TEMP?
							TEMP_SCREW_BLOCK_TIMER = time.time()
							SCREW.activate_for_time(int(OB.RUN_TIME_SCREW))
							logging.info('%s%s%s', "Run screw for ", OB.RUN_TIME_SCREW, "sec")
			if FAN.contactor and SOND.contactor:
				pid = p.update(TANK.get_temp())
				FAN.set_voltage(pid*(-0.1)+2)
			else:
				FAN.set_voltage(int(OB.FAN_SAFE_MODE_SPEED))
			if time.time() > (int(TEMP_LOG_BLOCK_TIMER) + int(OB.LOG_BLOCK_TIME)): 								# LOG DEBUG DATA
				TEMP_LOG_BLOCK_TIMER = time.time()
				logging.debug('Temp: %s PID: %s FAN: %s RPM', TANK.get_temp(), str(pid*(-0.1)+2), int(FAN.get_rpm()))
		else:																									# MAN MODE
			if FAN.contactor:
				logging.info('%s', "FAN Deactivate contactor")
				FAN.deactivate_contactor()
			if S.input_get_value(OB.BUTTON_MAN_SCREW_FORWARD):													# MAN SCREW
				SCREW.activate_contactor()
				logging.info('%s', "MAN Screw pressed")
				while S.input_get_value(OB.BUTTON_MAN_SCREW_FORWARD):
					pass
				logging.info('%s', "MAN Screw released")
				SCREW.deactivate_contactor()
			if S.input_get_value(OB.BUTTON_MAN_FAN_FORWARD):													# MAN FAN
				FAN.activate_contactor()
				FAN.set_voltage(int(OB.FAN_SAFE_MODE_SPEED))
				logging.info('%s', "MAN Fan pressed")
				while S.input_get_value(OB.BUTTON_MAN_FAN_FORWARD):												
					q.put(TANK.get_temp(), BOILER.get_temp(), FIRE.get_temp(), int(FAN.get_rpm()))				# UPPDATE VALUE FOR GUI
					if S.input_get_value(OB.BUTTON_RESET): 														# REBOOT (MAN FAN + RESET)
						os.system("sudo reboot")
				logging.info('%s', "MAN Fan released")
				FAN.set_voltage(0)
				FAN.deactivate_contactor()
		# RESET/AUTO/MAN MODE
	# EMERGENCY STOP
# INFINITI LOOP
