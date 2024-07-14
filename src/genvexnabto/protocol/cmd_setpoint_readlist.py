from typing import List
from .payload import GenvexCommandType
from ..models import GenvexNabtoSetpoint

class GenvexCommandSetpointReadList():
    
    @staticmethod
    def buildCommand(setpoints: List[GenvexNabtoSetpoint] = []): 
        request = b""
        for setpoint in setpoints:
            request += setpoint["read_obj"].to_bytes(1, 'big') + setpoint["read_address"].to_bytes(2, 'big')
        return b"".join([
            b'\x00\x00\x00',
            GenvexCommandType.SETPOINT_READLIST,            
            (len(setpoints)).to_bytes(2, 'big'),
            request,
            b'\x01' # Seems like terminator for list/command
        ])