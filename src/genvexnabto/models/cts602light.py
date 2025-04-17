from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoCTS602Light(GenvexNabtoBaseModel):
    def __init__(self, slaveDeviceModel):
        super().__init__(slaveDeviceModel)

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(address=37, divider=100),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(address=38, divider=100),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(address=34, divider=100),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(address=33, divider=100),
            GenvexNabtoDatapointKey.TEMP_HEATER: GenvexNabtoDatapoint(address=39, divider=100),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(address=51, divider=100),
            GenvexNabtoDatapointKey.FAN_LEVEL_SUPPLY: GenvexNabtoDatapoint(address=98),
            GenvexNabtoDatapointKey.FAN_LEVEL_EXTRACT: GenvexNabtoDatapoint(address=99),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(address=129),
            GenvexNabtoDatapointKey.CO2_LEVEL: GenvexNabtoDatapoint(address=53),
            GenvexNabtoDatapointKey.FILTER_DAYS_LEFT: GenvexNabtoDatapoint(address=101),
            GenvexNabtoDatapointKey.CONTROLSTATE_602: GenvexNabtoDatapoint(address=85),
            GenvexNabtoDatapointKey.ALARM_CTS602NO1: GenvexNabtoDatapoint(address=64),
            GenvexNabtoDatapointKey.ALARM_CTS602NO2: GenvexNabtoDatapoint(address=67),
            GenvexNabtoDatapointKey.ALARM_CTS602NO3: GenvexNabtoDatapoint(address=70)
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_address=135, write_address=135, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_address=136, write_address=136, divider=100, min=0, max=3000, step=0.5),
            GenvexNabtoSetpointKey.FILTER_RESET: GenvexNabtoSetpoint(read_address=67, write_address=67, min=0, max=1),            
            GenvexNabtoSetpointKey.FILTER_DAYS_SETTING: GenvexNabtoSetpoint(read_address=153, write_address=153, min=0, max=365)
        }

        self._defaultDatapointRequest = [
            GenvexNabtoDatapointKey.TEMP_SUPPLY,
            GenvexNabtoDatapointKey.TEMP_OUTSIDE,
            GenvexNabtoDatapointKey.TEMP_EXHAUST,
            GenvexNabtoDatapointKey.TEMP_EXTRACT,
            GenvexNabtoDatapointKey.TEMP_HEATER,
            GenvexNabtoDatapointKey.HUMIDITY,
            GenvexNabtoDatapointKey.FAN_LEVEL_SUPPLY,
            GenvexNabtoDatapointKey.FAN_LEVEL_EXTRACT,
            GenvexNabtoDatapointKey.BYPASS_ACTIVE,
            GenvexNabtoDatapointKey.CO2_LEVEL,
            GenvexNabtoDatapointKey.FILTER_DAYS_LEFT,
            GenvexNabtoDatapointKey.CONTROLSTATE_602,
            GenvexNabtoDatapointKey.ALARM_CTS602NO1,
            GenvexNabtoDatapointKey.ALARM_CTS602NO2,
            GenvexNabtoDatapointKey.ALARM_CTS602NO3
        ]

        self._defaultSetpointRequest = [
            GenvexNabtoSetpointKey.FAN_SPEED,
            GenvexNabtoSetpointKey.TEMP_SETPOINT,
            GenvexNabtoSetpointKey.FILTER_DAYS_SETTING
        ]

    def getModelName(self):
        return "CTS 602light"
    
    def getManufacturer(self):
        return "Nilan"