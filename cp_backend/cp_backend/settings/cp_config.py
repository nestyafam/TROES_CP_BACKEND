OPERATING_MODE = "local"
SIMULATION = False
SYSTEM_FIELDS = {
    "pcs": {
        "on_off_grid_switch": {
            "address": 53600,
            "length": 2,
            "toggle_values": {

                0: {
                    "normal": [53600],
                    "large": [53600]
                },

                1: {
                    "normal": [53600],
                    "large": [53600]
                }
            }
        },
        "pcs_start": {
            "address": 53900,
            "length": 2,
            "toggle_values": {
                0: {
                    "normal": [53900],
                    "large": [53900]

                },
                1: {
                    "normal": [53900],
                    "large": [53900]
                }
            }
        },
        "pcs_stop": {
            "address": 53901,
            "length": 2,
            "toggle_values": {
                0: {
                    "normal": [53901],
                    "large": [53901]
                }
                ,
                1: {
                    "normal": [53901],
                    "large": [53901]
                }
            }
        },
        "active_power": {
            "address": 53622,
            "length": 2,
            "range": (0, 500)
        },
        "reactive_power": {
            "address": 53623,
            "length": 2,
            "range": (0, 500)
        }
    },
    "bms": {
        "high_voltage_box_contactor": {
            "address": 62701,
            "length": 2,
            "toggle_values": {
                0: {
                    # for normal and large systems the registers and no of registers might be different
                    # for example below, for large systems 0 should be sent to 62701 and 62702
                    # while for small system 0 should be sent to 62700
                    "normal": [62700],
                    "large": [62701, 62702]
                }
                ,
                1: {
                    "normal": [62700],
                    "large": [62700]
                }
            }
        },
    },
    "arm": {
        "km1": {
            "address": 40002,
            "multiplier": 8,
            "toggle_values": {
                0: {
                    "normal": [40002],
                    "large": [40002]
                }
                ,
                1: {
                    "normal": [40002],
                    "large": [40002]
                }
            }
        },
        "km2": {
            "address": 40003,
            "multiplier": 8,
            "toggle_values": {
                0: {
                    "normal": [40003],
                    "large": [40003]
                }
                ,
                1: {
                    "normal": [40003],
                    "large": [40003]
                }
            }
        },
        "km3": {
            "address": 40004,
            "multiplier": 8,
            "toggle_values": {
                0: {
                    "normal": [40004],
                    "large": [40004]
                }
                ,
                1: {
                    "normal": [40004],
                    "large": [40004]
                }
            }
        },
        "ac_switch": {
            "address": 40301,
            "multiplier": 24,
            "toggle_values": {
                0: {
                    "normal": [40301],
                    "large": [40301]
                }
                ,
                1: {
                    "normal": [40301],
                    "large": [40301]
                }
            }
        },
        "battery_bin_1_fan": {
            "address": 40305,
            "multiplier": 8,
            "toggle_values": {
                0: {
                    "normal": [40305],
                    "large": [40305]
                }
                ,
                1: {
                    "normal": [40305],
                    "large": [40305]
                }
            }
        },
        "battery_bin_2_fan": {
            "address": 40307,
            "multiplier": 8,
            "toggle_values": {
                0: {
                    "normal": [40307],
                    "large": [40307]
                }
                ,
                1: {
                    "normal": [40307],
                    "large": [40307]
                }
            }
        },
        "pcs_cabinet_fan": {
            "address": 40306,
            "multiplier": 8,
            "toggle_values": {
                0: {
                    "normal": [40306],
                    "large": [40306]
                }
                ,
                1: {
                    "normal": [40306],
                    "large": [40306]
                }
            }
        },
        "ac_cooling_on_temp": {
            "address": 40317,
            "multiplier": 24,
            "range": (25, 28)
        },
        "ac_cooling_off_temp": {
            "address": 40318,
            "multiplier": 24,
            "range": (20, 24)
        },
        "ac_heating_on_temp": {
            "address": 40321,
            "multiplier": 24,
            "range": (10, 15)
        }
        ,
        "ac_heating_off_temp": {
            "address": 40322,
            "multiplier": 24,
            "range": (20, 25)
        },
        "battery_compartment_fan_on_temp": {
            "address": 40401,
            "multiplier": 6,
            "range": (30, 35)
        },
        "battery_compartment_fan_off_temp": {
            "address": 40402,
            "multiplier": 6,
            "range": (25, 30)
        },
        "pcs_cabinet_fan_on_temp": {
            "address": 40405,
            "multiplier": 6,
            "range": (30, 35)
        },
        "pcs_cabinet_fan_off_temp": {
            "address": 40406,
            "multiplier": 6,
            "range": (25, 30)
        },
        "high_temp_alarm_value": {
            "address": 40201,
            "multiplier": 4,
            "range": ()
        },
        "low_temp_alarm_value": {
            "address": 40202,
            "multiplier": 4,
            "range": ()
        },
        "high_humidity_alarm_value": {
            "address": 40203,
            "multiplier": 4,
            "range": ()
        },
        "low_humidity_alarm_value": {
            "address": 40204,
            "multiplier": 4,
            "range": ()
        },

        "high_temp_system_cutoff_value": {
            "address": 40205,
            "length": 1,
            "range": ()
        },
        "low_temp_system_cutoff_value": {
            "address": 40206,
            "length": 1,
            "range": ()
        },
        "high_humidity_system_cutoff_value": {
            "address": 40207,
            "length": 1,
            "range": ()
        },
        "low_humidity_system_cutoff_value": {
            "address": 40208,
            "length": 1,
            "range": ()
        },
    },

}
SUB_SYSTEM_FIELDS = {
    "pcs": {
        "sub_system_test": {
            "address": 40002,
            "multiplier": 8,
            "toggle_values": {
                0: {
                    "normal": [40002],
                    "large": [40002]
                }
                ,
                1: {
                    "normal": [40002],
                    "large": [40002]
                }
            }
        }
    },
    "bms": {

    },
    "arm": {

    },

}

SYSTEM_DETAILS = {
    "ip": "10.8.0.3",
    "bc_count": 4,
    "bsu_count": 12,
    "cell_count": 16,
    # system type is normal if the no of clusters are less than or equal to 16
    # type is large if the no is more than 16
    "type": "large",
    "pcs": {
        "ip": "10.16.32.2",
        "port": 502
    },
    "bms": {
        "ip": "10.16.32.1",
        "port": 502
    },
    "arm": {
        "ip": "10.16.32.3",
        "port": 502
    }
}
# system sizes below based on the no of clusters in the system
system_sizes = {
    "normal": 16
}

UI_MAPPING = {
    "manualControls": [
        {
            "name": "High Voltage Box Contactor",
            "key": "high_voltage_box_contactor",
            "options": [{"option": 'open', "clicked": False}, {"option": 'combine', "clicked": False}]
        },
        {
            "name": "PCS Compartment Main Contactor",
            "key": "km1",
            "options": [{"option": 'open', "clicked": False}, {"option": 'combine', "clicked": False}]
        },
        {
            "name": "PCS Warehouse Auxiliary Contactor KM2",
            "key": "km2",
            "options": [{"option": 'open', "clicked": False}, {"option": 'combine', "clicked": False}]
        },
        {
            "name": "Air conditioner Switch Machine",
            "key": "ac_switch",
            "options": [{"option": 'boot', "clicked": False}, {"option": 'shutdown', "clicked": False}]
        },
        {
            "name": "Battery Compartment Fan",
            "key": "battery_bin_1_fan",
            "options": [{"option": 'open', "clicked": False}, {"option": 'close', "clicked": False}]
        },
        {
            "name": "PCS Cabinet Fan",
            "key": "pcs_cabinet_fan",
            "options": [{"option": 'open', "clicked": False}, {"option": 'combine', "clicked": True}]
        },
        {
            "name": "Battery compartment 2 Fan",
            "key": "battery_bin_2_fan",
            "options": [{"option": 'open', "clicked": True}, {"option": 'combine', "clicked": False}]
        },
        {
            "name": "Auxiliary contactor for KM3 for PCS",
            "key": "km3",
            "options": [{"option": 'boot', "clicked": False}, {"option": 'shutdown', "clicked": False}]
        }
    ],
    "automaticControls": [
        {
            "name": "Air Conditioner refrigeration Turn on Temperature",
            "key": "ac_cooling_on_temp",
            "value": 17.2
        },
        {
            "name": "Air Conditioner refrigeration Turn off Temperature",
            "key": "ac_cooling_off_temp",
            "value": 17.2
        },
        {
            "name": "Air Conditioner heating Turn on Temperature",
            "key": "ac_heating_on_temp",
            "value": 17.2
        },
        {
            "name": "Air Conditioner heating Turn off Temperature",
            "key": "ac_heating_off_temp",
            "value": 17.2
        },
        {
            "name": "Battery Compartment Fan Turn On Temperature",
            "key": "battery_compartment_fan_on_temp",
            "value": 17.2
        },
        {
            "name": "Battery Compartment Fan Turn Off Temperature",
            "key": "battery_compartment_fan_off_temp",
            "value": 17.2
        },
        {
            "name": "PCS Compartment Fan Turn On Temperature",
            "key": "pcs_cabinet_fan_on_temp",
            "value": 17.2
        },
        {
            "name": "PCS Cabinet Fan Off Temperature",
            "key": "pcs_cabinet_fan_off_temp",
            "value": 17.2
        }
    ],
    "automaticProtection": [
        {
            "name": "High Temperature Alarm",
            "key": "high_temp_alarm_value",
            "value": 17.2
        },
        {
            "name": "Low Temperature Alarm",
            "key": "low_temp_alarm_value",
            "value": 17.2
        },
        {
            "name": "High Humidity Alarm",
            "key": "high_humidity_alarm_value",
            "value": 17.2
        },
        {
            "name": "Low Humidity Alarm",
            "key": "low_humidity_alarm_value",
            "value": 17.2
        },
        {
            "name": "High Temperature Cut-Off System",
            "key": "high_temp_system_cutoff_value",
            "value": 17.2
        },
        {
            "name": "Low Temperature Cut-Off System",
            "key": "low_temp_system_cutoff_value",
            "value": 17.2
        },
        {
            "name": "High Humidity Cut-Off System",
            "key": "high_humidity_system_cutoff_value",
            "value": 17.2
        },
        {
            "name": "Low Humidity Cut-Off System",
            "key": "low_humidity_system_cutoff_value",
            "value": 17.2
        }
    ],
    "pcsStateSwitch": [
        {
            "name": "PCS Switch Machine",
            "key": "pcs_start_stop",
            "options": [{"option": 'open', "clicked": False}, {"option": 'combine', "clicked": False}]
        },
        {
            "name": "ON and OFF Grid Switching",
            "key": "on_off_grid_switch",
            "options": [{"option": 'boot', "clicked": False}, {"option": 'shutdown', "clicked": False}]
        },
        {
            "name": "Active Power",
            "key": "active_power",
            "value": 800
        },
        {
            "name": "Reactive Power",
            "key": "reactive_power",
            "value": 0
        }
    ]}
