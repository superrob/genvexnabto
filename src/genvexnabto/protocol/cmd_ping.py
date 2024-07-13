from .payload import GenvexPayload, GenvexCommandType

class GenvexCommandPing():
    
    def __init__(self) -> None:
        pass

    def buildCommand(self): 
        return b"".join([
            b'\x00\x00\x00',
            GenvexCommandType.PING,
            b'\x70\x69\x6e\x67'
        ])