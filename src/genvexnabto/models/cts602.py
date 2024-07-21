from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoCTS602(GenvexNabtoBaseModel):
    def __init__(self):
        super().__init__()

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=38, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=39, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(obj=0, address=34, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=35, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_CONDENSER: GenvexNabtoDatapoint(obj=0, address=36, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_EVAPORATOR: GenvexNabtoDatapoint(obj=0, address=37, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_ROOM: GenvexNabtoDatapoint(obj=0, address=41, divider=100, offset=0),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=52, divider=100, offset=0),
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(obj=0, address=99, divider=1, offset=0),
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(obj=0, address=100, divider=1, offset=0),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=187, divider=1, offset=0),
            GenvexNabtoDatapointKey.SACRIFICIAL_ANODE: GenvexNabtoDatapoint(obj=0, address=142, divider=1, offset=0),
            GenvexNabtoDatapointKey.CO2_LEVEL: GenvexNabtoDatapoint(obj=0, address=53, divider=1, offset=0),
            GenvexNabtoDatapointKey.FILTER_DAYS_LEFT: GenvexNabtoSetpoint(read_obj=0, address=102, divider=1, offset=0)
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_obj=0, read_address=139, write_obj=0, write_address=139, divider=1, offset=0, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_obj=0, read_address=140, write_obj=0, write_address=140, divider=100, offset=0, min=0, max=3000),
            GenvexNabtoSetpointKey.FILTER_RESET: GenvexNabtoSetpoint(read_obj=0, read_address=71, write_obj=0, write_address=71, divider=1, offset=0, min=0, max=1),
            GenvexNabtoSetpointKey.HOTWATER_TEMP: GenvexNabtoSetpoint(read_obj=0, read_address=190, write_obj=0, write_address=190, divider=100, offset=0, min=2000, max=7000),
            GenvexNabtoSetpointKey.HOTWATER_BOOSTTEMP: GenvexNabtoSetpoint(read_obj=0, read_address=189, write_obj=0, write_address=189, divider=100, offset=0, min=2000, max=7000),
            GenvexNabtoSetpointKey.REHEATING: GenvexNabtoSetpoint(read_obj=0, read_address=281, write_obj=0, write_address=281, divider=1, offset=0, min=0, max=1)
        }

        self._defaultDatapointRequest = [
            GenvexNabtoDatapointKey.TEMP_SUPPLY,
            GenvexNabtoDatapointKey.TEMP_OUTSIDE,
            GenvexNabtoDatapointKey.TEMP_EXHAUST,
            GenvexNabtoDatapointKey.TEMP_EXTRACT,
            GenvexNabtoDatapointKey.TEMP_CONDENSER,
            GenvexNabtoDatapointKey.TEMP_EVAPORATOR,            
            GenvexNabtoDatapointKey.TEMP_ROOM,
            GenvexNabtoDatapointKey.HUMIDITY,
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY,
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT,
            GenvexNabtoDatapointKey.BYPASS_ACTIVE,
            GenvexNabtoDatapointKey.SACRIFICIAL_ANODE,
            GenvexNabtoDatapointKey.CO2_LEVEL,
            GenvexNabtoDatapointKey.FILTER_DAYS_LEFT
        ]

        self._defaultSetpointRequest = [
            GenvexNabtoSetpointKey.FAN_SPEED,
            GenvexNabtoSetpointKey.TEMP_SETPOINT,
            GenvexNabtoSetpointKey.HOTWATER_TEMP,
            GenvexNabtoSetpointKey.HOTWATER_BOOSTTEMP,
            GenvexNabtoSetpointKey.REHEATING
        ]

        self._quirks = {
            "hotwaterTempSensor": [
                9, 10, 11,  12,  18, 19,
                20, 21, 23,  30,  32, 34,
                38, 43, 44, 144, 244
            ]
        }
        
    
    def addDeviceQuirks(self, deviceNumber, slaveDeviceNumber, slaveDeviceModel):
        # Add quirks unique to the connected device
        if self.deviceHasQuirk("hotwaterTempSensor", slaveDeviceModel):
            self._datapoints[GenvexNabtoDatapointKey.HOTWATER_TOP] = GenvexNabtoDatapoint(obj=0, address=42, divider=100, offset=0)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HOTWATER_TOP)
            self._datapoints[GenvexNabtoDatapointKey.HOTWATER_BOTTOM] = GenvexNabtoDatapoint(obj=0, address=43, divider=100, offset=0)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HOTWATER_BOTTOM)        
        return

    def getModelName(self):
        return "CTS 602"
    
    def getManufacturer(self):
        return "Nilan"
    