import asyncio
from random import randint
import socket
import threading
import time


from .protocol import (GenvexPacketType, GenvexDiscovery, GenvexPayloadIPX, GenvexPayloadCrypt, 
                       GenvexPayloadCP_ID,  GenvexPacket, GenvexPacketKeepAlive, GenvexCommandDatapointReadList, 
                       GenvexCommandSetpointReadList, GenvexCommandPing, GenvexCommandSetpointWriteList)

class GenvexNabtoConnectionErrorType:
    TIMEOUT = "timeout"
    AUTHENTICATION_ERROR = "authentication_error"
    UNSUPPORTED_MODEL = "unsupported_model"

class GenvexNabto():
    AUTHORIZED_EMAIL = ""

    CLIENT_ID = randint(0,0xffffffff).to_bytes(4, 'big') # Our client ID can be anything.
    SERVER_ID = b'\x00\x00\x00\x00' # This is our ID optained from the uNabto service on device.

    DEVICE_ID = None
    DEVICE_IP = None
    DEVICE_PORT = 5570
    DEVICE_MODEL = None

    CONNECTION_TIMEOUT = None
    IS_CONNECTED = False
    CONNECTION_ERROR = False
    LAST_RESPONCE = 0

    DISCOVERY_PORT = 5570

    SOCKET = None
    LISTEN_THREAD = None
    LISTEN_THREAD_OPEN = False

    VALUES = {}

    DISCOVERED_DEVICES = {}

    def __init__(self, email = "", device_ip = None, deviceID = None) -> None:
        self.AUTHORIZED_EMAIL = email
        self.DEVICE_IP = device_ip
        self.DEVICE_ID = deviceID
        return

    def openSocket(self):
        if self.SOCKET is not None:
            return
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
        self.SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Allows for sending broadcasts
        self.SOCKET.settimeout(1)
        self.SOCKET.bind(("", 0))

    def startListening(self):
        if self.LISTEN_THREAD_OPEN:
            return False
        if self.SOCKET == None:
            self.openSocket()
        self.LISTEN_THREAD = threading.Thread(target=self.receiveThread)
        self.LISTEN_THREAD_OPEN = True
        self.LISTEN_THREAD.start()

    def stopListening(self):
        self.LISTEN_THREAD_OPEN = False

    def closeSocket(self):
        self.SOCKET.close()
        self.SOCKET = None

    # Broadcasts a discovery packet. Any device listening should respond.
    def sendDiscovery(self, specificDevice = None): 
        if self.SOCKET == None:
            return
        self.SOCKET.sendto(GenvexDiscovery.build_packet(specificDevice), ("255.255.255.255", 5570))

    async def discoverDevices(self):
        self.sendDiscovery()
        await asyncio.sleep(0.5) # Allow for all devices to reply
        return self.DISCOVERED_DEVICES
    
    def setDevice(self, device_id):
        self.DEVICE_ID = device_id
        self.getDeviceIP()

    def getDeviceIP(self):
        # Check if we already know the IP from earlier
        if self.DEVICE_ID in self.DISCOVERED_DEVICES:
            self.DEVICE_IP = self.DISCOVERED_DEVICES[self.DEVICE_ID][0]
            self.DEVICE_PORT = self.DISCOVERED_DEVICES[self.DEVICE_ID][1]
        else:
            self.sendDiscovery(self.DEVICE_ID)

    def connectToDevice(self):
        if self.SOCKET == None:
            return False
        if self.LISTEN_THREAD_OPEN == False:
            return False
        self.CONNECTION_ERROR = False
        IPXPayload = GenvexPayloadIPX()
        CP_IDPayload = GenvexPayloadCP_ID()
        CP_IDPayload.setEmail(self.AUTHORIZED_EMAIL)
        self.SOCKET.sendto(GenvexPacket.build_packet(self.CLIENT_ID, self.SERVER_ID, GenvexPacketType.U_CONNECT, 0, [IPXPayload, CP_IDPayload]), (self.DEVICE_IP, self.DEVICE_PORT))

    async def waitForConnection(self):
        """Wait for connection to be tried"""
        connectionTimeout = time.time() + 3
        while self.CONNECTION_ERROR is False and self.IS_CONNECTED is False:
            if time.time() > connectionTimeout:
                self.CONNECTION_ERROR = GenvexNabtoConnectionErrorType.TIMEOUT                
                connectionTimeout = None
            await asyncio.sleep(0.2)

    async def waitForDiscovery(self):
        """Wait for discovery of ip to be done"""
        discoveryTimeout = time.time() + 3
        while True:
            if self.DEVICE_ID in self.DISCOVERED_DEVICES and self.DEVICE_IP is not None:
                return True
            if time.time() > discoveryTimeout:
                return False
            await asyncio.sleep(0.2)

    async def waitForData(self):
        """Wait for data to be available"""
        dataTimeout = time.time() + 12
        while True:
            if 'temp_supply' in self.VALUES and 'fan_set' in self.VALUES: # TODO Add setpoint data check
                return True
            if time.time() > dataTimeout:
                return False
            await asyncio.sleep(0.2)

    def processDataPayload(self, payload):
        self.VALUES['temp_supply'] = (int.from_bytes(payload[2:4], 'big')-300)/10
        self.VALUES['temp_outside'] = (int.from_bytes(payload[4:6], 'big')-300)/10
        self.VALUES['temp_extract'] = (int.from_bytes(payload[6:8], 'big')-300)/10
        self.VALUES['temp_exhaust'] = (int.from_bytes(payload[8:10], 'big')-300)/10
        self.VALUES['humidity'] = int.from_bytes(payload[10:12], 'big')
        self.VALUES['dutycycle_supply'] = int.from_bytes(payload[12:14], 'big')/100
        self.VALUES['dutycycle_extract'] = int.from_bytes(payload[14:16], 'big')/100
        self.VALUES['bypass_active'] = int.from_bytes(payload[16:18], 'big')

    def processSetpointPayload(self, payload):
        self.VALUES['fan_set'] = int.from_bytes(payload[3:5], 'big')
        self.VALUES['temp_setpoint'] = (int.from_bytes(payload[5:7], 'big')+100)/10

    def processPingPayload(self, payload):
        self.DEVICE_MODEL = int.from_bytes(payload[8:12], 'big')
        if self.DEVICE_MODEL == 2010: # Seems to be Optima 270
            self.IS_CONNECTED = True
            self.sendDataStateRequest()
            self.sendSetpointStateRequest()
        else:
            self.CONNECTION_ERROR = GenvexNabtoConnectionErrorType.UNSUPPORTED_MODEL

    def processReceivedMessage(self, message, address):
        if message[0:4] == b'\x00\x80\x00\x01': # This might be a discovery packet responce!
            discoveryResponce = message[19:len(message)]
            deviceIdLength = 0
            for b in discoveryResponce:
                if b == 0x00:
                    break;
                deviceIdLength += 1
            deviceId = discoveryResponce[0: deviceIdLength].decode("ascii")
            if "remote.lscontrol.dk" in deviceId:
                # This is a valid reponse from a GenvexConnect device!
                # Add the device Id and IP to our list if not seen before.
                if deviceId not in self.DISCOVERED_DEVICES:
                    self.DISCOVERED_DEVICES[deviceId] = address
            if deviceId == self.DEVICE_ID:
                self.SERVER_ID = address[0]
            return
        if message[0:4] != self.CLIENT_ID: # Not a packet intented for us
            return
        self.LAST_RESPONCE = time.time()
        packetType = message[8].to_bytes(1, 'big')
        if (packetType == GenvexPacketType.U_CONNECT):
            print("U_CONNECT responce packet")
            if (message[20:24] == b'\x00\x00\x00\x01'):
                print('Connected, pinging to get model number')
                self.sendPing()
                self.SERVER_ID = message[24:28]
            else:
                print("Received unsucessfull response")
                self.CONNECTION_ERROR = GenvexNabtoConnectionErrorType.AUTHENTICATION_ERROR

        elif (packetType == GenvexPacketType.DATA): # 0x16
            print("Data packet", message[16])
            # We only care about data packets with crypt payload. 
            if message[16] == 54: # x36
                print("Packet with crypt payload!")
                length = int.from_bytes(message[18:20], 'big')
                payload = message[22:20+length]
                print(''.join(r'\x'+hex(letter)[2:] for letter in payload))
                if (message[12:14] == b'\x05\x39'): #1337
                    self.processDataPayload(payload)
                elif (message[12:14] == b'\x01\xa4'): #420
                    self.processSetpointPayload(payload)
                elif (message[12:14] == b'\x00\x64'): #100
                    self.processPingPayload(payload)
            else:
                print("Not an interresting data packet.")
        else:
            print("Unknown packet type. Ignoring")

    def sendPing(self):
        PingCmd = GenvexCommandPing()
        Payload = GenvexPayloadCrypt()
        Payload.setData(PingCmd.buildCommand())
        self.SOCKET.sendto(GenvexPacket().build_packet(self.CLIENT_ID, self.SERVER_ID, GenvexPacketType.DATA, 100, [Payload]), (self.DEVICE_IP, self.DEVICE_PORT))

    def sendDataStateRequest(self):
        ReadlistCmd = GenvexCommandDatapointReadList()
        Payload = GenvexPayloadCrypt()
        Payload.setData(ReadlistCmd.buildCommand([(0, 20), (0, 21), (0, 22), (0, 23), (0, 26), (0, 18), (0, 19), (0, 53)]))
        self.SOCKET.sendto(GenvexPacket().build_packet(self.CLIENT_ID, self.SERVER_ID, GenvexPacketType.DATA, 1337, [Payload]), (self.DEVICE_IP, self.DEVICE_PORT))

    def sendSetpointStateRequest(self):
        ReadlistCmd = GenvexCommandSetpointReadList()
        Payload = GenvexPayloadCrypt()
        Payload.setData(ReadlistCmd.buildCommand([(0, 7), (0, 1)]))
        self.SOCKET.sendto(GenvexPacket().build_packet(self.CLIENT_ID, self.SERVER_ID, GenvexPacketType.DATA, 420, [Payload]), (self.DEVICE_IP, self.DEVICE_PORT))

    def setTargetTemperature(self, target: int):
        if target < 10 or target > 30:
            return
        WritelistCmd = GenvexCommandSetpointWriteList()
        Payload = GenvexPayloadCrypt()
        temperature = (int(target) * 10) + 100
        Payload.setData(WritelistCmd.buildCommand([(0, 12, temperature)]))
        self.SOCKET.sendto(GenvexPacket().build_packet(self.CLIENT_ID, self.SERVER_ID, GenvexPacketType.DATA, 3, [Payload]), (self.DEVICE_IP, self.DEVICE_PORT))
    
    def setFanSpeed(self, target: int):
        if target < 0 or target > 4:
            return
        WritelistCmd = GenvexCommandSetpointWriteList()
        Payload = GenvexPayloadCrypt()
        Payload.setData(WritelistCmd.buildCommand([(0, 24, int(target))]))
        self.SOCKET.sendto(GenvexPacket().build_packet(self.CLIENT_ID, self.SERVER_ID, GenvexPacketType.DATA, 3, [Payload]), (self.DEVICE_IP, self.DEVICE_PORT))

    def handleRecieve(self):
        try:
            message, address = self.SOCKET.recvfrom(512)
            if (len(message) < 16): # Not a valid packet
                return 
            self.processReceivedMessage(message, address)
        except socket.timeout:  
            return

    def receiveThread(self):
        while self.LISTEN_THREAD_OPEN:
            self.handleRecieve()          
            if self.IS_CONNECTED:
                if time.time() - self.LAST_RESPONCE > 10:
                    print("Sending data request..")
                    self.sendDataStateRequest()
                    self.sendSetpointStateRequest()
                    
