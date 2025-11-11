from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoOptima314(GenvexNabtoBaseModel):
    def __init__(self, slaveDeviceModel):
        super().__init__(slaveDeviceModel)

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=20, divider=10, offset=-300),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=21, divider=10, offset=-300),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(obj=0, address=22, divider=10, offset=-300),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=64, divider=10, offset=-300),
            GenvexNabtoDatapointKey.TEMP_FROSTPROTECTION: GenvexNabtoDatapoint(address=24, divider=10, offset=-300),
            GenvexNabtoDatapointKey.HPS_TEMP_BEFORE_CONDENSER: GenvexNabtoDatapoint(address=65, divider=10, offset=-300), #T5
            GenvexNabtoDatapointKey.TEMP_EVAPORATOR: GenvexNabtoDatapoint(address=66, divider=10, offset=-300), #T6
            GenvexNabtoDatapointKey.HOTWATER_TOP: GenvexNabtoDatapoint(address=23, divider=10, offset=-300), #T7
            GenvexNabtoDatapointKey.HOTWATER_BOTTOM: GenvexNabtoDatapoint(address=24, divider=10, offset=-300), #T8    
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=26),
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(obj=0, address=18, divider=100),
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(obj=0, address=19, divider=100),
            GenvexNabtoDatapointKey.RPM_SUPPLY: GenvexNabtoDatapoint(obj=0, address=35),
            GenvexNabtoDatapointKey.RPM_EXTRACT: GenvexNabtoDatapoint(obj=0, address=36),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=12)
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_address=7, write_address=24, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_address=1, write_address=12, divider=10, offset=100, min=0, max=200, step=0.5),
            GenvexNabtoSetpointKey.HOTWATER_TEMP: GenvexNabtoSetpoint(read_address=122, write_address=254, divider=10, min=0, max=550),
            GenvexNabtoSetpointKey.REHEATING: GenvexNabtoSetpoint(read_address=3, write_address=16, min=0, max=1),
            GenvexNabtoSetpointKey.HUMIDITY_CONTROL: GenvexNabtoSetpoint(read_address=6, write_address=22, min=0, max=1),
            GenvexNabtoSetpointKey.BOOST_ENABLE: GenvexNabtoSetpoint(read_address=30, write_address=70, min=0, max=1),
            GenvexNabtoSetpointKey.BOOST_TIME: GenvexNabtoSetpoint(read_address=70, write_address=150, min=1, max=120),
            GenvexNabtoSetpointKey.FILTER_DAYS: GenvexNabtoSetpoint(read_address=100, write_address=210, min=0, max=65535),
            GenvexNabtoSetpointKey.FILTER_RESET: GenvexNabtoSetpoint(read_address=50, write_address=110, min=0, max=2)
            # Setpoints not included, due to them being write locked in the gateway.
            #GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1: GenvexNabtoSetpoint(read_address=10, write_address=30, min=0, max=100),
            #GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2: GenvexNabtoSetpoint(read_address=11, write_address=32, min=0, max=100),
            #GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3: GenvexNabtoSetpoint(read_address=12, write_address=34, min=0, max=100),
            #GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL4: GenvexNabtoSetpoint(read_address=8, write_address=26, min=0, max=100),
            #GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1: GenvexNabtoSetpoint(read_address=13, write_address=36, min=0, max=100),
            #GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2: GenvexNabtoSetpoint(read_address=14, write_address=38, min=0, max=100),
            #GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3: GenvexNabtoSetpoint(read_address=15, write_address=40, min=0, max=100),
            #GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL4: GenvexNabtoSetpoint(read_address=9, write_address=28, min=0, max=100)
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
            GenvexNabtoDatapointKey.TEMP_FROSTPROTECTION,
            GenvexNabtoDatapointKey.HPS_TEMP_BEFORE_CONDENSER,
            GenvexNabtoDatapointKey.TEMP_EVAPORATOR,
            GenvexNabtoDatapointKey.HOTWATER_TOP,
            GenvexNabtoDatapointKey.HOTWATER_BOTTOM,
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
            GenvexNabtoSetpointKey.BOOST_TIME
        ]