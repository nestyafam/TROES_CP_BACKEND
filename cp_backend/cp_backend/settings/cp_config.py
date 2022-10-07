OPERATING_MODE = "local"

SYSTEM_FIELDS = {
    "pcs": {
        "on_off_grid_switch": {
            "address": 53600,
            "length": 2,
            "toggle_values": [0, 1]
        },
        "pcs_start_stop": {
            "address": 53900,
            "length": 2,
            "toggle_values": [0, 1]
        },
        "active_power": {
            "address": 53622,
            "length": 2
        },
        "reactive_power": {
            "address": 53623,
            "length": 2
        }
    },
    "bms": {

    },
    "arm": {
        "km1": {
            "address": 40002,
            "multiplier": 8,
            "toggle_values": [0, 1]
        },
        "km2": {
            "address": 40003,
            "multiplier": 8,
            "toggle_values": [0, 1]
        }, "km3": {
            "address": 40004,
            "multiplier": 8,
            "toggle_values": [0, 1]
        },
        "ac_switch": {
            "address": 40301,
            "multiplier": 24,
            "toggle_values": [0, 1]
        },
        "battery_bin_1_fan": {
            "address": 40005,
            "multiplier": 8,
            "toggle_values": [0, 1]
        },
        "battery_bin_2_fan": {
            "address": 40007,
            "multiplier": 8,
            "toggle_values": [0, 1]
        },
        "pcs_barn_fan": {
            "address": 40006,
            "multiplier": 8,
            "toggle_values": [0, 1]
        },
        "ac_refrigeration_opening_temp": {
            "address": 40317,
            "multiplier": 24
        },
        "ac_cooling_off_return_temp": {
            "address": 40318,
            "multiplier": 24
        },
        "ac_heating_and_opening_temp": {
            "address": 40321,
            "multiplier": 24
        }
        ,
        "ac_heating_off_return_temp": {
            "address": 40322,
            "multiplier": 24
        },
        "battery_compartment_fan_open_temp": {
            "address": 40401,
            "multiplier": 6
        },
        "battery_compartment_fan_shut_off_temp": {
            "address": 40402,
            "multiplier": 6
        },
        "pcs_warehouse_fan_open_temp": {
            "address": 40405,
            "multiplier": 6
        },
        "pcs_warehouse_fan_shut_off_temp": {
            "address": 40406,
            "multiplier": 6
        },
        "high_temp_alarm_value": {
            "address": 40201,
            "multiplier": 4
        },
        "low_temp_alarm_value": {
            "address": 40202,
            "multiplier": 4
        },
        "high_humidity_alarm_value": {
            "address": 40203,
            "multiplier": 4
        },
        "low_humidity_alarm_value": {
            "address": 40204,
            "multiplier": 4
        },
        "high_voltage_box_contractor": {
            "address": 62701,
            "length": 2,
            "toggle_values": [0, 1]
        },
        "high_temp_system_cutoff_value": {
            "address": 40205,
            "length": 1
        },
        "low_temp_system_cutoff_value": {
            "address": 40206,
            "length": 1
        },
        "high_humidity_system_cutoff_value": {
            "address": 40207,
            "length": 1
        },
        "low_humidity_system_cutoff_value": {
            "address": 40208,
            "length": 1
        },
    },

}
SUB_SYSTEM_FIELDS = {
    "pcs": {
    },
    "bms": {

    },
    "arm": {

    },

}

SYSTEM_DETAILS = {
    "ip": "10.8.0.10",
    "bc_count": 4,
    "bsu_count": 12,
    "cell_count": 16,
    "pcs_config": {
        "ip": "192.168.1.10",
        "port": "502"
    },
    "bms_config": {
        "ip": "192.168.1.100",
        "port": "502"
    },
    "arm_config": {
        "ip": "192.168.1.121",
        "port": "502"
    }
}
