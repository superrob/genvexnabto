from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoOptima270(GenvexNabtoBaseModel):
    def __init__(self, slaveDeviceModel):
        super().__init__(slaveDeviceModel)

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(address=20, divider=10, offset=-300),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(address=21, divider=10, offset=-300),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(address=22, divider=10, offset=-300),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(address=23, divider=10, offset=-300),
            GenvexNabtoDatapointKey.TEMP_FROSTPROTECTION: GenvexNabtoDatapoint(address=24, divider=10, offset=-300),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(address=26),
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(address=18, divider=100),
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(address=19, divider=100),
            GenvexNabtoDatapointKey.RPM_SUPPLY: GenvexNabtoDatapoint(address=35),
            GenvexNabtoDatapointKey.RPM_EXTRACT: GenvexNabtoDatapoint(address=36),
            GenvexNabtoDatapointKey.PREHEAT_PWM: GenvexNabtoDatapoint(address=41, divider=100),
            GenvexNabtoDatapointKey.REHEAT_PWM: GenvexNabtoDatapoint(address=42, divider=100),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(address=53),
            GenvexNabtoDatapointKey.BYPASS_ANALOG: GenvexNabtoDatapoint(address=40),
            GenvexNabtoDatapointKey.ALARM_OPTIMA270: GenvexNabtoDatapoint(address=38),
            GenvexNabtoDatapointKey.ROTOR_SPEED: GenvexNabtoDatapoint(address=50)             
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_address=7, write_address=24, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_address=1, write_address=12, divider=10, offset=100, min=0, max=200, step=0.5),
            GenvexNabtoSetpointKey.BYPASS_OPENOFFSET: GenvexNabtoSetpoint(read_address=21, write_address=52, divider=10, min=10, max=100, step=0.1),
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
        return "Optima 270"
    
    def getManufacturer(self):
        return "Genvex"

    def getDefaultDatapointRequest(self) -> List[GenvexNabtoDatapointKey]:
        return [
            GenvexNabtoDatapointKey.TEMP_SUPPLY,
            GenvexNabtoDatapointKey.TEMP_OUTSIDE,
            GenvexNabtoDatapointKey.TEMP_EXHAUST,
            GenvexNabtoDatapointKey.TEMP_EXTRACT,
            GenvexNabtoDatapointKey.TEMP_FROSTPROTECTION,
            GenvexNabtoDatapointKey.HUMIDITY,
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY,
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT,
            GenvexNabtoDatapointKey.RPM_SUPPLY,            
            GenvexNabtoDatapointKey.RPM_EXTRACT,
            GenvexNabtoDatapointKey.PREHEAT_PWM,
            GenvexNabtoDatapointKey.REHEAT_PWM,
            GenvexNabtoDatapointKey.BYPASS_ACTIVE,
            GenvexNabtoDatapointKey.BYPASS_ANALOG,
            GenvexNabtoDatapointKey.ALARM_OPTIMA270,
            GenvexNabtoDatapointKey.ROTOR_SPEED
        ]
    
    def getDefaultSetpointRequest(self) -> List[GenvexNabtoSetpointKey]:
        return [
            GenvexNabtoSetpointKey.FAN_SPEED,
            GenvexNabtoSetpointKey.TEMP_SETPOINT,
            GenvexNabtoSetpointKey.BYPASS_OPENOFFSET,
            GenvexNabtoSetpointKey.REHEATING,
            GenvexNabtoSetpointKey.HUMIDITY_CONTROL,
            GenvexNabtoSetpointKey.BOOST_ENABLE,
            GenvexNabtoSetpointKey.BOOST_TIME,
            GenvexNabtoSetpointKey.FILTER_DAYS
        ]