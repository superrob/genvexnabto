class GenvexPayloadType:
    U_IPX = b'\x35'
    U_CRYPT = b'\x36'
    U_CP_ID = b'\x3F'
# There are more, but others are no interrest in them to us currently.

class GenvexCommandType:    
    DATAPOINT_READLIST = b'\x2d'
    SETPOINT_READLIST = b'\x2a'
    SETPOINT_WRITELIST = b'\x2b'
    KEEP_ALIVE = b'\x02'
    PING = b'\x11'

class GenvexPayload():
    
    requiresChecksum = False
    payloadType = None
    payloadFlags = b'\x00'

    def __init__(self) -> None:
        pass

    def buildPayload(): 
        return b''