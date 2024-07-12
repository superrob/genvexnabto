from .payload import GenvexPayload, GenvexCommandType

class GenvexCommandDatapointReadList():
    
    def __init__(self) -> None:
        pass

    def buildCommand(self, datapoints = []): 
        request = b""
        for datapoint in datapoints:
            request += datapoint[0].to_bytes(1, 'big') + datapoint[1].to_bytes(4, 'big')
        return b"".join([
            b'\x00\x00\x00',
            GenvexCommandType.DATAPOINT_READLIST,            
            (len(datapoints)).to_bytes(2, 'big'),
            request,
            b'\x01' # Seems like terminator for list/command
        ])