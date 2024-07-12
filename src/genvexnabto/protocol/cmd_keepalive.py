from .payload import GenvexPayload, GenvexCommandType

class GenvexCommandKeepAlive():
    
    def __init__(self) -> None:
        pass

    def buildCommand(self): 
        return b"".join([
            b'\x00\x00\x00',
            GenvexCommandType.KEEP_ALIVE,
        ])