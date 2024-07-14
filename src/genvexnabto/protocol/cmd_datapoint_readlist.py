from typing import List
from .payload import GenvexCommandType
from ..models import GenvexNabtoDatapoint

class GenvexCommandDatapointReadList():
    
    @staticmethod
    def buildCommand(datapoints: List[GenvexNabtoDatapoint] = []): 
        request = b""
        for datapoint in datapoints:
            request += datapoint['obj'].to_bytes(1, 'big') + datapoint['address'].to_bytes(4, 'big')
        return b"".join([
            b'\x00\x00\x00',
            GenvexCommandType.DATAPOINT_READLIST,            
            (len(datapoints)).to_bytes(2, 'big'),
            request,
            b'\x01' # Seems like terminator for list/command
        ])