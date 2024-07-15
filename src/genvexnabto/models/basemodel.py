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
    BYPASS_OPENOFFSET = "bypass_openoffset" # EE1
    REHEATING = "reheating" # A1
    HUMIDITY_CONTROL = "humidity_control" # A2
    FILTER_DAYS = "filter_days"
    FILTER_MONTHS = "filter_months"
    FILTER_HOURS = "filter_hours"

class GenvexNabtoDatapoint(TypedDict):
    obj: int
    address: int
    divider: int
    offset: int

class GenvexNabtoSetpoint(TypedDict):
    read_obj: int
    read_address: int
    write_obj: int
    write_address: int
    divider: int
    offset: int
    min: int
    max: int
    step: float



class GenvexNabtoBaseModel:
    _datapoints: Dict[GenvexNabtoDatapointKey, GenvexNabtoDatapoint] = {}
    _setpoints: Dict[GenvexNabtoSetpointKey, GenvexNabtoSetpoint] = {}

    def __init__(self):
        return
    
    def getModelName(self):
        return "Basemodel"

    def modelProvidesDatapoint(self, datapoint: GenvexNabtoDatapointKey) -> bool: 
        return datapoint in self._datapoints
    
    def getDefaultDatapointRequest(self) -> List[GenvexNabtoDatapointKey]:
        return {}
    
    def modelProvidesSetpoint(self, datapoint: GenvexNabtoSetpointKey) -> bool: 
        return datapoint in self._setpoints
    
    def getDefaultSetpointRequest(self) -> List[GenvexNabtoSetpointKey]:
        return {}