import ConfigParser

class OpenBCcfg(object):

	def __init__(self, file_name):

		self.config = ConfigParser.RawConfigParser()
		self.config.read(file_name)

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

if __name__ == "__main__":
	openBCcfg = openBCcfg("openWB.cfg")
	print openBCcfg.LAMBDA_SENSOR_PORT