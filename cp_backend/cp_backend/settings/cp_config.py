OPERATING_MODE = "local"

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
            "length": 2
        },
        "reactive_power": {
            "address": 53623,
            "length": 2
        }
    },
    "bms": {
        "high_voltage_box_contractor": {
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
        "pcs_barn_fan": {
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
        "ip": "10.8.0.3",
        "port": 502
    },
    "bms": {
        "ip": "10.8.0.3",
        "port": 2502
    },
    "arm": {
        "ip": "10.8.0.3",
        "port": 3502
    }
}
# system sizes below based on the no of clusters in the system
system_sizes = {
    "normal": 16
}
