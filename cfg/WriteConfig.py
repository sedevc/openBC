import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('info')
config.set('info', 'hw_name', 'openWB_viktor_edition')
config.set('info', 'ip', '127.5.0.2')
config.set('info', 'evok_url', 'http://127.0.0.1/rpc')

config.add_section('boiler_temp_sensor')
config.set('boiler_temp_sensor', 'enabled', 'yes')
config.set('boiler_temp_sensor', 'type', 'DS18B20')
config.set('boiler_temp_sensor', 'base_dir', '/sys/bus/w1/devices/')
config.set('boiler_temp_sensor', 'file_name', 'w1_slave')
config.set('boiler_temp_sensor', 'id', '28E6E8500500008C')

config.add_section('tank_temp_sensor')
config.set('tank_temp_sensor', 'enabled', 'yes')
config.set('tank_temp_sensor', 'type', 'DS18B20')
config.set('tank_temp_sensor', 'base_dir', '/sys/bus/w1/devices/')
config.set('tank_temp_sensor', 'file_name', 'w1_slave')
config.set('tank_temp_sensor', 'id', '2888045105000028')

config.add_section('fire_temp_sensor')
config.set('fire_temp_sensor', 'enabled', 'yes')
config.set('fire_temp_sensor', 'type', 'K-Type 0-5V')
config.set('fire_temp_sensor', 'analog_pin', '2')

config.add_section('lambda_sensor')
config.set('lambda_sensor', 'enabled', '1')
config.set('lambda_sensor', 'type', 'LC-2')
config.set('lambda_sensor', 'port', '/dev/ttyUSB0')
config.set('lambda_sensor', 'baud', '19200')
config.set('lambda_sensor', 'sync_header_attempt', '10')
config.set('lambda_sensor', 'analog_pin', '1')
config.set('lambda_sensor', 'contactor_pin', '7')

config.add_section('control_button')
config.set('control_button', 'contactor_pin', '6')
config.set('control_button', 'emergency_stop_gpio', '1')
config.set('control_button', 'auto_man_gpio', '2')
config.set('control_button', 'man_screw_forward_gpio', '3')
config.set('control_button', 'man_screw_backward_gpio', '4')
config.set('control_button', 'man_fan_forward_gpio', '4')
config.set('control_button', 'reset_gpio	', '5')

config.add_section('timers')
config.set('timers', 'block_time', '100')
config.set('timers', 'block_time_idle', '300')
config.set('timers', 'run_time_fan_idle', '30')
config.set('timers', 'run_time_screw', '3')
config.set('timers', 'run_time_screw_idle', '5')
config.set('timers', 'log_block_time', '15')


config.add_section('limits')
config.set('limits', 'tank_set_temp', '30')
config.set('limits', 'boiler_set_temp', '85')
config.set('limits', 'fire_set_temp', '300')
config.set('limits', 'idle_fire_set_temp', '200')

config.add_section('fan')
config.set('fan', 'enabled', '1')
config.set('fan', 'type', 'G1G120-AB67-02')
config.set('fan', 'analog_pin', '1')
config.set('fan', 'safe_mode_speed', '2')
config.set('fan', 'contactor_pin', '8')


config.add_section('screw')
config.set('screw', 'enabled', 'True')
config.set('screw', 'type', 'Relay')
config.set('screw', 'contactor_pin', '5')

config.add_section('database')
config.set('database', 'enabled', 'True')
config.set('database', 'type', 'SQLite')
config.set('database', 'db_name', 'data_temp.db')

config.add_section('log')
config.set('log', 'base_dir', '/tmp/')
config.set('log', 'file_name', 'openWB.log')




# Writing our configuration file to 'openBC.cfg'
with open('openBC.cfg', 'wb') as configfile:
    config.write(configfile)


