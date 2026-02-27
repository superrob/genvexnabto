from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoOptima250(GenvexNabtoBaseModel):
    def __init__(self, slaveDeviceModel):
        super().__init__(slaveDeviceModel)

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=0, divider=10, offset=-300), #T1
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=2, divider=10, offset=-300), #T3
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(obj=0, address=3, divider=10, offset=-300), #T4
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=6, divider=10, offset=-300), #T7
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=10),
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(obj=0, address=102),
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(obj=0, address=103),
            GenvexNabtoDatapointKey.RPM_SUPPLY: GenvexNabtoDatapoint(obj=0, address=108),
            GenvexNabtoDatapointKey.RPM_EXTRACT: GenvexNabtoDatapoint(obj=0, address=109),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=104),
            GenvexNabtoDatapointKey.ALARM_OPTIMA25X: GenvexNabtoDatapoint(obj=0, address=101)
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_address=100, write_address=100, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_address=0, write_address=0, divider=10, offset=100, min=0, max=200, step=0.5),
            GenvexNabtoSetpointKey.BYPASS_OPENOFFSET: GenvexNabtoSetpoint(read_address=17, write_address=17, divider=10, min=10, max=100, step=0.1),
            GenvexNabtoSetpointKey.REHEATING: GenvexNabtoSetpoint(read_address=2, write_address=2, min=0, max=1),
            GenvexNabtoSetpointKey.HUMIDITY_CONTROL: GenvexNabtoSetpoint(read_address=5, write_address=5, min=0, max=1),
            GenvexNabtoSetpointKey.FILTER_MONTHS_SETTING: GenvexNabtoSetpoint(read_address=4, write_address=4, min=0, max=6),            
            GenvexNabtoSetpointKey.FILTER_RESET: GenvexNabtoSetpoint(read_address=105, write_address=105, min=0, max=1),          
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1: GenvexNabtoSetpoint(read_address=6, write_address=6, min=0, max=100),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2: GenvexNabtoSetpoint(read_address=7, write_address=7, min=0, max=100),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3: GenvexNabtoSetpoint(read_address=8, write_address=8, min=0, max=100),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1: GenvexNabtoSetpoint(read_address=9, write_address=9, min=0, max=100),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2: GenvexNabtoSetpoint(read_address=10, write_address=10, min=0, max=100),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3: GenvexNabtoSetpoint(read_address=11, write_address=11, min=0, max=100)
        }

    def getModelName(self):
        return "Optima 250"
        
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
            GenvexNabtoDatapointKey.RPM_SUPPLY,            
            GenvexNabtoDatapointKey.RPM_EXTRACT,
            GenvexNabtoDatapointKey.BYPASS_ACTIVE,
            GenvexNabtoDatapointKey.ALARM_OPTIMA25X
        ]
    
    def getDefaultSetpointRequest(self) -> List[GenvexNabtoSetpointKey]:
        return [
            GenvexNabtoSetpointKey.FAN_SPEED,
            GenvexNabtoSetpointKey.TEMP_SETPOINT,
            GenvexNabtoSetpointKey.BYPASS_OPENOFFSET,
            GenvexNabtoSetpointKey.REHEATING,
            GenvexNabtoSetpointKey.HUMIDITY_CONTROL,
            GenvexNabtoSetpointKey.FILTER_MONTHS_SETTING,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3
        ]