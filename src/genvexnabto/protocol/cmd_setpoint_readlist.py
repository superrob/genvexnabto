from .payload import GenvexPayload, GenvexCommandType

class GenvexCommandSetpointReadList():
    
    def __init__(self) -> None:
        pass

    def buildCommand(self, setpoints = []): 
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