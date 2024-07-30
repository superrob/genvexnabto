from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoOptima314(GenvexNabtoBaseModel):
    def __init__(self):
        super().__init__()

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=20, divider=10, offset=-300),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=21, divider=10, offset=-300),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(obj=0, address=22, divider=10, offset=-300),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=64, divider=10, offset=-300),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=26, divider=1, offset=0),
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(obj=0, address=18, divider=100, offset=0),
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(obj=0, address=19, divider=100, offset=0),
            GenvexNabtoDatapointKey.RPM_SUPPLY: GenvexNabtoDatapoint(obj=0, address=35, divider=1, offset=0),
            GenvexNabtoDatapointKey.RPM_EXTRACT: GenvexNabtoDatapoint(obj=0, address=36, divider=1, offset=0),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=12, divider=1, offset=0)
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_obj=0, read_address=7, write_obj=0, write_address=24, divider=1, offset=0, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_obj=0, read_address=1, write_obj=0, write_address=12, divider=10, offset=100, min=0, max=200, step=0.5),
            GenvexNabtoSetpointKey.HOTWATER_TEMP: GenvexNabtoSetpoint(read_obj=0, read_address=122, write_obj=0, write_address=254, divider=10, offset=0, min=0, max=550, step=1),
            GenvexNabtoSetpointKey.REHEATING: GenvexNabtoSetpoint(read_obj=0, read_address=3, write_obj=0, write_address=16, divider=1, offset=0, min=0, max=1),
            GenvexNabtoSetpointKey.HUMIDITY_CONTROL: GenvexNabtoSetpoint(read_obj=0, read_address=6, write_obj=0, write_address=22, divider=1, offset=0, min=0, max=1),
            GenvexNabtoSetpointKey.BOOST_ENABLE: GenvexNabtoSetpoint(read_obj=0, read_address=30, write_obj=0, write_address=70, divider=1, offset=0, min=0, max=1),
            GenvexNabtoSetpointKey.BOOST_TIME: GenvexNabtoSetpoint(read_obj=0, read_address=70, write_obj=0, write_address=150, divider=1, offset=0, min=1, max=120, step=1),
            GenvexNabtoSetpointKey.FILTER_DAYS: GenvexNabtoSetpoint(read_obj=0, read_address=100, write_obj=0, write_address=210, divider=1, offset=0, min=0, max=65535),
            GenvexNabtoSetpointKey.FILTER_RESET: GenvexNabtoSetpoint(read_obj=0, read_address=50, write_obj=0, write_address=110, divider=1, offset=0, min=0, max=2),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1: GenvexNabtoSetpoint(read_obj=0, read_address=10, write_obj=0, write_address=30, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2: GenvexNabtoSetpoint(read_obj=0, read_address=11, write_obj=0, write_address=32, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3: GenvexNabtoSetpoint(read_obj=0, read_address=12, write_obj=0, write_address=34, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL4: GenvexNabtoSetpoint(read_obj=0, read_address=8, write_obj=0, write_address=26, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1: GenvexNabtoSetpoint(read_obj=0, read_address=13, write_obj=0, write_address=36, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2: GenvexNabtoSetpoint(read_obj=0, read_address=14, write_obj=0, write_address=38, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3: GenvexNabtoSetpoint(read_obj=0, read_address=15, write_obj=0, write_address=40, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL4: GenvexNabtoSetpoint(read_obj=0, read_address=9, write_obj=0, write_address=28, divider=1, offset=0, min=0, max=100, step=1)
        }

    def getModelName(self):
        return "Optima 314"
    
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
            GenvexNabtoDatapointKey.BYPASS_ACTIVE
        ]
    
    def getDefaultSetpointRequest(self) -> List[GenvexNabtoSetpointKey]:
        return [
            GenvexNabtoSetpointKey.FAN_SPEED,
            GenvexNabtoSetpointKey.TEMP_SETPOINT,
            GenvexNabtoSetpointKey.HOTWATER_TEMP,
            GenvexNabtoSetpointKey.REHEATING,
            GenvexNabtoSetpointKey.HUMIDITY_CONTROL,
            GenvexNabtoSetpointKey.FILTER_DAYS,
            GenvexNabtoSetpointKey.BOOST_ENABLE,
            GenvexNabtoSetpointKey.BOOST_TIME,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL4,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL4
        ]