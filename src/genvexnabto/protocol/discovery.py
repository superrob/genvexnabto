class GenvexDiscovery():
    @staticmethod
    def build_packet(DEVICE_ID = None):
        if DEVICE_ID == None:
            DEVICE_ID = "*"

        return b"".join([
            b'\x00\x00\x00\x01', # So called "Legacy header"
            b'\x00\x00\x00\x00\x00\x00\x00\x00', # Seems like unused space in header?
            DEVICE_ID.encode("ascii"),
            b'\x00' # Zero terminator for string
        ])