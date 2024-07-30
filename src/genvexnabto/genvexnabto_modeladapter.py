from typing import Dict, List
from collections.abc import Callable
from .models import ( GenvexNabtoBaseModel, GenvexNabtoOptima314, GenvexNabtoOptima312, GenvexNabtoOptima301, GenvexNabtoOptima270, GenvexNabtoOptima260, GenvexNabtoOptima251, GenvexNabtoOptima250, 
                     GenvexNabtoCTS400, GenvexNabtoCTS602, GenvexNabtoCTS602Light,
                     GenvexNabtoDatapoint, GenvexNabtoDatapointKey, GenvexNabtoSetpoint, GenvexNabtoSetpointKey )

class GenvexNabtoModelAdapter:
    _loadedModel: GenvexNabtoBaseModel = None

    _currentDatapointList: Dict[int, List[GenvexNabtoDatapointKey]] = {}
    _currentSetpointList: Dict[int, List[GenvexNabtoSetpointKey]] = {}

    _values = {}
    _update_handlers: Dict[GenvexNabtoDatapointKey|GenvexNabtoSetpointKey, List[Callable[[int, int], None]]] = {}

    def __init__(self, model, deviceNumber, slaveDeviceNumber, slaveDeviceModel):
        modelToLoad = GenvexNabtoModelAdapter.translateToModel(model, deviceNumber, slaveDeviceNumber, slaveDeviceModel)
        if modelToLoad == None:
            raise "Invalid model"
        self._loadedModel = modelToLoad()
        self._loadedModel.addDeviceQuirks(deviceNumber, slaveDeviceNumber, slaveDeviceModel)
            
        self._currentDatapointList = {100: self._loadedModel.getDefaultDatapointRequest()}
        self._currentSetpointList = {200: self._loadedModel.getDefaultSetpointRequest()}

    def getModelName(self):
        return self._loadedModel.getModelName()
    
    def getManufacturer(self):
        return self._loadedModel.getManufacturer()

    @staticmethod
    def translateToModel(model, deviceNumber, slaveDeviceNumber, slaveDeviceModel) -> Callable:
        if model == 2010:
            if deviceNumber == 79265:
                return GenvexNabtoOptima270
        if model == 2020:
            if deviceNumber == 79280:
                return GenvexNabtoOptima314
        if model == 1040:
            if slaveDeviceNumber == 70810:
                if slaveDeviceModel == 26:
                    return GenvexNabtoOptima260
            if slaveDeviceNumber == 79250:
                if slaveDeviceModel == 9:
                    return GenvexNabtoOptima312
                if slaveDeviceModel == 8:
                    return GenvexNabtoOptima251
                if slaveDeviceModel == 5:
                    return GenvexNabtoOptima301
                if slaveDeviceModel == 1:
                    return GenvexNabtoOptima250
        if model == 1140 or model == 1141:
            if slaveDeviceNumber == 72270:
                if slaveDeviceModel == 1:
                    return GenvexNabtoCTS400
            if slaveDeviceNumber == 2763306:
                if slaveDeviceModel == 2:
                    return GenvexNabtoCTS602Light
                return GenvexNabtoCTS602
            
        return None

    @staticmethod
    def providesModel(model, deviceNumber, slaveDeviceNumber, slaveDeviceModel):
        if GenvexNabtoModelAdapter.translateToModel(model, deviceNumber, slaveDeviceNumber, slaveDeviceModel) is not None:
            return True
        return False
    
    def providesValue(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey):
        if self._loadedModel.modelProvidesDatapoint(key) or self._loadedModel.modelProvidesSetpoint(key):
            return True 
        return False

    def hasValue(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey) -> bool:
        return key in self._values
    
    def getValue(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey):
        return self._values[key]
    
    def getMinValue(self, key: GenvexNabtoSetpointKey):
        if self._loadedModel.modelProvidesSetpoint(key): 
            return (self._loadedModel._setpoints[key]['min'] + self._loadedModel._setpoints[key]['offset']) / self._loadedModel._setpoints[key]['divider']
        return False
    
    def getMaxValue(self, key: GenvexNabtoSetpointKey):
        if self._loadedModel.modelProvidesSetpoint(key): 
            return (self._loadedModel._setpoints[key]['max'] + self._loadedModel._setpoints[key]['offset']) / self._loadedModel._setpoints[key]['divider']
        return False
    
    def getSetpointStep(self, key: GenvexNabtoSetpointKey):
        if self._loadedModel.modelProvidesSetpoint(key):
            if "step" in self._loadedModel._setpoints[key]:             
                return self._loadedModel._setpoints[key]['step']
        return 1
    
    def registerUpdateHandler(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey, updateMethod: Callable[[int, int], None]):
        if key not in self._update_handlers:
            self._update_handlers[key] = []
        self._update_handlers[key].append(updateMethod)

    def notifyAllUpdateHandlers(self):
        for key in self._update_handlers:
            for method in self._update_handlers[key]:
                method(-1, self._values[key])

    
    def getDatapointRequestList(self, sequenceId):
        if sequenceId not in self._currentDatapointList:
            return False
        returnList = []
        for key in self._currentDatapointList[sequenceId]:
            returnList.append(self._loadedModel._datapoints[key])
        return returnList
    
    def getSetpointRequestList(self, sequenceId):
        if sequenceId not in self._currentSetpointList:
            return False
        returnList = []
        for key in self._currentSetpointList[sequenceId]:
            returnList.append(self._loadedModel._setpoints[key])
        return returnList
    
    def parseDataResponce(self, responceSeq, responcePayload):
        print(f"Got dataresponce with sequence id: {responceSeq}")
        if responceSeq in self._currentDatapointList:
            print(f"Is a datapoint responce")
            return self.parseDatapointResponce(responceSeq, responcePayload)
        if responceSeq in self._currentSetpointList:
            print(f"Is a setpoint responce")
            return self.parseSetpointResponce(responceSeq, responcePayload)

    def parseDatapointResponce(self, responceSeq, responcePayload):
        if responceSeq not in self._currentDatapointList:
            return False
        decodingKeys = self._currentDatapointList[responceSeq]
        print(decodingKeys)
        responceLength = int.from_bytes(responcePayload[0:2])
        for position in range(responceLength):
            valueKey = decodingKeys[position]
            payloadSlice = responcePayload[2+position*2:4+position*2]
            oldValue = -1
            if valueKey in self._values:
                oldValue = self._values[valueKey]
            self._values[valueKey] = (int.from_bytes(payloadSlice, 'big') + self._loadedModel._datapoints[valueKey]['offset']) / self._loadedModel._datapoints[valueKey]['divider']
            if oldValue != self._values[valueKey]:
                if valueKey in self._update_handlers:
                    for method in self._update_handlers[valueKey]:
                        method(oldValue, self._values[valueKey])
        return
    
    def parseSetpointResponce(self, responceSeq, responcePayload):
        if responceSeq not in self._currentSetpointList:
            return False
        decodingKeys = self._currentSetpointList[responceSeq]
        responceLength = int.from_bytes(responcePayload[1:3])
        for position in range(responceLength):
            valueKey = decodingKeys[position]
            payloadSlice = responcePayload[3+position*2:5+position*2]
            oldValue = -1
            if valueKey in self._values:
                oldValue = self._values[valueKey]
            self._values[valueKey] = (int.from_bytes(payloadSlice, 'big') + self._loadedModel._setpoints[valueKey]['offset']) / self._loadedModel._setpoints[valueKey]['divider']
            if oldValue != self._values[valueKey]:
                if valueKey in self._update_handlers:
                    for method in self._update_handlers[valueKey]:
                        method(oldValue, self._values[valueKey])
        return

