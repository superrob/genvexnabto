import asyncio
from collections.abc import Callable
from random import randint
import socket
import threading
import time

from .models import ( GenvexNabtoDatapointKey, GenvexNabtoSetpointKey )
from .genvexnabto_modeladapter import GenvexNabtoModelAdapter
from .protocol import (GenvexPacketType, GenvexDiscovery, GenvexPayloadIPX, GenvexPayloadCrypt, 
                       GenvexPayloadCP_ID,  GenvexPacket, GenvexPacketKeepAlive, GenvexCommandDatapointReadList, 
                       GenvexCommandSetpointReadList, GenvexCommandPing, GenvexCommandSetpointWriteList)

from .const import ( SOCKET_TIMEOUT, SOCKET_MAXSIZE, DATAPOINT_UPDATEINTERVAL, SETPOINT_UPDATEINTERVAL, SECONDS_UNTILRECONNECT, DISCOVERY_PORT)

class GenvexNabtoConnectionErrorType:
    TIMEOUT = "timeout"
    AUTHENTICATION_ERROR = "authentication_error"
    UNSUPPORTED_MODEL = "unsupported_model"

class GenvexNabto():
    _authorized_email = ""

    _client_id = randint(0,0xffffffff).to_bytes(4, 'big') # Our client ID can be anything.
    _server_id = b'\x00\x00\x00\x00' # This is our ID optained from the uNabto service on device.

    _device_id = None
    _device_ip = None
    _device_port = 5570
    _device_model = None
    _device_number = None
    _slavedevice_number = None
    _slavedevice_model = None

    _model_adapter = None

    _is_connected = False
    _connection_error = False
    _last_responce = 0
    _last_dataupdate = 0
    _last_setpointupdate = 0

    _socket = None
    _listen_thread = None
    _listen_thread_open = False

    _discovered_devices = {}

    def __init__(self, _authorized_email = "", _device_id = None) -> None:
        self._authorized_email = _authorized_email
        self._device_id = _device_id
        if self._authorized_email != "" and self._device_id is not None:
            self.startListening()
            self.getDeviceIP()
        return

    def openSocket(self):
        if self._socket is not None:
            return
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Allows for sending broadcasts
        self._socket.settimeout(SOCKET_TIMEOUT)
        self._socket.bind(("", 0))

    def startListening(self):
        if self._listen_thread_open:
            return False
        if self._socket == None:
            self.openSocket()
        self._listen_thread = threading.Thread(target=self.receiveThread)
        self._listen_thread_open = True
        self._listen_thread.start()

    def stopListening(self):
        self._listen_thread_open = False

    def closeSocket(self):
        self._socket.close()
        self._socket = None

    # Broadcasts a discovery packet. Any device listening should respond.
    def sendDiscovery(self, specificDevice = None): 
        if self._socket == None:
            return
        self._socket.sendto(GenvexDiscovery.build_packet(specificDevice), ("255.255.255.255", DISCOVERY_PORT))

    async def discoverDevices(self):
        self.sendDiscovery()
        await asyncio.sleep(0.5) # Allow for all devices to reply
        return self._discovered_devices
    
    def setDevice(self, device_id):
        self._device_id = device_id
        self.getDeviceIP()

    def getDeviceIP(self):
        # Check if we already know the IP from earlier
        if self._device_id in self._discovered_devices:
            self._device_ip = self._discovered_devices[self._device_id][0]
            self._device_port = self._discovered_devices[self._device_id][1]
        else:
            self.sendDiscovery(self._device_id)

    def connectToDevice(self):
        if self._socket == None:
            return False
        if self._listen_thread_open == False:
            return False
        self._connection_error = False
        IPXPayload = GenvexPayloadIPX()
        CP_IDPayload = GenvexPayloadCP_ID()
        CP_IDPayload.setEmail(self._authorized_email)
        self._socket.sendto(GenvexPacket.build_packet(self._client_id, self._server_id, GenvexPacketType.U_CONNECT, 0, [IPXPayload, CP_IDPayload]), (self._device_ip, self._device_port))

    async def waitForConnection(self):
        """Wait for connection to be tried"""
        connectionTimeout = time.time() + 3
        while self._connection_error is False and self._is_connected is False:
            if time.time() > connectionTimeout:
                self._connection_error = GenvexNabtoConnectionErrorType.TIMEOUT                
                connectionTimeout = None
            await asyncio.sleep(0.2)

    async def waitForDiscovery(self):
        """Wait for discovery of ip to be done"""
        discoveryTimeout = time.time() + 3
        while True:
            if self._device_id in self._discovered_devices and self._device_ip is not None:
                return True
            if time.time() > discoveryTimeout:
                return False
            await asyncio.sleep(0.2)

    async def waitForData(self):
        """Wait for data to be available"""
        dataTimeout = time.time() + 12
        while True:
            if self._model_adapter is not None:
                if self._model_adapter.hasValue(GenvexNabtoDatapointKey.TEMP_SUPPLY) and self._model_adapter.hasValue(GenvexNabtoSetpointKey.TEMP_SETPOINT):
                    return True
            if time.time() > dataTimeout:
                return False
            await asyncio.sleep(0.2)

    def providesValue(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey):
        if self._model_adapter is None:
            return False
        return self._model_adapter.providesValue(key)

    def hasValue(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey):
        if self._model_adapter is None:
            return False
        return self._model_adapter.hasValue(key)
    
    def getValue(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey):
        if self._model_adapter is None:
            return False
        return self._model_adapter.getValue(key)
    
    def getSetpointMinValue(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey):
        if self._model_adapter is None:
            return False
        return self._model_adapter.getMinValue(key)
    
    def getSetpointMaxValue(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey):
        if self._model_adapter is None:
            return False
        return self._model_adapter.getMaxValue(key)
    
    def getSetpointStep(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey):
        if self._model_adapter is None:
            return False
        return self._model_adapter.getSetpointStep(key)
    
    def registerUpdateHandler(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey, updateMethod: Callable[[int, int], None]):
        if self._model_adapter is not None:
            self._model_adapter.registerUpdateHandler(key, updateMethod)

    def notifyAllUpdateHandlers(self):
        if self._model_adapter is not None:
            self._model_adapter.notifyAllUpdateHandlers()

    def processPingPayload(self, payload):
        self._device_number = int.from_bytes(payload[4:8], 'big')
        self._device_model = int.from_bytes(payload[8:12], 'big')
        self._slavedevice_number = int.from_bytes(payload[16:20], 'big')
        self._slavedevice_model = int.from_bytes(payload[20:24], 'big')
        print(f"Got model: {self._device_model} with device number: {self._device_number}, slavedevice number: {self._slavedevice_number} and slavedevice model: {self._slavedevice_model}")
        if GenvexNabtoModelAdapter.providesModel(self._device_model, self._device_number, self._slavedevice_number, self._slavedevice_model):
            self._is_connected = True
            print(f"Going to load model")
            self._model_adapter = GenvexNabtoModelAdapter(self._device_model, self._device_number, self._slavedevice_number, self._slavedevice_model)
            print(f"Loaded model for {self._model_adapter.getModelName()}")
            self.sendDataStateRequest(100)
            self.sendSetpointStateRequest(200)
        else:
            print(f"No model available")
            self._connection_error = GenvexNabtoConnectionErrorType.UNSUPPORTED_MODEL

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
                if deviceId not in self._discovered_devices:
                    self._discovered_devices[deviceId] = address
            if deviceId == self._device_id:
                self._device_ip = address[0]
            return
        if message[0:4] != self._client_id: # Not a packet intented for us
            return
        self._last_responce = time.time()
        packetType = message[8].to_bytes(1, 'big')
        if (packetType == GenvexPacketType.U_CONNECT):
            print("U_CONNECT responce packet")
            if (message[20:24] == b'\x00\x00\x00\x01'):
                self._server_id = message[24:28]
                print('Connected, pinging to get model number')
                if not self._is_connected:
                    self.sendPing()
            else:
                print("Received unsucessfull response")
                self._connection_error = GenvexNabtoConnectionErrorType.AUTHENTICATION_ERROR

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
                    if self._model_adapter is not None:
                        self._model_adapter.parseDataResponce(sequenceId, payload)
                    if sequenceId == 100:                        
                        self._last_dataupdate = time.time()
                    if sequenceId == 200:                        
                        self._last_setpointupdate = time.time()
            else:
                print("Not an interresting data packet.")
        else:
            print("Unknown packet type. Ignoring")

    def sendPing(self):
        PingCmd = GenvexCommandPing()
        Payload = GenvexPayloadCrypt()
        Payload.setData(PingCmd.buildCommand())
        self._socket.sendto(GenvexPacket().build_packet(self._client_id, self._server_id, GenvexPacketType.DATA, 50, [Payload]), (self._device_ip, self._device_port))

    def sendDataStateRequest(self, sequenceId):
        if self._model_adapter is None:
            return
        datalist = self._model_adapter.getDatapointRequestList(sequenceId)
        if datalist is False:
            return
        Payload = GenvexPayloadCrypt()
        Payload.setData(GenvexCommandDatapointReadList.buildCommand(datalist))
        self._socket.sendto(GenvexPacket().build_packet(self._client_id, self._server_id, GenvexPacketType.DATA, sequenceId, [Payload]), (self._device_ip, self._device_port))

    def sendSetpointStateRequest(self, sequenceId):
        Payload = GenvexPayloadCrypt()
        datalist = self._model_adapter.getSetpointRequestList(sequenceId)
        if datalist is False:
            return
        Payload.setData(GenvexCommandSetpointReadList.buildCommand(datalist))
        self._socket.sendto(GenvexPacket().build_packet(self._client_id, self._server_id, GenvexPacketType.DATA, sequenceId, [Payload]), (self._device_ip, self._device_port))

    def setSetpoint(self, setpointKey: GenvexNabtoSetpointKey, newValue) -> bool:
        if self._model_adapter is None:
            return False
        if self._model_adapter.providesValue(setpointKey) is False:
            return False
        setpointData = self._model_adapter._loadedModel._setpoints[setpointKey]
        newValue = int((newValue * setpointData["divider"]) - setpointData['offset'])
        if newValue < setpointData['min'] or newValue > setpointData['max']:
            return False
        Payload = GenvexPayloadCrypt()
        Payload.setData(GenvexCommandSetpointWriteList.buildCommand([(setpointData['write_obj'], setpointData['write_address'], newValue)]))
        self._socket.sendto(GenvexPacket().build_packet(self._client_id, self._server_id, GenvexPacketType.DATA, 3, [Payload]), (self._device_ip, self._device_port))
        self._last_dataupdate = time.time() - DATAPOINT_UPDATEINTERVAL + 1 # Ensure updates are check for next thread loop.
        self._last_setpointupdate = time.time() - SETPOINT_UPDATEINTERVAL + 1

    def handleRecieve(self):
        try:
            message, address = self._socket.recvfrom(SOCKET_MAXSIZE)
            if (len(message) < 16): # Not a valid packet
                return 
            self.processReceivedMessage(message, address)
        except socket.timeout:  
            return

    def receiveThread(self):
        while self._listen_thread_open:
            self.handleRecieve()          
            if self._is_connected:
                if time.time() - self._last_dataupdate > DATAPOINT_UPDATEINTERVAL:
                    print("Sending data request..")
                    self.sendDataStateRequest(100)
                if time.time() - self._last_setpointupdate > SETPOINT_UPDATEINTERVAL:                    
                    self.sendSetpointStateRequest(200)
                if time.time() - self._last_responce > SECONDS_UNTILRECONNECT:
                    self.connectToDevice()
                    
