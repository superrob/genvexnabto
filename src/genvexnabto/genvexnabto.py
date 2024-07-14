import asyncio
from random import randint
import socket
import threading
import time

from .models import ( GenvexNabtoDatapointKey, GenvexNabtoSetpointKey )
from .genvexnabto_modeladapter import GenvexNabtoModelAdapter
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

    MODEL_ADAPTER = None

    CONNECTION_TIMEOUT = None
    IS_CONNECTED = False
    CONNECTION_ERROR = False
    LAST_RESPONCE = 0

    DISCOVERY_PORT = 5570

    SOCKET = None
    LISTEN_THREAD = None
    LISTEN_THREAD_OPEN = False

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
            if self.MODEL_ADAPTER is not None:
                if self.MODEL_ADAPTER.hasValue(GenvexNabtoDatapointKey.TEMP_SUPPLY) and self.MODEL_ADAPTER.hasValue(GenvexNabtoSetpointKey.TEMP_SETPOINT):
                    return True
            if time.time() > dataTimeout:
                return False
            await asyncio.sleep(0.2)

    def providesValue(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey):
        if self.MODEL_ADAPTER is None:
            return False
        return self.MODEL_ADAPTER.providesModel()

    def hasValue(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey):
        if self.MODEL_ADAPTER is None:
            return False
        return self.MODEL_ADAPTER.hasValue(key)
    
    def getValue(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey):
        if self.MODEL_ADAPTER is None:
            return False
        return self.MODEL_ADAPTER.getValue(key)

    def processPingPayload(self, payload):
        self.DEVICE_MODEL = int.from_bytes(payload[8:12], 'big')
        print(f"Got model: {self.DEVICE_MODEL}")
        if GenvexNabtoModelAdapter.providesModel(self.DEVICE_MODEL):
            self.IS_CONNECTED = True
            self.MODEL_ADAPTER = GenvexNabtoModelAdapter(self.DEVICE_MODEL)
            self.sendDataStateRequest(100)
            self.sendSetpointStateRequest(200)
        else:
            self.CONNECTION_ERROR = GenvexNabtoConnectionErrorType.UNSUPPORTED_MODEL

    def processReceivedMessage(self, message, address):
        if message[0:4] == b'\x00\x80\x00\x01': # This might be a discovery packet responce!
            discoveryResponce = message[19:len(message)]
            deviceIdLength = 0
            for b in discoveryResponce: # Loop until first string terminator
                if b == 0x00:
                    break
                deviceIdLength += 1
            deviceId = discoveryResponce[0: deviceIdLength].decode("ascii")
            if "remote.lscontrol.dk" in deviceId:
                # This is a valid reponse from a GenvexConnect device!
                # Add the device Id and IP to our list if not seen before.
                if deviceId not in self.DISCOVERED_DEVICES:
                    self.DISCOVERED_DEVICES[deviceId] = address
            if deviceId == self.DEVICE_ID:
                self.DEVICE_IP = address[0]
            return
        if message[0:4] != self.CLIENT_ID: # Not a packet intented for us
            return
        self.LAST_RESPONCE = time.time()
        packetType = message[8].to_bytes(1, 'big')
        if (packetType == GenvexPacketType.U_CONNECT):
            print("U_CONNECT responce packet")
            if (message[20:24] == b'\x00\x00\x00\x01'):
                print('Connected, pinging to get model number')
                self.SERVER_ID = message[24:28]
                self.sendPing()
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
                sequenceId = int.from_bytes(message[12:14], 'big')
                if sequenceId == 50: #50
                    self.processPingPayload(payload)
                else:
                    if self.MODEL_ADAPTER is not None:
                        self.MODEL_ADAPTER.parseDataResponce(sequenceId, payload)
            else:
                print("Not an interresting data packet.")
        else:
            print("Unknown packet type. Ignoring")

    def sendPing(self):
        PingCmd = GenvexCommandPing()
        Payload = GenvexPayloadCrypt()
        Payload.setData(PingCmd.buildCommand())
        self.SOCKET.sendto(GenvexPacket().build_packet(self.CLIENT_ID, self.SERVER_ID, GenvexPacketType.DATA, 50, [Payload]), (self.DEVICE_IP, self.DEVICE_PORT))

    def sendDataStateRequest(self, sequenceId):
        if self.MODEL_ADAPTER is None:
            return
        datalist = self.MODEL_ADAPTER.getDatapointRequestList(sequenceId)
        if datalist is False:
            return
        Payload = GenvexPayloadCrypt()
        Payload.setData(GenvexCommandDatapointReadList.buildCommand(datalist))
        self.SOCKET.sendto(GenvexPacket().build_packet(self.CLIENT_ID, self.SERVER_ID, GenvexPacketType.DATA, sequenceId, [Payload]), (self.DEVICE_IP, self.DEVICE_PORT))

    def sendSetpointStateRequest(self, sequenceId):
        Payload = GenvexPayloadCrypt()
        datalist = self.MODEL_ADAPTER.getSetpointRequestList(sequenceId)
        if datalist is False:
            return
        Payload.setData(GenvexCommandSetpointReadList.buildCommand(datalist))
        self.SOCKET.sendto(GenvexPacket().build_packet(self.CLIENT_ID, self.SERVER_ID, GenvexPacketType.DATA, sequenceId, [Payload]), (self.DEVICE_IP, self.DEVICE_PORT))

    def setSetpoint(self, setpointKey: GenvexNabtoSetpointKey, newValue) -> bool:
        if self.MODEL_ADAPTER is None:
            return False
        if self.MODEL_ADAPTER.providesValue(setpointKey) is False:
            return False
        setpointData = self.MODEL_ADAPTER._loadedModel._setpoints[setpointKey]
        newValue = int((newValue * setpointData["divider"]) - setpointData['offset'])
        if newValue < setpointData['min'] or newValue > setpointData['max']:
            return False
        Payload = GenvexPayloadCrypt()
        Payload.setData(GenvexCommandSetpointWriteList.buildCommand([(setpointData['write_obj'], setpointData['write_address'], newValue)]))
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
                    self.sendDataStateRequest(100)
                    self.sendSetpointStateRequest(200)
                    
