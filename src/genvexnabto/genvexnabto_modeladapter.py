from typing import Dict, List
from .models import ( GenvexNabtoBaseModel, GenvexNabtoOptima270, GenvexNabtoDatapoint, GenvexNabtoDatapointKey, GenvexNabtoSetpoint, GenvexNabtoSetpointKey )

class GenvexNabtoModelAdapter:
    _loadedModel: GenvexNabtoBaseModel = None

    _currentDatapointList: Dict[int, List[GenvexNabtoDatapointKey]] = {}
    _currentSetpointList: Dict[int, List[GenvexNabtoSetpointKey]] = {}

    _VALUES = {}

    def __init__(self, model):
        if (model == 2010):
            self._loadedModel = GenvexNabtoOptima270()
        else:
            raise "Invalid model"
        self._currentDatapointList = {100: self._loadedModel.getDefaultDatapointRequest()}
        self._currentSetpointList = {200: self._loadedModel.getDefaultSetpointRequest()}

    @staticmethod
    def providesModel(model):
        return model == 2010
    
    def providesValue(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey):
        if key in GenvexNabtoDatapointKey:
            return self._loadedModel.modelProvidesDatapoint(key)
        if key in GenvexNabtoSetpointKey:
            return self._loadedModel.modelProvidesSetpoint(key)
        return False

    def hasValue(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey) -> bool:
        return key in self._VALUES
    
    def getValue(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey):
        return self._VALUES[key]
    
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
            self._VALUES[valueKey] = (int.from_bytes(payloadSlice, 'big') + self._loadedModel._datapoints[valueKey]['offset']) / self._loadedModel._datapoints[valueKey]['divider']
        return
    
    def parseSetpointResponce(self, responceSeq, responcePayload):
        if responceSeq not in self._currentSetpointList:
            return False
        decodingKeys = self._currentSetpointList[responceSeq]
        responceLength = int.from_bytes(responcePayload[1:3])
        for position in range(responceLength):
            valueKey = decodingKeys[position]
            payloadSlice = responcePayload[3+position*2:5+position*2]
            self._VALUES[valueKey] = (int.from_bytes(payloadSlice, 'big') + self._loadedModel._setpoints[valueKey]['offset']) / self._loadedModel._setpoints[valueKey]['divider']
        return

