from .payload import GenvexPayload, GenvexPayloadType

class GenvexPayloadCrypt(GenvexPayload):
    
    requiresChecksum = True
    payloadType = GenvexPayloadType.U_CRYPT
    data = b''

    def __init__(self) -> None:
        pass

    def setData(self, data):
        self.data = data

    def buildPayload(self): 
        return b"".join([
            self.payloadType,
            self.payloadFlags,
            (6+len(self.data)+3).to_bytes(2, 'big'), # Header + Crypto code + data length + padding and checksum to be inserted by packet builder.
            b'\x00\x0a', # Crypto code for the payload
            self.data,
            b'\x02' # Padding??
        ])