import json

class TempSensor(object):
	def __init__(self,s, adress):
		self.s = s
		self.adress = adress
	def get_temp(self):
		return self.s.sensor_get_value(self.adress)


class AnalogOut(object):
	def __init__(self,s, relay_pin, analog_pin, voltage=0):
		self.s = s
		self.relay_pin = relay_pin
		self.analog_pin = analog_pin
		self.voltage = voltage
		self.contactor = False

	def activate_contactor(self):
		self.contactor = True
		self.s.relay_set(self.relay_pin, 1)
	def deactivate_contactor(self):
		self.contactor = False
		self.s.relay_set(self.relay_pin, 0)
	def set_voltage(self, voltage):
		self.voltage = voltage
		self.s.ao_set_value(self.analog_pin, self.voltage)
	def increase_voltage(self, increase_value):
		self.voltage = self.voltage + increase_value
		self.s.ao_set_value(self.analog_pin, self.voltage)
	def decrease_voltage(self, decrease_value):
		self.voltage = self.voltage - decrease_value
		self.s.ao_set_value(self.analog_pin, self.voltage)
	def get_rpm(self):
			temp = self.translate(self.voltage)
			if temp < 1.2 or self.contactor == False:
				return 0
			elif temp > 2200:
				return 2200
			else:
				return temp
	def translate(self, value, leftMin=0, leftMax=9, rightMin=0, rightMax=2200):
		leftSpan = leftMax - leftMin
		rightSpan = rightMax - rightMin
		valueScaled = float(value - leftMin) / float(leftSpan)
		return rightMin + (valueScaled * rightSpan)


class AnalogLambda(object):
	def __init__(self,s, relay_pin, analog_pin):
		self.s = s
		self.relay_pin = relay_pin
		self.analog_pin = analog_pin

	def activate_contactor(self):
		self.s.relay_set(self.relay_pin, 1)
	def deactivate_contactor(self):
		self.s.relay_set(self.relay_pin, 0)
	def get_voltage(self):
		l = self.s.ai_get(self.analog_pin)
		return round(l[0], 2)
	def get_lambda():
		pass

class FireSensor(object):
	def __init__(self, s, analog_pin):
		self.s = s
		self.analog_pin = analog_pin
	def get_temp(self):
		t = self.s.ai_get(self.analog_pin)
		return round(t[0]/5*1000, 1)

class Screw(object):
	def __init__(self,s, relay_pin):
		self.s = s
		self.relay_pin = relay_pin
		self.contactor = False

	def activate_contactor(self):
		self.contactor = True
		self.s.relay_set(self.relay_pin, 1)
	def deactivate_contactor(self):
		self.contactor = False
		self.s.relay_set(self.relay_pin, 0)
	def activate_for_time(self, timeout):
		self.s.relay_set_for_time(self.relay_pin, 1, timeout)

class Hmi(object):
	def __init__(self,s, relay_pin):
		self.s = s
		self.relay_pin = relay_pin
		self.contactor = False

	def activate_contactor(self):
		self.contactor = True
		self.s.relay_set(self.relay_pin, 1)
	def deactivate_contactor(self):
		self.contactor = False
		self.s.relay_set(self.relay_pin, 0)

class GuiData():
	def __init__(self):
		self.data = ""
	def get(self):
		return self.data
	def put(self, tank_temp, boiler_temp, fire_temp, fan_rpm):
		self.data = json.dumps({'TANK': tank_temp, 'BOILER': boiler_temp, 'FIRE': fire_temp, 'FAN RPM': fan_rpm, })
