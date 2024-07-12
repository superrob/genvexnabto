from .payload import GenvexPayload, GenvexPayloadType

class GenvexPayloadIPX(GenvexPayload):
    
    requiresChecksum = False
    payloadType = GenvexPayloadType.U_IPX

    def __init__(self) -> None:
        pass

    def buildPayload(self): 
        return b"".join([
            self.payloadType,
            self.payloadFlags,
            b'\x00\x11', # Fixed payload length of 17
            b'\x00\x00\x00\x00', # NOT NEEDED Private Network IP
            b'\x00\x00', # NOT NEEDED Private Network Port
            b'\x00\x00\x00\x00', # NOT NEEDED Public IP
            b'\x00\x00', # NOT NEEDED Public Port
            b'\xa0' # disable rendez-vous and client peer is able of communication asynchroniously
        ])