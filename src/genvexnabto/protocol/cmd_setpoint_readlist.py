from .payload import GenvexPayload, GenvexCommandType
from ..models import GenvexNabtoDatapointKey, GenvexNabtoDatapoint

class GenvexCommandSetpointReadList():
    
    @staticmethod
    def buildCommand(setpoints = []): 
        request = b""
        for setpoint in setpoints:
            request += setpoint[0].to_bytes(1, 'big') + setpoint[1].to_bytes(2, 'big')
        return b"".join([
            b'\x00\x00\x00',
            GenvexCommandType.SETPOINT_READLIST,            
            (len(setpoints)).to_bytes(2, 'big'),
            request,
            b'\x01' # Seems like terminator for list/command
        ])