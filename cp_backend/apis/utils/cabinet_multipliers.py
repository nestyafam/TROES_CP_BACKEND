RTU_MULTIPLIERS = {
    'voltage': 0.001,
    'temperature': 0.1,
    "air_conditioner_coil_temperature": 0.1,
    "air_conditioner_outdoor_temperature_spare": 0.1,
    "air_conditioner_condensing_temperature": 0.1,
    "air_conditioner_indoor_temperature": 0.1,
    "air_conditioner_humidity": 1.0,
    "air_conditioner_AC_current_spare": 0.001,
    "air_conditioner_DC_voltage_spare": 0.1,
    "air_conditioner_exhaust_temperature_spare": 0.1,
    "air_conditioner_heating_start_temperature_setting_value": 1.0,
    "air_conditioner_heating_return_difference_temperature_setting_value": 1.0,
    "air_conditioner_high_temperature_alarm_setting_value": 1.0,
    "air_conditioner_low_temperature_alarm_setting_value": 1.0,
    "battery_soc": 0.1,
    "battery_soh": 0.1

}

RTU_BINARY_FIELDS = [
    "air_conditioner_alarm_status_1",
    "air_conditioner_alarm_status_2",
    "air_conditioner_alarm_status_3"
]

def get_cabinet_multiplier(key):
    """
    params: key
    return: values of RTU_MULTIPLIERS if key matches else None
    """
    multiplier = RTU_MULTIPLIERS.get(key, None)
    if not multiplier:
        return 1
    return multiplier




