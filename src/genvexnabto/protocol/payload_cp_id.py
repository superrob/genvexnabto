from .payload import GenvexPayload, GenvexPayloadType

class GenvexPayloadCP_ID(GenvexPayload):
    
    requiresChecksum = False
    payloadType = GenvexPayloadType.U_CP_ID

    email = ""

    def __init__(self) -> None:
        pass

    def setEmail(self, email):
        self.email = email

    def buildPayload(self): 
        length = 5 + len(self.email)
        return b"".join([
            self.payloadType,
            self.payloadFlags,
            length.to_bytes(2, 'big'),
            b'\x01', # ID type email
            self.email.encode("ascii")
        ])