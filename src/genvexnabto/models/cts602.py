from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoCTS602(GenvexNabtoBaseModel):

    _modelNames = {2: "Comfort_LIGHT",        
        3: "VPL15",
        4: "VPL15c",
        9: "CompacSU",
        10: "CompactS",
        11: "VP18compact",
        12: "VP18cCompact",
        13: "Comfort",
        18: "VP18",
        19: "VP18c",
        20: "VP18ek",
        21: "VP18cek",
        23: "VGU250ek",
        26: "VPM_28EC",
        27: "COMFORT_I",
        30: "COMPACT_N",
        31: "COMFORT_N",
        32: "VP18M1",
        33: "COMBI300",
        34: "COMPACTu",
        35: "COMBI302",
        36: "COMB302T",
        38: "VGU180ek",
        39: "VPM_1",
        40: "VPM_2",
        41: "VPM_3",
        43: "CompactPEK",
        44: "Compact P",
        45: "VPR",
        144: "Compact P AIR",
        244: "Compact P GEO"}

    def __init__(self, slaveDeviceModel):
        super().__init__(slaveDeviceModel)

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(address=33, divider=100),
            GenvexNabtoDatapointKey.TEMP_SUPPLY_AFTER_HEATER: GenvexNabtoDatapoint(address=38, divider=100),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(address=39, divider=100),            
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(address=35, divider=100),
            GenvexNabtoDatapointKey.TEMP_CONDENSER: GenvexNabtoDatapoint(address=36, divider=100),
            GenvexNabtoDatapointKey.TEMP_EVAPORATOR: GenvexNabtoDatapoint(address=37, divider=100),
            GenvexNabtoDatapointKey.TEMP_ROOM: GenvexNabtoDatapoint(address=41, divider=100),
            GenvexNabtoDatapointKey.TEMP_HEATER: GenvexNabtoDatapoint(address=40, divider=100),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(address=52, divider=100),
            GenvexNabtoDatapointKey.FAN_LEVEL_SUPPLY: GenvexNabtoDatapoint(address=99),
            GenvexNabtoDatapointKey.FAN_LEVEL_EXTRACT: GenvexNabtoDatapoint(address=100),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(address=187),
            GenvexNabtoDatapointKey.CO2_LEVEL: GenvexNabtoDatapoint(address=53),
            GenvexNabtoDatapointKey.FILTER_DAYS_LEFT: GenvexNabtoDatapoint(address=102),
            GenvexNabtoDatapointKey.CONTROLSTATE_602: GenvexNabtoDatapoint(address=86),
            GenvexNabtoDatapointKey.ALARM_CTS602NO1: GenvexNabtoDatapoint(address=65),
            GenvexNabtoDatapointKey.ALARM_CTS602NO2: GenvexNabtoDatapoint(address=68),
            GenvexNabtoDatapointKey.ALARM_CTS602NO3: GenvexNabtoDatapoint(address=71)
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_address=139, write_address=139, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_address=140, write_address=140, divider=100, min=0, max=3000, step=0.5),
            GenvexNabtoSetpointKey.FILTER_RESET: GenvexNabtoSetpoint(read_address=71, write_address=71, min=0, max=1),
            GenvexNabtoSetpointKey.FILTER_DAYS_SETTING: GenvexNabtoSetpoint(read_address=159, write_address=159, min=0, max=365)
        }

        self._defaultDatapointRequest = [
            GenvexNabtoDatapointKey.TEMP_SUPPLY,
            GenvexNabtoDatapointKey.TEMP_SUPPLY_AFTER_HEATER,
            GenvexNabtoDatapointKey.TEMP_OUTSIDE,
            GenvexNabtoDatapointKey.TEMP_EXHAUST,
            GenvexNabtoDatapointKey.TEMP_CONDENSER,
            GenvexNabtoDatapointKey.TEMP_EVAPORATOR,            
            GenvexNabtoDatapointKey.TEMP_ROOM,
            GenvexNabtoDatapointKey.TEMP_HEATER,
            GenvexNabtoDatapointKey.HUMIDITY,
            GenvexNabtoDatapointKey.FAN_LEVEL_SUPPLY,
            GenvexNabtoDatapointKey.FAN_LEVEL_EXTRACT,
            GenvexNabtoDatapointKey.BYPASS_ACTIVE,
            GenvexNabtoDatapointKey.CO2_LEVEL,
            GenvexNabtoDatapointKey.FILTER_DAYS_LEFT,
            GenvexNabtoDatapointKey.CONTROLSTATE_602,
            GenvexNabtoDatapointKey.ALARM_CTS602NO1,
            GenvexNabtoDatapointKey.ALARM_CTS602NO2,
            GenvexNabtoDatapointKey.ALARM_CTS602NO3
        ]

        self._defaultSetpointRequest = [
            GenvexNabtoSetpointKey.FAN_SPEED,
            GenvexNabtoSetpointKey.TEMP_SETPOINT,
            GenvexNabtoSetpointKey.FILTER_DAYS_SETTING,
        ]

        self._quirks = {
            "hotwaterTempSensor": [
                9, 10, 11,  12,  18, 19,
                20, 21, 23,  30,  32, 34,
                38, 43, 44, 144, 244
            ],
            "sacrificialAnode": [
                9, 10,  11,  12, 18, 19,
                20, 21,  23,  30, 34, 38,
                43, 44, 144, 244
            ],
            "reheating": [
                2,   3,   4,  9, 10, 11, 12, 13, 18,
                19,  20,  21, 23, 26, 27, 30, 31, 33,
                34,  35,  36, 38, 39, 40, 41, 43, 44,
                45, 144, 244
            ],
            "extractTempSensor": [ 2, 13, 27, 31 ],
            "antiLegionella": [
                3,  4,  9, 10,  11,  12, 18,
                19, 20, 21, 23,  30,  32, 34,
                38, 43, 44, 45, 144, 244
            ],
            "hotwaterTempSet": [
                9, 10, 11,  12,  13, 18, 19,
                20, 21, 23,  30,  31, 32, 34,
                38, 43, 44, 144, 244
            ],
            "summerTemperatures": [
                2,  4,  9, 10, 12, 13, 19,  21,
                26, 30, 31, 32, 33, 34, 35,  36,
                38, 39, 40, 41, 43, 44, 45, 144,
                244
            ],
            "coolingPriority": [
                2,  9, 10, 12, 13,  30,
                31, 32, 38, 43, 44, 144,
                244
            ],
            "coolingOffset": [
                4,  9, 10, 12, 19,  21,  26,
                30, 32, 33, 35, 36,  38,  39,
                40, 41, 43, 44, 45, 144, 244
            ],
            "heatpumpData": [ 44, 144, 244 ],
            "centralHeat": [ 20, 21, 23, 38, 43, 45 ],
            "disableCoolingMode": [ 23 ]
        }
        
    
    def addDeviceQuirks(self):
        # Add quirks unique to the connected device

        # Some models do not have cooling. Don't use the control mode for that model.
        if not self.deviceHasQuirk("disableCoolingMode", self._slaveDeviceModel):  
            self._setpoints[GenvexNabtoSetpointKey.CTS602_CONTROL_MODE_SET] = GenvexNabtoSetpoint(read_address=138, write_address=138, min=0, max=4)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.CTS602_CONTROL_MODE_SET)
        
        if self.deviceHasQuirk("hotwaterTempSensor", self._slaveDeviceModel):
            self._datapoints[GenvexNabtoDatapointKey.HOTWATER_TOP] = GenvexNabtoDatapoint(address=42, divider=100)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HOTWATER_TOP)
            self._datapoints[GenvexNabtoDatapointKey.HOTWATER_BOTTOM] = GenvexNabtoDatapoint(address=43, divider=100)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HOTWATER_BOTTOM)   

        if self.deviceHasQuirk("sacrificialAnode", self._slaveDeviceModel):  
            self._datapoints[GenvexNabtoDatapointKey.SACRIFICIAL_ANODE] = GenvexNabtoDatapoint(address=142)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.SACRIFICIAL_ANODE)
            
        if self.deviceHasQuirk("reheating", self._slaveDeviceModel):  
            self._setpoints[GenvexNabtoSetpointKey.REHEATING] = GenvexNabtoSetpoint(read_address=281, write_address=281, min=0, max=1)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.REHEATING)

        if self.deviceHasQuirk("extractTempSensor", self._slaveDeviceModel):  
            self._datapoints[GenvexNabtoDatapointKey.TEMP_EXTRACT] = GenvexNabtoDatapoint(address=34, divider=100)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.TEMP_EXTRACT)
        else:
            self._datapoints[GenvexNabtoDatapointKey.TEMP_EXTRACT] = GenvexNabtoDatapoint(address=41, divider=100)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.TEMP_EXTRACT)

        if self.deviceHasQuirk("antiLegionella", self._slaveDeviceModel):  
            self._setpoints[GenvexNabtoSetpointKey.ANTILEGIONELLA_DAY] = GenvexNabtoSetpoint(read_address=194, write_address=194, min=7, max=1)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.ANTILEGIONELLA_DAY)

        if self.deviceHasQuirk("hotwaterTempSet", self._slaveDeviceModel):  
            self._setpoints[GenvexNabtoSetpointKey.HOTWATER_TEMP] = GenvexNabtoSetpoint(read_address=190, write_address=190, divider=100, min=2000, max=7000)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.HOTWATER_TEMP)
            self._setpoints[GenvexNabtoSetpointKey.HOTWATER_BOOSTTEMP] = GenvexNabtoSetpoint(read_address=189, write_address=189, divider=100, min=2000, max=7000)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.HOTWATER_BOOSTTEMP)

        if self.deviceHasQuirk("summerTemperatures", self._slaveDeviceModel):
            self._setpoints[GenvexNabtoSetpointKey.SUPPLYAIR_MIN_TEMP_SUMMER] = GenvexNabtoSetpoint(read_address=171, write_address=171, divider=100, min=0, max=4000)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.SUPPLYAIR_MIN_TEMP_SUMMER)
            self._setpoints[GenvexNabtoSetpointKey.SUPPLYAIR_MAX_TEMP_SUMMER] = GenvexNabtoSetpoint(read_address=173, write_address=173, divider=100, min=0, max=4000)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.SUPPLYAIR_MAX_TEMP_SUMMER)

        if self.deviceHasQuirk("coolingPriority", self._slaveDeviceModel):
            self._setpoints[GenvexNabtoSetpointKey.COOLING_PRIORITY] = GenvexNabtoSetpoint(read_address=191, write_address=191, min=0, max=1)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.COOLING_PRIORITY)

        if self.deviceHasQuirk("coolingOffset", self._slaveDeviceModel):
            self._setpoints[GenvexNabtoSetpointKey.COOLING_OFFSET] = GenvexNabtoSetpoint(read_address=170, write_address=170, min=0, max=10)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.COOLING_OFFSET)

        if self.deviceHasQuirk("heatpumpData", self._slaveDeviceModel):
            self._datapoints[GenvexNabtoDatapointKey.HPS_OPERATION_STATE] = GenvexNabtoDatapoint(address=198)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HPS_OPERATION_STATE) 
            self._datapoints[GenvexNabtoDatapointKey.HPS_HEATPUMP_ACTIVE] = GenvexNabtoDatapoint(address=164)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HPS_HEATPUMP_ACTIVE) 
            self._datapoints[GenvexNabtoDatapointKey.HPS_HEATER_ACTIVE] = GenvexNabtoDatapoint(address=165)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HPS_HEATER_ACTIVE) 
            self._datapoints[GenvexNabtoDatapointKey.HPS_CAPACITY_ACTUAL] = GenvexNabtoDatapoint(address=268, divider=10)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HPS_CAPACITY_ACTUAL) 

            
            self._datapoints[GenvexNabtoDatapointKey.HPS_TEMP_AFTER_CONDENSER] = GenvexNabtoDatapoint(address=57, divider=10)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HPS_TEMP_AFTER_CONDENSER) 
            self._datapoints[GenvexNabtoDatapointKey.HPS_TEMP_BEFORE_CONDENSER] = GenvexNabtoDatapoint(address=154, divider=10)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HPS_TEMP_BEFORE_CONDENSER) 
            self._datapoints[GenvexNabtoDatapointKey.HPS_TEMP_BUFFERTANK] = GenvexNabtoDatapoint(address=252, divider=10)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HPS_TEMP_BUFFERTANK) 
            self._datapoints[GenvexNabtoDatapointKey.HPS_TEMP_HEATPUMP_OUTDOOR] = GenvexNabtoDatapoint(address=156, divider=10)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HPS_TEMP_HEATPUMP_OUTDOOR) 
            self._datapoints[GenvexNabtoDatapointKey.HPS_TEMP_PRESSURE_PIPE] = GenvexNabtoDatapoint(address=256, divider=10)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.HPS_TEMP_PRESSURE_PIPE) 

        if self.deviceHasQuirk("centralHeat", self._slaveDeviceModel):
            self._setpoints[GenvexNabtoSetpointKey.CENTRALHEAT_SUPPLY_MIN] = GenvexNabtoSetpoint(read_address=203, write_address=203, divider=100, min=0, max=6000)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.CENTRALHEAT_SUPPLY_MIN)
            self._setpoints[GenvexNabtoSetpointKey.CENTRALHEAT_SUPPLY_MAX] = GenvexNabtoSetpoint(read_address=204, write_address=204, divider=100, min=0, max=6000)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.CENTRALHEAT_SUPPLY_MAX)
            self._setpoints[GenvexNabtoSetpointKey.CENTRALHEAT_PUMP_MODE] = GenvexNabtoSetpoint(read_address=207, write_address=207, divider=1, min=0, max=1)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.CENTRALHEAT_PUMP_MODE)
            self._setpoints[GenvexNabtoSetpointKey.CENTRALHEAT_TYPE] = GenvexNabtoSetpoint(read_address=208, write_address=208, divider=1, min=0, max=3)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.CENTRALHEAT_TYPE)
            self._setpoints[GenvexNabtoSetpointKey.CENTRALHEAT_SELECT] = GenvexNabtoSetpoint(read_address=202, write_address=202, divider=1, min=0, max=2)
            self._defaultSetpointRequest.append(GenvexNabtoSetpointKey.CENTRALHEAT_SELECT)

            self._datapoints[GenvexNabtoDatapointKey.CENTRALHEAT_TEMP_SUPPLY] = GenvexNabtoDatapoint(address=45, divider=100)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.CENTRALHEAT_TEMP_SUPPLY) 
            self._datapoints[GenvexNabtoDatapointKey.CENTRALHEAT_TEMP_RETURN] = GenvexNabtoDatapoint(address=44, divider=100)
            self._defaultDatapointRequest.append(GenvexNabtoDatapointKey.CENTRALHEAT_TEMP_RETURN) 

        return

    def getModelName(self):
        if int(self._slaveDeviceModel) in self._modelNames:
            return f'CTS 602 - {self._modelNames[int(self._slaveDeviceModel)]}'
        return "CTS 602 - Unknown model"
    
    def getManufacturer(self):
        return "Nilan"
    