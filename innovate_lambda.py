#!/usr/bin/env python
from jsonrpclib import Server
import serial
import time

# Uncomment.
#s = Server("http://127.0.0.1/rpc") # Connection to evok api
#DEVICE_NAME = "LC-2"
#DEVICE_PORT = "/dev/ttyAMA0"
#DEVICE_PORT = "/dev/ttyUSB0"
#BAUD = 19200
#SYNC_HEADER_ATTEMPT = 10

class SerialLambda(object):
	def __init__(self, s, relay_pin, device_name, device_port, baud, sync_header_attempt):
		self.s = s
		self.relay_pin = relay_pin
		self.device_name  = device_name
		self.device_port = device_port
		self.baud = baud
		self.sync_header_attempt = sync_header_attempt
		self.contactor = False

		self.status_code = {
							"000": "Lambda valid",
							"001": "To lean, lambda value contains O2 level in 1/10%",
							"010": "Free air calibration in progress, Lambda data not valid",
							"011": "Need Free air Calibration Request, Lambda data not valid",
							"100": "Warming up, Lambda value is temp in 1/10 of operating temp.",
							"101": "Heater Calibration, Lambda value contains calibration countdown.",
							"110": "Error code in Lambda value",
							"111": "reserved"
							}
	def activate_contactor(self):
		self.s.relay_set(self.relay_pin, 1)
		self.contactor = True
	def deactivate_contactor(self):
		self.s.relay_set(self.relay_pin, 0)
		self.contactor = False
	def GetSerialOrFalse(self):
		try:
			return serial.Serial(self.device_port, self.baud)
		except:
			return False

	def ReadDataFromSond(self, ser, sync_header_attempt):
		for x in xrange(0, sync_header_attempt):
			temp_data1 = ser.read().encode('hex')
			if hex(int(temp_data1, 16) & 0xa2) == "0xa2":
				temp_data2 = ser.read().encode('hex')
				if hex(int(temp_data2, 16) & 0x80) == "0x80": #Header found						
					#Read upcoming byte
					temp_data3 = ser.read().encode('hex')
					temp_data4 = ser.read().encode('hex')
					temp_data5 = ser.read().encode('hex')
					temp_data6 = ser.read().encode('hex')
					#print temp_data1, temp_data2, temp_data3, temp_data4, temp_data5, temp_data6
					return (temp_data1, temp_data2, temp_data3, temp_data4, temp_data5, temp_data6)
		return False

	def HexToBin(self, raw_data):
		temp_list = []
		for item in raw_data:
			temp_list.append('{:08b}'.format(int(item, 16)))
		return temp_list

	def ParseBinData(self, bin_data_list):
		header = bin_data_list[0] + bin_data_list[1]
		word0 = bin_data_list[2] + bin_data_list[3]
		word1 =  bin_data_list[4] + bin_data_list[5]
		#print header, word0, word1
		status = word0[3] + word0[4] + word0[5]
		af = word0[7] + word0[9] + word0[10] + word0[11] + word0[12] + word0[13] + word0[14] + word0[15]
		if not int(status, 2):
			l = word1[2] + word1[3] + word1[4] + word1[5] + word1[6] + word1[7] + word1[9] + word1[10] + word1[11] + word1[12] + word1[13] + word1[14] + word1[15]
			lambda_value = (int(l, 2) * 0.001) + 0.500
			afr_value = lambda_value * (int(af, 2) / float(100)) / 10
		else:
			afr_value = False
			lambda_value = False
		return {"Status code": status, "Status message": self.status_code[status], "Air/Fuel Multiplier": int(af, 2) / float(100), "Lambda value": lambda_value, "AFR value": afr_value}

	def GetData(self):
		ser = self.GetSerialOrFalse()
		if ser:
			data_raw = self.ReadDataFromSond(ser, self.sync_header_attempt)
			ser.close()
			if data_raw:
				bin_data = self.HexToBin(data_raw)
				data = self.ParseBinData(bin_data)
				return data
		return False

	def GetAllValue(self):
		return self.GetData()

	def GetValueLambda(self):
		temp = self.GetData()
		if temp['Lambda value']:
			return temp['Lambda value']
		else:
			return False

	def GetValueAfr(self):
		temp = self.GetData()
		if temp['AFR value']:
			return temp['AFR value']
		else:
			return False

	def GetStatusCode(self):
		temp = self.GetData()
		return temp['Status code']

	def GetStatusMessage(self):
		temp = self.GetData()
		return temp['Status message']

if __name__ == "__main__":
	
	while True:
		time.sleep(2)
		sond = SerialLambda(s, 1, DEVICE_NAME, DEVICE_PORT, BAUD, SYNC_HEADER_ATTEMPT)
		print sond.GetAllValue()