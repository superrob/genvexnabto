from typing import Dict, List, TypedDict

class GenvexNabtoDatapointKey:
    TEMP_SUPPLY = "temp_supply"
    TEMP_OUTSIDE = "temp_outside"
    TEMP_EXHAUST = "temp_exhaust"
    TEMP_EXTRACT = "temp_extract"
    HUMIDITY = "humidity"
    DUTYCYCLE_SUPPLY = "dutycycle_supply"
    DUTYCYCLE_EXTRACT = "dutycycle_extract"
    BYPASS_ACTIVE = "bypass_active"

class GenvexNabtoSetpointKey:
    FAN_SPEED = "fan_speed"
    TEMP_SETPOINT = "temp_setpoint"
    FILTER_DAYS = "filter_days"

class GenvexNabtoDatapoint(TypedDict):
    obj: int = 0
    address: int
    divider: int = 1
    offset: int = 0

class GenvexNabtoSetpoint(TypedDict):
    read_obj: int = 0
    read_address: int
    write_obj: int = 0
    write_address: int
    divider: int = 1
    offset: int = 0
    min: int
    max: int


class GenvexNabtoBaseModel:
    _datapoints: Dict[GenvexNabtoDatapointKey, GenvexNabtoDatapoint] = {}
    _setpoints: Dict[GenvexNabtoSetpointKey, GenvexNabtoSetpoint] = {}

    def __init__(self):
        return
    
    def modelProvidesDatapoint(self, datapoint: GenvexNabtoDatapointKey) -> bool: 
        return datapoint in self._datapoint
    
    def getDefaultDatapointRequest(self) -> List[GenvexNabtoDatapointKey]:
        return {}
    
    def modelProvidesSetpoint(self, datapoint: GenvexNabtoSetpointKey) -> bool: 
        return datapoint in self._datapoint
    
    def getDefaultSetpointRequest(self) -> List[GenvexNabtoSetpointKey]:
        return {}