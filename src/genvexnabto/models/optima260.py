from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoOptima260(GenvexNabtoBaseModel):
    def __init__(self):
        super().__init__()

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=0, divider=10, offset=-300), #T1
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=2, divider=10, offset=-300), #T3
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(obj=0, address=3, divider=10, offset=-300), #T4
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=6, divider=10, offset=-300), #T7
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=13, divider=1, offset=0),
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(obj=0, address=9, divider=1, offset=0),
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(obj=0, address=10, divider=1, offset=0),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=11, divider=1, offset=0)
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_obj=0, read_address=0, write_obj=0, write_address=0, divider=1, offset=0, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_obj=0, read_address=2, write_obj=0, write_address=2, divider=10, offset=100, min=0, max=200, step=0.5),
            GenvexNabtoSetpointKey.BYPASS_OPENOFFSET: GenvexNabtoSetpoint(read_obj=0, read_address=18, write_obj=0, write_address=18, divider=10, offset=0, min=10, max=100, step=0.1),
            GenvexNabtoSetpointKey.HUMIDITY_CONTROL: GenvexNabtoSetpoint(read_obj=0, read_address=5, write_obj=0, write_address=5, divider=1, offset=0, min=0, max=1),
            GenvexNabtoSetpointKey.FILTER_MONTHS_SETTING: GenvexNabtoSetpoint(read_obj=0, read_address=5, write_obj=0, write_address=5, divider=1, offset=0, min=0, max=12, step=1),            
            GenvexNabtoSetpointKey.FILTER_RESET: GenvexNabtoSetpoint(read_obj=0, read_address=47, write_obj=0, write_address=47, divider=1, offset=0, min=0, max=1),          
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1: GenvexNabtoSetpoint(read_obj=0, read_address=7, write_obj=0, write_address=7, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2: GenvexNabtoSetpoint(read_obj=0, read_address=8, write_obj=0, write_address=8, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3: GenvexNabtoSetpoint(read_obj=0, read_address=9, write_obj=0, write_address=9, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1: GenvexNabtoSetpoint(read_obj=0, read_address=10, write_obj=0, write_address=10, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2: GenvexNabtoSetpoint(read_obj=0, read_address=11, write_obj=0, write_address=11, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3: GenvexNabtoSetpoint(read_obj=0, read_address=12, write_obj=0, write_address=12, divider=1, offset=0, min=0, max=100, step=1)
        }

    def getModelName(self):
        return "Optima 260"
    
    def getManufacturer(self):
        return "Genvex"

    def getDefaultDatapointRequest(self) -> List[GenvexNabtoDatapointKey]:
        return [
            GenvexNabtoDatapointKey.TEMP_SUPPLY,
            GenvexNabtoDatapointKey.TEMP_OUTSIDE,
            GenvexNabtoDatapointKey.TEMP_EXHAUST,
            GenvexNabtoDatapointKey.TEMP_EXTRACT,
            GenvexNabtoDatapointKey.HUMIDITY,
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY,
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT,
            GenvexNabtoDatapointKey.BYPASS_ACTIVE
        ]
    
    def getDefaultSetpointRequest(self) -> List[GenvexNabtoSetpointKey]:
        return [
            GenvexNabtoSetpointKey.FAN_SPEED,
            GenvexNabtoSetpointKey.TEMP_SETPOINT,
            GenvexNabtoSetpointKey.BYPASS_OPENOFFSET,
            GenvexNabtoSetpointKey.HUMIDITY_CONTROL,
            GenvexNabtoSetpointKey.FILTER_MONTHS_SETTING,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3
        ]