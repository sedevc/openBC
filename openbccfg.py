import ConfigParser

class OpenBCcfg(object):

	def __init__(self, file_name):
		self.config = ConfigParser.RawConfigParser()
		self.file_name = file_name
			
	def readConfigFile(self):
		self.config.read(self.file_name)

		self.HW_NAME = self.config.get("info", "hw_name")
		self.IP = self.config.get("info", "ip")
		self.EVOK_URL = self.config.get("info", "evok_url")

		self.BOILER_TEMP_SENSOR_ENABLED = self.config.get("boiler_temp_sensor", "enabled")
		self.BOILER_TEMP_SENSOR_TYPE = self.config.get("boiler_temp_sensor", "type")
		self.BOILER_TEMP_SENSOR_BASE_DIR = self.config.get("boiler_temp_sensor", "base_dir")
		self.BOILER_TEMP_SENSOR_FILE_NAME = self.config.get("boiler_temp_sensor", "file_name")
		self.BOILER_TEMP_SENSOR_ID = self.config.get("boiler_temp_sensor", "id")

		self.TANK_TEMP_SENSOR_ENABLED = self.config.get("tank_temp_sensor", "enabled")
		self.TANK_TEMP_SENSOR_TYPE = self.config.get("tank_temp_sensor", "type")
		self.TANK_TEMP_SENSOR_BASE_DIR = self.config.get("tank_temp_sensor", "base_dir")
		self.TANK_TEMP_SENSOR_FILE_NAME = self.config.get("tank_temp_sensor", "file_name")
		self.TANK_TEMP_SENSOR_ID = self.config.get("tank_temp_sensor", "id")

		self.FIRE_TEMP_SENSOR_ENABLED = self.config.get("fire_temp_sensor", "enabled")
		self.FIRE_TEMP_SENSOR_TYPE = self.config.get("fire_temp_sensor", "type")
		self.FIRE_TEMP_SENSOR_ANALOG_PIN = self.config.get("fire_temp_sensor", "analog_pin")

		self.LAMBDA_SENSOR_ENABLED = self.config.get("lambda_sensor", "enabled")
		self.LAMBDA_SENSOR_TYPE = self.config.get("lambda_sensor", "type")
		self.LAMBDA_SENSOR_PORT = self.config.get("lambda_sensor", "port")
		self.LAMBDA_SENSOR_BAUD = self.config.get("lambda_sensor", "baud")
		self.LAMBDA_SENSOR_SYNC_HEADER_ATTEMPT = self.config.get("lambda_sensor", "sync_header_attempt")
		self.LAMBDA_SENSOR_ANALOG_PIN = self.config.get("lambda_sensor", "analog_pin")
		self.LAMBDA_SENSOR_CONTACTOR_PIN = self.config.get("lambda_sensor", "contactor_pin")

		self.BUTTON_CONTACTOR_PIN = self.config.get("control_button", "contactor_pin")
		self.BUTTON_EMERGENCY_STOP = self.config.get("control_button", "emergency_stop_gpio")
		self.BUTTON_AUTO_MAN = self.config.get("control_button", "auto_man_gpio")
		self.BUTTON_MAN_SCREW_FORWARD = self.config.get("control_button", "man_screw_forward_gpio")
		self.BUTTON_MAN_SCREW_BACKWARD = self.config.get("control_button", "man_screw_backward_gpio")
		self.BUTTON_MAN_FAN_FORWARD = self.config.get("control_button", "man_fan_forward_gpio")
		self.BUTTON_RESET = self.config.get("control_button", "reset_gpio")
				
		self.BLOCK_TIME = self.config.get("timers", "block_time")
		self.BLOCK_TIME_IDLE = self.config.get("timers", "block_time_idle")
		self.RUN_TIME_FAN_IDLE = self.config.get("timers", "run_time_fan_idle")
		self.RUN_TIME_SCREW = self.config.get("timers", "run_time_screw")
		self.RUN_TIME_SCREW_IDLE = self.config.get("timers", "run_time_screw_idle")
		self.LOG_BLOCK_TIME = self.config.get("timers", "log_block_time")
				
		self.TANK_SET_TEMP = self.config.get("limits", "tank_set_temp")
		self.BOILER_SET_TEMP = self.config.get("limits", "boiler_set_temp")
		self.FIRE_SET_TEMP = self.config.get("limits", "fire_set_temp")
		self.LAMBDA_SET_VALUE = self.config.get("limits", "lambda_set_value")
		self.IDLE_FIRE_SET_TEMP = self.config.get("limits", "idle_fire_set_temp")

		self.FAN_ENABLED = self.config.get("fan", "enabled")
		self.FAN_TYPE = self.config.get("fan", "type")
		self.FAN_ANALOG_PIN = self.config.get("fan", "analog_pin")
		self.FAN_SAFE_MODE_SPEED = self.config.get("fan", "safe_mode_speed")
		self.FAN_CONTACTOR_PIN = self.config.get("fan", "contactor_pin")

		self.SCREW_ENABLED = self.config.get("screw", "enabled")
		self.SCREW_TYPE = self.config.get("screw", "type")
		self.SCREW_CONTACTOR_PIN = self.config.get("screw", "contactor_pin")

		self.DATABASE_ENABLED = self.config.get("database", "enabled")
		self.DATABASE_TYPE = self.config.get("database", "type")
		self.DATABASE_NAME = self.config.get("database", "db_name")

		self.LOG_BASE_DIR = self.config.get("log", "base_dir")
		self.LOG_FILE_NAME = self.config.get("log", "file_name")

	def WriteConfigFile(self):
		self.config.set('info', 'hw_name', self.HW_NAME)
		self.config.set('info', 'ip', self.IP)
		self.config.set('info', 'evok_url', self.EVOK_URL)

		self.config.set('boiler_temp_sensor', 'enabled', self.BOILER_TEMP_SENSOR_ENABLED)
		self.config.set('boiler_temp_sensor', 'type', self.BOILER_TEMP_SENSOR_TYPE)
		self.config.set('boiler_temp_sensor', 'base_dir', self.BOILER_TEMP_SENSOR_BASE_DIR)
		self.config.set('boiler_temp_sensor', 'file_name', self.BOILER_TEMP_SENSOR_FILE_NAME)
		self.config.set('boiler_temp_sensor', 'id', self.BOILER_TEMP_SENSOR_ID)

		self.config.set('tank_temp_sensor', 'enabled', self.TANK_TEMP_SENSOR_ENABLED)
		self.config.set('tank_temp_sensor', 'type', self.TANK_TEMP_SENSOR_TYPE)
		self.config.set('tank_temp_sensor', 'base_dir', self.TANK_TEMP_SENSOR_BASE_DIR)
		self.config.set('tank_temp_sensor', 'file_name', self.TANK_TEMP_SENSOR_FILE_NAME)
		self.config.set('tank_temp_sensor', 'id', self.TANK_TEMP_SENSOR_ID)

		self.config.set('fire_temp_sensor', 'enabled', self.FIRE_TEMP_SENSOR_ENABLED)
		self.config.set('fire_temp_sensor', 'type', self.FIRE_TEMP_SENSOR_TYPE)
		self.config.set('fire_temp_sensor', 'analog_pin', self.FIRE_TEMP_SENSOR_ANALOG_PIN)

		self.config.set('lambda_sensor', 'enabled', self.LAMBDA_SENSOR_ENABLED)
		self.config.set('lambda_sensor', 'type', self.LAMBDA_SENSOR_TYPE)
		self.config.set('lambda_sensor', 'port', self.LAMBDA_SENSOR_PORT)
		self.config.set('lambda_sensor', 'baud', self.LAMBDA_SENSOR_BAUD)
		self.config.set('lambda_sensor', 'sync_header_attempt', self.LAMBDA_SENSOR_SYNC_HEADER_ATTEMPT)
		self.config.set('lambda_sensor', 'analog_pin', self.LAMBDA_SENSOR_ANALOG_PIN)
		self.config.set('lambda_sensor', 'contactor_pin', self.LAMBDA_SENSOR_CONTACTOR_PIN)

		self.config.set('control_button', 'contactor_pin', self.BUTTON_CONTACTOR_PIN)
		self.config.set('control_button', 'emergency_stop_gpio', self.BUTTON_EMERGENCY_STOP)
		self.config.set('control_button', 'auto_man_gpio', self.BUTTON_AUTO_MAN)
		self.config.set('control_button', 'man_screw_forward_gpio', self.BUTTON_MAN_SCREW_FORWARD)
		self.config.set('control_button', 'man_screw_backward_gpio', self.BUTTON_MAN_SCREW_BACKWARD)
		self.config.set('control_button', 'man_fan_forward_gpio', self.BUTTON_MAN_FAN_FORWARD)
		self.config.set('control_button', 'reset_gpio', self.BUTTON_RESET)

		self.config.set('timers', 'block_time', self.BLOCK_TIME)
		self.config.set('timers', 'block_time_idle', self.BLOCK_TIME_IDLE)
		self.config.set('timers', 'run_time_fan_idle', self.RUN_TIME_FAN_IDLE)
		self.config.set('timers', 'run_time_screw', self.RUN_TIME_SCREW)
		self.config.set('timers', 'run_time_screw_idle', self.RUN_TIME_SCREW_IDLE)
		self.config.set('timers', 'log_block_time', self.LOG_BLOCK_TIME)

		self.config.set('limits', 'tank_set_temp', self.TANK_SET_TEMP)
		self.config.set('limits', 'boiler_set_temp', self.BOILER_SET_TEMP)
		self.config.set('limits', 'fire_set_temp', self.FIRE_SET_TEMP)
		self.config.set('limits', 'lambda_set_value', self.LAMBDA_SET_VALUE)
		self.config.set('limits', 'idle_fire_set_temp', self.IDLE_FIRE_SET_TEMP)

		self.config.set('fan', 'enabled', self.FAN_ENABLED)
		self.config.set('fan', 'type', self.FAN_TYPE)
		self.config.set('fan', 'analog_pin', self.FAN_ANALOG_PIN)
		self.config.set('fan', 'safe_mode_speed', self.FAN_SAFE_MODE_SPEED)
		self.config.set('fan', 'contactor_pin', self.FAN_CONTACTOR_PIN)

		self.config.set('screw', 'enabled', self.SCREW_ENABLED)
		self.config.set('screw', 'type', self.SCREW_TYPE)
		self.config.set('screw', 'contactor_pin', self.SCREW_CONTACTOR_PIN)

		self.config.set('database', 'enabled', self.DATABASE_ENABLED)
		self.config.set('database', 'type', self.DATABASE_TYPE)
		self.config.set('database', 'db_name', self.DATABASE_NAME)

		self.config.set('log', 'base_dir', self.LOG_BASE_DIR)
		self.config.set('log', 'file_name', self.LOG_FILE_NAME)

		with open(self.file_name, 'wb') as configfile:
			self.config.write(configfile)

if __name__ == "__main__":
	openBCcfg = OpenBCcfg("cfg/openBC.cfg")
	openBCcfg.readConfigFile()
	openBCcfg.IP = "127.0.0.44"
	openBCcfg.SCREW_ENABLED = "1"
	openBCcfg.WriteConfigFile()




