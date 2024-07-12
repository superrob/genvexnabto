from .payload import GenvexPayload
from .packet import GenvexPacketType
from .cmd_keepalive import GenvexCommandKeepAlive
from .payload_crypt import GenvexPayloadCrypt

class GenvexPacketKeepAlive():
    @staticmethod
    def build_packet(CLIENT_ID, SERVER_ID, SEQUENCE_ID):

        CryptPayload = GenvexPayloadCrypt()
        CryptPayload.setData(GenvexCommandKeepAlive().buildCommand())
        payload = CryptPayload.buildPayload()
        packetLength = len(payload) + 18 + 2 # Header with framecontrol tag and checksum at end
        
        packet = b''.join([
            CLIENT_ID,
            SERVER_ID,
            GenvexPacketType.DATA,
            b'\x02', # Version
            b'\x00', # Retransmision count
            b'\x40', # Flags
            SEQUENCE_ID.to_bytes(2, 'big'),
            packetLength.to_bytes(2, 'big'),
            b'\x00\x03', #Frame control tag
            payload            
        ])
        
        sum = 0
        for b in packet:
            sum += b
        packet = b''.join([
            packet,
            sum.to_bytes(2, 'big')
        ])
        return packet