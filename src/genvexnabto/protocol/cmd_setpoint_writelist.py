from typing import List
from .payload import GenvexCommandType
from ..models import GenvexNabtoSetpoint

class GenvexCommandSetpointWriteList():
    
    @staticmethod
    def buildCommand(setpoints = []): 
        request = b""
        for setpoint in setpoints:
            request += setpoint[0].to_bytes(1, 'big') + setpoint[1].to_bytes(4, 'big') + setpoint[2].to_bytes(2, 'big')
        return b"".join([
            b'\x00\x00\x00',
            GenvexCommandType.SETPOINT_WRITELIST,            
            (len(setpoints)).to_bytes(2, 'big'),
            request,
            b'\x01' # Seems like terminator for list/command
        ])