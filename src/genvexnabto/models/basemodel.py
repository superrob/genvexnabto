from typing import Dict, List, TypedDict, NotRequired

class GenvexNabtoDatapointKey:
    # Temperature of the air to supplied to the house
    TEMP_SUPPLY = "temp_supply"
    # Temperature of the air passing through the heater
    TEMP_SUPPLY_AFTER_HEATER = "temp_supply_after_heater"
    # Temperature of the air outside the house, being pulled into the system
    TEMP_OUTSIDE = "temp_outside"
    # Temperature of the air being exhausted from the system to the outside
    TEMP_EXHAUST = "temp_exhaust"
    # Temperature of the air being extracted from the house into the system
    TEMP_EXTRACT = "temp_extract"
    # Temperature of the condenser in the heatpump
    TEMP_CONDENSER = "temp_condenser"
    # Temperature of the evaporator in the heatpump
    TEMP_EVAPORATOR = "temp_evaporator"
    # Temperature of the room sensor
    TEMP_ROOM = "temp_room"
    # Temperature of the heater
    TEMP_HEATER = "temp_heater"
    # Frostprotection temperature 
    TEMP_FROSTPROTECTION = "temp_frostprotection"
    HUMIDITY = "humidity"
    # The current fan level from 0 to 4
    FAN_LEVEL_SUPPLY = "fan_level_supply"
    FAN_LEVEL_EXTRACT = "fan_level_extract"
    # The current dutycycle of the supply and extract fans from 0 to 100
    DUTYCYCLE_SUPPLY = "fan_speed_supply"
    DUTYCYCLE_EXTRACT = "fan_speed_extract"
    # The current RPM of the supply and extract fans from 0 to their max RPM
    RPM_SUPPLY = "fan_rpm_supply"
    RPM_EXTRACT = "fan_rpm_extract"
    # The current m3/h of the supply and extract fans from 0 to their max m3/h
    M3H_SUPPLY = "fan_m3h_supply"
    M3H_EXTRACT = "fan_m3h_extract"
    # The current PWM of the heating elements from 0 to 100
    PREHEAT_PWM = "preheat_pwm"
    REHEAT_PWM = "reheat_pwm"
    # The current RPM of the rotor from 0 to its max RPM
    ROTOR_SPEED = "rotor_speed"
    # Indicates if the bypass currently is active (Opened)
    BYPASS_ACTIVE = "bypass_active"
    # The analog value of the bypass
    BYPASS_ANALOG = "bypass_analog"
    # The temperature of the hot water in the tank in the top
    HOTWATER_TOP = "hotwater_top"
    # The temperature of the hot water in the tank in the bottom
    HOTWATER_BOTTOM = "hotwater_bottom"
    # Indicates if the summer mode is active
    SUMMER_MODE = "summer_mode"
    # Indicates if the sacrificial anode has a problem. 0 = OK, 1 = Problem
    SACRIFICIAL_ANODE = "sacrificial_anode"
    # The current CO2 level in the house
    CO2_LEVEL = "co2_level"
    # The current days left before planned filter change
    FILTER_DAYS_LEFT = "filter_days_left"
    # Indicates if the defrost is currently active
    DEFROST_ACTIVE = "defrost_active"
    # The time since the last defrost
    DEFORST_TIMESINCELAST = "defrost_timesincelast"
    CONTROLSTATE_602 = "controlstate_602"
    ALARM_OPTIMA270 = "alarm_optima270"
    ALARM_CTS602NO1 = "alarm_cts602no1"
    ALARM_CTS602NO2 = "alarm_cts602no2"
    ALARM_CTS602NO3 = "alarm_cts602no3"
    ALARM_CTS400CRITICAL = "alarm_cts400critical"
    ALARM_CTS400WARNING = "alarn_cts400warning"
    ALARM_CTS400INFO = "alarm_cts400info"

    # CTS 602 Compact P
    HPS_CAPACITY_ACTUAL = "hps_capacity_actual"
    HPS_OPERATION_STATE = "hps_operation_state"
    HPS_HEATPUMP_ACTIVE = "hps_heatpump_active"
    HPS_HEATER_ACTIVE = "hps_heater_active"
    HPS_TEMP_AFTER_CONDENSER = "hps_temp_after_condenser" # Heatpump equiped T17
    HPS_TEMP_BEFORE_CONDENSER = "hps_temp_before_condenser" # Heatpump equiped T16
    HPS_TEMP_BUFFERTANK = "hps_temp_buffertank" # Heatpump equiped T18
    HPS_TEMP_HEATPUMP_OUTDOOR = "hps_temp_heatpump_outdoor" # Heatpump equiped T20
    HPS_TEMP_PRESSURE_PIPE = "hps_temp_pressure_pipe" # Heatpump equiped T19

    CENTRALHEAT_TEMP_SUPPLY = "centralheat_temp_supply"
    CENTRALHEAT_TEMP_RETURN = "centralheat_temp_return"


class GenvexNabtoSetpointKey:
    FAN_SPEED = "fan_speed"
    TEMP_SETPOINT = "temp_setpoint"
    BYPASS_OPENOFFSET = "bypass_openoffset" # EE1
    REHEATING = "reheating" # A1
    PREHEATING = "preheating" # A1
    HUMIDITY_CONTROL = "humidity_control" # A2
    BOOST_ENABLE = "boost_enable"
    BOOST_TIME = "boost_time" # A3
    FILTER_DAYS = "filter_days"
    FILTER_HOURS = "filter_hours"
    FILTER_RESET = "filter_reset"
    FILTER_MONTHS_SETTING = "filter_months_setting"
    FILTER_DAYS_SETTING = "filter_days_setting"
    SUPPLY_AIR_LEVEL1 = "supply_air_level1"
    SUPPLY_AIR_LEVEL2 = "supply_air_level2"
    SUPPLY_AIR_LEVEL3 = "supply_air_level3"
    SUPPLY_AIR_LEVEL4 = "supply_air_level4"
    EXTRACT_AIR_LEVEL1 = "extract_air_level1"
    EXTRACT_AIR_LEVEL2 = "extract_air_level2"
    EXTRACT_AIR_LEVEL3 = "extract_air_level3"
    EXTRACT_AIR_LEVEL4 = "extract_air_level4"
    HOTWATER_TEMP = "hotwater_temp"
    HOTWATER_BOOSTTEMP = "hotwater_boosttemp"
    ANTILEGIONELLA_DAY = "antilegionella_day"
    SUPPLYAIR_MIN_TEMP_SUMMER = "supplyair_min_temp_summer"
    SUPPLYAIR_MAX_TEMP_SUMMER = "supplyair_max_temp_summer"
    COOLING_PRIORITY = "cooling_priority"
    COOLING_ENABLE = "cooling_enable"
    COOLING_TEMPERATURE = "cooling_temperature"
    COOLING_OFFSET = "cooling_offset"
    VENTILATION_ENABLE = "ventilation_enable"
    CENTRALHEAT_SUPPLY_MIN = "centralheat_supply_min"
    CENTRALHEAT_SUPPLY_MAX = "centralheat_supply_max"
    CENTRALHEAT_PUMP_MODE = "centralheat_pump_mode"
    CENTRALHEAT_TYPE = "centralheat_type"
    CENTRALHEAT_SELECT = "centralheat_select"
    CTS602_CONTROL_MODE_SET = "cts602_control_mode_set"


class GenvexNabtoDatapoint(TypedDict):
    obj: NotRequired[int] # Default 0
    address: int
    divider: NotRequired[int] # Default 1
    offset: NotRequired[int] # Default 0

class GenvexNabtoSetpoint(TypedDict):
    read_obj: NotRequired[int] # Default 0
    read_address: int
    write_obj: NotRequired[int] # Default 0
    write_address: int
    divider: NotRequired[int] # Default 1
    offset: NotRequired[int] # Default 0
    min: int
    max: int
    step: NotRequired[float] # Default 1.0

class GenvexNabtoBaseModel:    

    def __init__(self, slaveDeviceModel):
        self._datapoints: Dict[GenvexNabtoDatapointKey, GenvexNabtoDatapoint] = {}
        self._setpoints: Dict[GenvexNabtoSetpointKey, GenvexNabtoSetpoint] = {}
        self._quirks: Dict[str, list[int]] = {}

        self._defaultDatapointRequest: List[GenvexNabtoDatapointKey] = []
        self._defaultSetpointRequest: List[GenvexNabtoDatapointKey] = []
        self._slaveDeviceModel = slaveDeviceModel
        return
    
    def getModelName(self):
        return "Basemodel"
    
    def getManufacturer(self):
        return ""

    def modelProvidesDatapoint(self, datapoint: GenvexNabtoDatapointKey) -> bool: 
        return datapoint in self._datapoints
    
    def getDefaultDatapointRequest(self) -> List[GenvexNabtoDatapointKey]:
        return self._defaultDatapointRequest
    
    def modelProvidesSetpoint(self, datapoint: GenvexNabtoSetpointKey) -> bool: 
        return datapoint in self._setpoints
    
    def getDefaultSetpointRequest(self) -> List[GenvexNabtoSetpointKey]:
        return self._defaultSetpointRequest
    
    def deviceHasQuirk(self, quirk, device) -> bool:
        if quirk not in self._quirks:
            return False
        return device in self._quirks[quirk]

    def addDeviceQuirks(self):
        return
    
    # This method is called by the subclass to add default values to the data and setpoint dictionaries
    def finishLoading(self):
        for datapoint in self._datapoints.values():
            if "obj" not in datapoint:
                datapoint["obj"] = 0
            if "divider" not in datapoint:
                datapoint["divider"] = 1
            if "offset" not in datapoint:
                datapoint["offset"] = 0
        for setpoint in self._setpoints.values():
            if "read_obj" not in setpoint:
                setpoint["read_obj"] = 0
            if "write_obj" not in setpoint:
                setpoint["write_obj"] = 0
            if "divider" not in setpoint:
                setpoint["divider"] = 1
            if "offset" not in setpoint:
                setpoint["offset"] = 0
            if "step" not in setpoint:
                setpoint["step"] = 1.0
        
