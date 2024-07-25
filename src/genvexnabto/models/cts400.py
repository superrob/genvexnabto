from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoCTS400(GenvexNabtoBaseModel):
    def __init__(self):
        super().__init__()

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=30, divider=10, offset=0),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=27, divider=10, offset=0),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(obj=0, address=29, divider=10, offset=0),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=28, divider=10, offset=0),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=31, divider=10, offset=0),
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(obj=0, address=25, divider=10, offset=0),
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(obj=0, address=24, divider=10, offset=0),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=23, divider=1, offset=0),
            GenvexNabtoDatapointKey.SUMMER_MODE: GenvexNabtoDatapoint(obj=0, address=72, divider=1, offset=0),
            GenvexNabtoDatapointKey.CO2_LEVEL: GenvexNabtoDatapoint(obj=0, address=47, divider=1, offset=0),
            GenvexNabtoDatapointKey.FILTER_DAYS_LEFT: GenvexNabtoDatapoint(obj=0, address=110, divider=1, offset=0),
            GenvexNabtoDatapointKey.DEFROST_ACTIVE: GenvexNabtoDatapoint(obj=0, address=91, divider=1, offset=0),
            GenvexNabtoDatapointKey.DEFORST_TIMESINCELAST: GenvexNabtoDatapoint(obj=0, address=89, divider=1, offset=0)               
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_obj=0, read_address=69, write_obj=0, write_address=69, divider=1, offset=0, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_obj=0, read_address=37, write_obj=0, write_address=37, divider=10, offset=0, min=0, max=300, step=0.5),
            GenvexNabtoSetpointKey.FILTER_RESET: GenvexNabtoSetpoint(read_obj=0, read_address=51, write_obj=0, write_address=51, divider=1, offset=0, min=0, max=1),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1: GenvexNabtoSetpoint(read_obj=0, read_address=59, write_obj=0, write_address=59, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2: GenvexNabtoSetpoint(read_obj=0, read_address=60, write_obj=0, write_address=60, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3: GenvexNabtoSetpoint(read_obj=0, read_address=61, write_obj=0, write_address=61, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL4: GenvexNabtoSetpoint(read_obj=0, read_address=62, write_obj=0, write_address=62, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1: GenvexNabtoSetpoint(read_obj=0, read_address=63, write_obj=0, write_address=63, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2: GenvexNabtoSetpoint(read_obj=0, read_address=64, write_obj=0, write_address=64, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3: GenvexNabtoSetpoint(read_obj=0, read_address=65, write_obj=0, write_address=65, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL4: GenvexNabtoSetpoint(read_obj=0, read_address=66, write_obj=0, write_address=66, divider=10, offset=0, min=200, max=1000, step=1)
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
            GenvexNabtoDatapointKey.DEFORST_TIMESINCELAST
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
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL4
        ]

    def getModelName(self):
        return "CTS 400"
    
    def getManufacturer(self):
        return "Nilan"