from typing import Dict, List
from collections.abc import Callable
from .models import ( GenvexNabtoBaseModel, GenvexNabtoOptima270, GenvexNabtoOptima260, GenvexNabtoOptima251, GenvexNabtoOptima250, 
                     GenvexNabtoCTS400,
                     GenvexNabtoDatapoint, GenvexNabtoDatapointKey, GenvexNabtoSetpoint, GenvexNabtoSetpointKey )

class GenvexNabtoModelAdapter:
    _loadedModel: GenvexNabtoBaseModel = None

    _currentDatapointList: Dict[int, List[GenvexNabtoDatapointKey]] = {}
    _currentSetpointList: Dict[int, List[GenvexNabtoSetpointKey]] = {}

    _VALUES = {}
    _UPDATE_HANDLERS: Dict[GenvexNabtoDatapointKey|GenvexNabtoSetpointKey, List[Callable[[int, int], None]]] = {}

    def __init__(self, model, deviceNumber, slaveDeviceModel):
        if model == 2010 and deviceNumber == 79265:
            self._loadedModel = GenvexNabtoOptima270()
        elif model == 1040 and deviceNumber == 70810 and slaveDeviceModel == 26:
            self._loadedModel = GenvexNabtoOptima260()
        elif model == 1040 and deviceNumber == 79250 and slaveDeviceModel == 8:
            self._loadedModel = GenvexNabtoOptima251()
        elif model == 1040 and deviceNumber == 79250 and slaveDeviceModel == 1:
            self._loadedModel = GenvexNabtoOptima250()
        elif (model == 1141 or model == 1140) and deviceNumber == 72270:
            self._loadedModel = GenvexNabtoCTS400()
        else:
            raise "Invalid model"
        self._currentDatapointList = {100: self._loadedModel.getDefaultDatapointRequest()}
        self._currentSetpointList = {200: self._loadedModel.getDefaultSetpointRequest()}

    def getModelName(self):
        return self._loadedModel.getModelName()

    @staticmethod
    def providesModel(model, deviceNumber, slaveDeviceModel):
        if model == 2010 and deviceNumber == 79265:
            return True
        if model == 1040 and deviceNumber == 70810:
            if slaveDeviceModel == 26 or slaveDeviceModel == 1 or slaveDeviceModel == 8:
                return True
        if model == 1141 or model == 1140: #Nilan
            if deviceNumber == 72270 or deviceNumber == 2763306: #72270  = CTS400 | 2763306 = CTS602
                return True
        return False
    
    def providesValue(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey):
        if self._loadedModel.modelProvidesDatapoint(key) or self._loadedModel.modelProvidesSetpoint(key):
            return True 
        return False

    def hasValue(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey) -> bool:
        return key in self._VALUES
    
    def getValue(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey):
        return self._VALUES[key]
    
    def registerUpdateHandler(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey, updateMethod: Callable[[int, int], None]):
        if key not in self._UPDATE_HANDLERS:
            self._UPDATE_HANDLERS[key] = []
        self._UPDATE_HANDLERS[key].append(updateMethod)

    def notifyAllUpdateHandlers(self):
        for key in self._UPDATE_HANDLERS:
            for method in self._UPDATE_HANDLERS[key]:
                method(-1, self._VALUES[key])

    
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
            if valueKey in self._VALUES:
                oldValue = self._VALUES[valueKey]
            self._VALUES[valueKey] = (int.from_bytes(payloadSlice, 'big') + self._loadedModel._datapoints[valueKey]['offset']) / self._loadedModel._datapoints[valueKey]['divider']
            if oldValue != self._VALUES[valueKey]:
                if valueKey in self._UPDATE_HANDLERS:
                    for method in self._UPDATE_HANDLERS[valueKey]:
                        method(oldValue, self._VALUES[valueKey])
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
            if valueKey in self._VALUES:
                oldValue = self._VALUES[valueKey]
            self._VALUES[valueKey] = (int.from_bytes(payloadSlice, 'big') + self._loadedModel._setpoints[valueKey]['offset']) / self._loadedModel._setpoints[valueKey]['divider']
            if oldValue != self._VALUES[valueKey]:
                if valueKey in self._UPDATE_HANDLERS:
                    for method in self._UPDATE_HANDLERS[valueKey]:
                        method(oldValue, self._VALUES[valueKey])
        return

