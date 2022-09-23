fields_data = {
    "cellVol": {
        "fields": ["cellVol"],
        "starting_address": 100,
        "type": "repeat"
    },
    "cellTemp": {
        "fields": ["cellTemp"],
        "starting_address": 19200,
        "type": "repeat"
    },
    "bmuBoardTemp": {
        "fields": ["bmuBoardTemp"],
        "starting_address": 28800,
        "type": "repeat"
    },
    "bmuBalanceTemp": {
        "fields": ["bmuBalanceTemp"],
        "starting_address": 32640,
        "type": "repeat"
    },
    "bmuBalanceState": {
        "fields": ["bmuBalanceState"],
        "starting_address": 36480,
        "type": "repeat"
    },
    "bcu_data": {
        "fields": ["InternalSumVoltage", "Current", "ExternalSumVoltage", "FuseVoltage", "MaxCellVInfo",
                   "MaxCellVBmuNo", "MaxCellVCellNo", "MinCellVInfo", "MinCellVBmuNo", "MinCellVCellNo",
                   "MaxCellTempInfo", "MaxCellTBmuNo", "MaxCellTCellNo", "MinCellTempInfo", "MinCellTBmuNo",
                   "MinCellTCellNo", "USOC", "SOH", "ASOC", "CycleCount", "MaxPermitChgCurr", "MaxPermitDsgCurr",
                   "FCCCapacity", "RemainCapacity", "TotalInCap", "TotalInCap", "TotalOutCap", "TotalOutCap",
                   "TotalInEng", "TotalInEng", "TotalOutEng", "TotalOutEng", "BCUBoardTemp01", "BCUBoardTemp02",
                   "BCUBoardTemp03", "MainSWVersion", "SubSWVersion", "MainHWVersion", "SubHWVersion", "BMSSeriseNUM",
                   "BMSSeriseNUM", "ChgPowerAlarmThrhd", "DsgPowerAlarmThrhd", "AsocOCV", "AsocAh0", "AsocAh1",
                   "AsocFull0", "AsocFull1", "AsocEmpty0", "AsocEmpty1", "PassedCharge0", "PassedCharge1", "SOCflag",
                   "CellNum", "CellCapacity", "BreakVoltage", "SumVoltage", "Qmax", "BMSRunMode", "BMSWorkMode",
                   "ProtectAlarm0_8", "ProtectAlarm0_8", "ProtectAlarm0_8", "ProtectAlarm0_8", "SysFaultCode0_8",
                   "SysFaultCode0_8", "SysFaultCode0_8", "SysFaultCode0_8", "OtherErrorCode0_8", "OtherErrorCode0_8",
                   "OtherErrorCode0_8", "OtherErrorCode0_8", "HwErrorCode0_8", "HwErrorCode0_8", "HwErrorCode0_8",
                   "HwErrorCode0_8", "HwStateCode0_8", "HwStateCode0_8", "HwStateCode0_8", "HwStateCode0_8",
                   "ActuatorStaCode0_8", "ActuatorStaCode0_8", "ActuatorStaCode0_8", "ActuatorStaCode0_8", "HvPowOnReq",
                   "HvPowOnState", "LvShutDownReq", "FullChgCalibReq", "BcuLimitCurrState", "BcuLife",
                   "InsulResistance", "AvgCellVolt", "BCUHSDTemp01", "BCUHSDTemp02", "BCUHSDTemp03", "BCUHSDTemp04",
                   "BCUHSDTemp05", "BCUHSDTemp06", "BCUHSDTemp07", "BmuNumber", "BcuNumber", "MaxChargePower",
                   "MaxDisChargePower", "BmuAfeCommFault", "BmuAfeCommFault", "BmuFuseFault", "BmuFuseFault",
                   "BmuCommFault", "BmuCommFault", "ProtectAlarmLevel1", "ProtectAlarmLevel1", "ProtectAlarmLevel2",
                   "ProtectAlarmLevel2", "ProtectAlarmLevel3", "ProtectAlarmLevel3", "SysFaultLevel1", "SysFaultLevel1",
                   "SysFaultLevel2", "SysFaultLevel2", "SysFaultLevel3", "SysFaultLevel3", "HwErrLevel1", "HwErrLevel1",
                   "HwErrLevel2", "HwErrLevel2", "HwErrLevel3", "HwErrLevel3", "BcuAsMasterAllowMaxPermitChargePower",
                   "BcuAsMasterAllowMaxPermitDisChargePower"],
        "starting_address": 50000,
        "type": "repeat"
    },
    "bams_data": {
        "fields": ["BamsVoltage", "BamsVoltage", "BamsCurrent", "BamsCurrent", "BamsPower", "BamsPower", "BamsSoc",
                   "BamsSoh", "BamsPermitChgPower", "BamsPermitChgPower", "BamsPermitDsgPower", "BamsPermitDsgPower",
                   "BamsPermitChgCurrent", "BamsPermitChgCurrent", "BamsPermitDsgCurrent", "BamsPermitDsgCurrent",
                   "BamsBcuSocDiff", "BamsBcuMinSoc", "BamsBcuMinSocNo", "BamsBcuMaxSoc", "BamsBcuMaxSocNo",
                   "BamsMaxCellVol", "BamsMaxCellVBcuBmuNo", "BamsMaxCellVNo", "BamsMinCellVol", "BamsMinCellVBcuBmuNo",
                   "BamsMinCellVNo", "BamsAvgCellVol", "BamsCellVolDiff", "BamsMaxCellT", "BamsMaxCellTBcuBmuNo",
                   "BamsMaxCellTNo", "BamsMinCellT", "BamsMinCellTBcuBmuNo", "BamsMinCellTNo", "BamsAvgCellT",
                   "BamsCellTDiff", "BamsMaxBcuVol", "BamsMaxBcuVNo", "BamsMinBcuVol", "BamsMinBcuVNo", "BamsBcuAvgVol",
                   "BamsBcuVolDiff", "BamsMaxBcuCurr", "BamsMaxBcuCNo", "BamsMinBcuCurr", "BamsMinBcuCNo",
                   "BamsTotalInCap", "BamsTotalInCap", "BamsTotalOutCap", "BamsTotalOutCap", "BamsTotalInEng",
                   "BamsTotalInEng", "BamsTotalOutEng", "BamsTotalOutEng", "BamsResistance", "BcuHvOnOffStaMap",
                   "BcuHvOnOffStaMap", "BcuHvOnOffStaMap", "BcuHvOnOffStaMap", "BcuLvOffReqMap", "BcuLvOffReqMap",
                   "BcuLvOffReqMap", "BcuLvOffReqMap", "BcuHvOnOffReqMap", "BcuHvOnOffReqMap", "BcuHvOnOffReqMap",
                   "BcuHvOnOffReqMap", "BcuFullChgReqMap", "BcuFullChgReqMap", "BcuFullChgReqMap", "BcuFullChgReqMap",
                   "BamsCtlHvOnOffMap", "BamsCtlHvOnOffMap", "BamsCtlHvOnOffMap", "BamsCtlHvOnOffMap",
                   "BamsCtlLvShutDown", "BamsCtlFullChg", "BamsCtlHvOnToOffFlg", "BamsExtSWVer", "BamsExtSWVer",
                   "BamsIntSWVer", "BamsIntSWVer", "BamsHWVer", "BamsUsedEnergy", "BamsUsedEnergy", "BamsLeftEnergy",
                   "BamsLeftEnergy", "BamsUsedCap", "BamsUsedCap", "BamsLeftCap", "BamsLeftCap", "BamsForceChgFlag",
                   "BamsAddrBcuOk", "Reserve1", "Reserve1", "Reserve2", "Reserve2", "Reserve3", "Reserve3", "Reserve4",
                   "Reserve4", "Reserve5", "Reserve5", "Reserve6", "Reserve6", "Reserve7", "Reserve7", "Reserve8",
                   "Reserve8", "Reserve9", "Reserve9", "Reserve10", "Reserve10", "Reserve11", "Reserve11", "Reserve12",
                   "Reserve12", "Reserve13", "Reserve13", "Reserve14", "Reserve14", "BamsProtAlarm0_8",
                   "BamsProtAlarm0_8", "BamsProtAlarm0_8", "BamsProtAlarm0_8", "BamsSysFaultCode0_8",
                   "BamsSysFaultCode0_8", "BamsSysFaultCode0_8", "BamsSysFaultCode0_8", "BamsOtherErrCode0_8",
                   "BamsOtherErrCode0_8", "BamsOtherErrCode0_8", "BamsOtherErrCode0_8", "BamsHwErrCode0_8",
                   "BamsHwErrCode0_8", "BamsHwErrCode0_8", "BamsHwErrCode0_8", "BamsHwStaCode0_8", "BamsHwStaCode0_8",
                   "BamsHwStaCode0_8", "BamsHwStaCode0_8", "BamsFaultCode0_8", "BamsFaultCode0_8", "BamsFaultCode0_8",
                   "BamsFaultCode0_8", "Reserve15", "Reserve16", "Reserve17", "BcuOnlineMap", "BcuOnlineMap",
                   "BcuOnlineMap", "BcuOnlineMap", "MsBamsCommState", "BamsAllowHvOnMap", "BamsAllowHvOnMap",
                   "BamsAllowHvOnMap", "BamsAllowHvOnMap"],
        "starting_address": 62000,
        "type": "no_repeat"
    },
    "bams_esu_data": {
        "fields": ["TempHumiNum", "TempNum", "HumiNum", "DoorNum", "FloodingNum", "SmokeNum", "LeakNumIO", "LeakNumPhy",
                   "RsvDI1", "RsvDI2", "RsvDI3", "RsvDI4", "RsvDI5", "RsvDI6", "RsvDI7", "RsvPhyDev1", "RsvPhyDev2",
                   "RsvPhyDev3", "RsvPhyDev4", "RsvPhyDev5", "DoControl", "FanControl", "FaultStatus1", "FaultStatus2",
                   "FaultStatus3", "FaultStatus4", "FaultStatus5", "FaultStatus6", "EnvTemp1", "EnvTemp2", "EnvTemp3",
                   "EnvTemp4", "EnvTemp5", "Humidity1", "Humidity2", "Humidity3", "Humidity4", "Humidity5", "TH_Temp1",
                   "TH_Humidity1", "TH_Temp2", "TH_Humidity2", "TH_Temp3", "TH_Humidity3", "TH_Temp4", "TH_Humidity4",
                   "TH_Temp5", "TH_Humidity5", "Aerosol1", "Aerosol2", "Aerosol3", "Aerosol4", "Aerosol5", "DoorStatus",
                   "FloodingStatus", "SmokeStatus", "LeakSensorIO", "DOStatus", "FANStatus", "HallLargeCurr",
                   "HallSmallCurr", "SumVoltage", "AI0DataAcquisition", "AI1DataAcquisition", "AI2DataAcquisition",
                   "AI3DataAcquisition", "AI4DataAcquisition", "AI5DataAcquisition", "AI0Eevicetype", "AI1Eevicetype",
                   "AI2Eevicetype", "AI3Eevicetype", "AI4Eevicetype", "AI5Eevicetype", "DiDeviceStatusRsv1",
                   "DiDeviceStatusRsv2", "DiDeviceStatusRsv3", "DiDeviceStatusRsv4", "DiDeviceStatusRsv5",
                   "DiDeviceStatusRsv6", "DiDeviceStatusRsv7", "DiDectStatus"],
        "starting_address": 62500
    },
    "hvac_data": [
        {
            "starting_address": 40001,
            "multiplier": 8,
            "fields": ["relay1", "relay2", "relay3", "relay4", "relay5", "relay6", "relay7", "relay8"]
        },
        {
            "starting_address": 40101,
            "multiplier": 6,
            "fields": ["Temp", "Humi", "IN1", "IN2", "Water1", "Water2"]
        },
        {
            "starting_address": 40201,
            "multiplier": 4,
            "fields": ["TempUpper", "TempLower", "HumiUpper", "HumiLower"]
        },
        {
            "starting_address": 40301,
            "multiplier": 24,
            "fields": ["MachineState", "InternalFanState", "ExternalFanState", "CompressorState", "HeatState",
                       "ReturnAirTempFault", "EvaporatorTempFault", "CondenserTempFault", "HighPreesureAlarm",
                       "CabinetInsideHighTemp", "CabinetInsideLowTemp", "EvaportatorFreezedAlarm",
                       "RefrigerantLeakageAlarm", "IndoorReturnTemp", "EvaporatorTemp", "CondenserTemp",
                       "CompressorStartTemp", "CompressorReturnDiff", "HighTempLimit", "LowTempLimit",
                       "HeaterStartTemp", "HeaterReturnDiff", "HydrogenState", "DeviceAddr"]
        }
    ],
    "pcs_data_1": {
        "fields": ["AC_line_voltage_L1_to_L2", "AC_line_voltage_L2_to_L3", "AC_line_voltage_L3_to_L1", "AC_L1_current",
                   "AC_L2_current", "AC_L3_current", "AC_frequency", "reserve", "reserve", "L1_AC_active_power",
                   "L2_AC_active_power",
                   "L3_AC_active_power", "L1_AC_reactive_power", "L2_AC_reactive_power", "L3_AC_reactive_power",
                   "L1_AC_apparent_power", "L2_AC_apparent_power", "L3_AC_apparent_power", "L1_AC_PF", "L2_AC_PF",
                   "L3_AC_PF", "Module_temperature", "reserve", "Ambient_temperature"],
        "starting_address": 53200
    },
    "pcs_data_2": {
        "fields": ["Total_AC_active_power",
                   "Total_AC_reactive_power", "Total_AC_apparent_power", "Total_AC_PF",
                   "Accumulative_charged_energy_through_AC_port_Higher_2_bytes",
                   "Accumulative_charged_energy_through_AC_port_Lower_2_bytes",
                   "Accumulative_discharged_energy_through_AC_port_higher_2_bytes",
                   "Accumulative_discharged_energy_through_AC_port_lower_2_bytes", "reserve", "reserve", "reserve",
                   "Maximum_operating_capacity",
                   "daily_charged_energy_through_AC_port", "daily_discharged_energy_through_AC_port"],
        "starting_address": 53235
    },
    "pcs_data_3": {
        "fields": ["DC_power", "DC_voltage", "DC_current", "Accumulative_charged_energy_through_DC_port_Higher_2_bytes",
                   "Accumulative_charged_energy_through_DC_port_Lower_2_bytes",
                   "Accumulative_discharged_energy_through_DC_port_Higher_2_bytes",
                   "Accumulative_discharged_energy_through_DC_port_Lower_2_bytes"],
        "starting_address": 53250
    }

}
