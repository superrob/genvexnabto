from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoCTS400(GenvexNabtoBaseModel):
    def __init__(self, slaveDeviceModel):
        super().__init__(slaveDeviceModel)

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(address=28, divider=10),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(address=27, divider=10),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(address=30, divider=10),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(address=29, divider=10),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(address=31, divider=10),
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(address=25, divider=10),
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(address=24, divider=10),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(address=23),
            GenvexNabtoDatapointKey.SUMMER_MODE: GenvexNabtoDatapoint(address=72),
            GenvexNabtoDatapointKey.CO2_LEVEL: GenvexNabtoDatapoint(address=47),
            GenvexNabtoDatapointKey.FILTER_DAYS_LEFT: GenvexNabtoDatapoint(address=110),
            GenvexNabtoDatapointKey.DEFROST_ACTIVE: GenvexNabtoDatapoint(address=91),
            GenvexNabtoDatapointKey.DEFORST_TIMESINCELAST: GenvexNabtoDatapoint(address=89),
            GenvexNabtoDatapointKey.ALARM_CTS400CRITICAL: GenvexNabtoDatapoint(address=79),
            GenvexNabtoDatapointKey.ALARM_CTS400WARNING: GenvexNabtoDatapoint(address=80),
            GenvexNabtoDatapointKey.ALARM_CTS400INFO: GenvexNabtoDatapoint(address=82)             
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_address=69, write_address=69, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_address=37, write_address=37, divider=10, min=0, max=300, step=0.5),
            GenvexNabtoSetpointKey.FILTER_RESET: GenvexNabtoSetpoint(read_address=51, write_address=51, min=0, max=1),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1: GenvexNabtoSetpoint(read_address=59, write_address=59, divider=10, min=200, max=1000),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2: GenvexNabtoSetpoint(read_address=60, write_address=60, divider=10, min=200, max=1000),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3: GenvexNabtoSetpoint(read_address=61, write_address=61, divider=10, min=200, max=1000),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL4: GenvexNabtoSetpoint(read_address=62, write_address=62, divider=10, min=200, max=1000),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1: GenvexNabtoSetpoint(read_address=63, write_address=63, divider=10, min=200, max=1000),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2: GenvexNabtoSetpoint(read_address=64, write_address=64, divider=10, min=200, max=1000),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3: GenvexNabtoSetpoint(read_address=65, write_address=65, divider=10, min=200, max=1000),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL4: GenvexNabtoSetpoint(read_address=66, write_address=66, divider=10, min=200, max=1000),
            GenvexNabtoSetpointKey.VENTILATION_ENABLE: GenvexNabtoSetpoint(read_address=70, write_address=70, min=0, max=1),
            GenvexNabtoSetpointKey.CTS400_HUMIDITY_LOW_LEVEL: GenvexNabtoSetpoint(read_address=31, write_address=31, divider=10, min=150, max=450),
            GenvexNabtoSetpointKey.CTS400_HUMIDITY_LOW_STEP: GenvexNabtoSetpoint(read_address=32, write_address=32, min=0, max=3),
            GenvexNabtoSetpointKey.CTS400_HUMIDITY_HIGH_STEP: GenvexNabtoSetpoint(read_address=33, write_address=33, min=2, max=4),
            GenvexNabtoSetpointKey.CTS400_HUMIDITY_HIGH_MAX_TIME: GenvexNabtoSetpoint(read_address=34, write_address=34, min=0, max=180),
        }

        self._defaultDatapointRequest = [
            GenvexNabtoDatapointKey.TEMP_SUPPLY,
            GenvexNabtoDatapointKey.TEMP_OUTSIDE,
            GenvexNabtoDatapointKey.TEMP_EXHAUST,
            GenvexNabtoDatapointKey.TEMP_EXTRACT,
            GenvexNabtoDatapointKey.HUMIDITY,
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY,
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT,
            GenvexNabtoDatapointKey.BYPASS_ACTIVE,
            GenvexNabtoDatapointKey.SUMMER_MODE,
            GenvexNabtoDatapointKey.CO2_LEVEL,
            GenvexNabtoDatapointKey.FILTER_DAYS_LEFT,
            GenvexNabtoDatapointKey.DEFROST_ACTIVE,
            GenvexNabtoDatapointKey.DEFORST_TIMESINCELAST,
            GenvexNabtoDatapointKey.ALARM_CTS400CRITICAL,
            GenvexNabtoDatapointKey.ALARM_CTS400WARNING,
            GenvexNabtoDatapointKey.ALARM_CTS400INFO
        ]

        self._defaultSetpointRequest = [
            GenvexNabtoSetpointKey.FAN_SPEED,
            GenvexNabtoSetpointKey.TEMP_SETPOINT,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL4,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL4,
            GenvexNabtoSetpointKey.VENTILATION_ENABLE,
            GenvexNabtoSetpointKey.CTS400_HUMIDITY_LOW_LEVEL,
            GenvexNabtoSetpointKey.CTS400_HUMIDITY_LOW_STEP,
            GenvexNabtoSetpointKey.CTS400_HUMIDITY_HIGH_STEP,
            GenvexNabtoSetpointKey.CTS400_HUMIDITY_HIGH_MAX_TIME
        ]

    def getModelName(self):
        return "CTS 400"
    
    def getManufacturer(self):
        return "Nilan"