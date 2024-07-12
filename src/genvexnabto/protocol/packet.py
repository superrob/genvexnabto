from .payload import GenvexPayload

class GenvexPacketType: 
    U_CONNECT = b'\x83'
    DATA = b'\x16'

class GenvexPacket():
    @staticmethod
    def build_packet(CLIENT_ID, SERVER_ID, PACKET_TYPE: GenvexPacketType, SEQUENCE_ID, PAYLOADS: list[GenvexPayload]=[]):
        payloadBundle = b''
        checksumRequired = False
        for payload in PAYLOADS:
            payloadBundle += payload.buildPayload()
            if payload.requiresChecksum:
                checksumRequired = True
        
        packetLength = len(payloadBundle) + 16
        if checksumRequired:
            packetLength += 2
        
        packet = b''.join([
            CLIENT_ID,
            SERVER_ID,
            PACKET_TYPE,
            b'\x02', # Version
            b'\x00', # Retransmision count
            b'\x00', # Flags
            SEQUENCE_ID.to_bytes(2, 'big'),
            packetLength.to_bytes(2, 'big'),
            payloadBundle
        ])
        if checksumRequired:
            # Calculate the checksum. It is simply a sum of all bytes.
            sum = 0
            for b in packet:
                sum += b
            packet = b''.join([
                packet,
                sum.to_bytes(2, 'big')
            ])
        return packet