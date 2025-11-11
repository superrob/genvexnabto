from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoOptima312(GenvexNabtoBaseModel):
    def __init__(self, slaveDeviceModel):
        super().__init__(slaveDeviceModel)

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(address=0, divider=10, offset=-300), #T1
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(address=2, divider=10, offset=-300), #T3
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(address=3, divider=10, offset=-300), #T4
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(address=1, divider=10, offset=-300), #T2?
            GenvexNabtoDatapointKey.HPS_TEMP_BEFORE_CONDENSER: GenvexNabtoDatapoint(address=4, divider=10, offset=-300), #T5
            GenvexNabtoDatapointKey.TEMP_EVAPORATOR: GenvexNabtoDatapoint(address=5, divider=10, offset=-300), #T6
            GenvexNabtoDatapointKey.HOTWATER_TOP: GenvexNabtoDatapoint(address=6, divider=10, offset=-300), #T7
            GenvexNabtoDatapointKey.HOTWATER_BOTTOM: GenvexNabtoDatapoint(address=7, divider=10, offset=-300), #T8            
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(address=10),
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(address=102),
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(address=103),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(address=104)
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_address=100, write_address=100, min=0, max=4),
            GenvexNabtoSetpointKey.HOTWATER_TEMP: GenvexNabtoSetpoint(read_address=1, write_address=1, divider=10, min=0, max=550),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_address=0, write_address=0, divider=10, offset=100, min=0, max=200, step=0.5),         
            GenvexNabtoSetpointKey.REHEATING: GenvexNabtoSetpoint(read_address=21, write_address=21, min=0, max=1),
            GenvexNabtoSetpointKey.FILTER_RESET: GenvexNabtoSetpoint(read_address=105, write_address=105, min=0, max=1),          
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1: GenvexNabtoSetpoint(read_address=6, write_address=6, min=0, max=100),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2: GenvexNabtoSetpoint(read_address=7, write_address=7, min=0, max=100),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3: GenvexNabtoSetpoint(read_address=8, write_address=8, min=0, max=100),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1: GenvexNabtoSetpoint(read_address=9, write_address=9, min=0, max=100),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2: GenvexNabtoSetpoint(read_address=10, write_address=10, min=0, max=100),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3: GenvexNabtoSetpoint(read_address=11, write_address=11, min=0, max=100)
        }

    def getModelName(self):
        return "Optima 312"
    
    def getManufacturer(self):
        return "Genvex"

    def getDefaultDatapointRequest(self) -> List[GenvexNabtoDatapointKey]:
        return [
            GenvexNabtoDatapointKey.TEMP_SUPPLY,
            GenvexNabtoDatapointKey.TEMP_OUTSIDE,
            GenvexNabtoDatapointKey.TEMP_EXHAUST,
            GenvexNabtoDatapointKey.TEMP_EXTRACT,
            GenvexNabtoDatapointKey.HPS_TEMP_BEFORE_CONDENSER,
            GenvexNabtoDatapointKey.TEMP_EVAPORATOR,
            GenvexNabtoDatapointKey.HOTWATER_TOP,
            GenvexNabtoDatapointKey.HOTWATER_BOTTOM,
            GenvexNabtoDatapointKey.HUMIDITY,
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY,
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT,
            GenvexNabtoDatapointKey.BYPASS_ACTIVE
        ]
    
    def getDefaultSetpointRequest(self) -> List[GenvexNabtoSetpointKey]:
        return [
            GenvexNabtoSetpointKey.FAN_SPEED,
            GenvexNabtoSetpointKey.HOTWATER_TEMP,
            GenvexNabtoSetpointKey.TEMP_SETPOINT,
            GenvexNabtoSetpointKey.REHEATING,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3
        ]