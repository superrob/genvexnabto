# GenvexNabto
Libary to locally interface with HVAC systems running Genvex Connect gateways. Usually those are only cloud accessible, however after lots of work i finally have a local solution ready.
This libary might also be able to be used on Nilan devices connected to a Nilan Gateway as the same company made that interface. However i do not have such a device to test for.

The libary is built to be used by my Home Assistant custom component and is currently in alpha. Expect things to change and break anything you might build around it.

### Supported controller models
|Controller         | Gateway requiured     | Supported       | Tested  |
|------------------:|:---------------------:|:---------------:|:-------:|
|Optima 250         | Yes, internet gateway | ✅              | ✅      |
|Optima 251         | Yes, internet gateway | ✅              | ✅      |
|Optima 260         | Yes, internet gateway | ✅              |         |
|Optima 270         | Built in              | ✅              | ✅     |
|Optima 301         | Yes, internet gateway | ✅              | ✅     |
|Optima 312         | Yes, internet gateway | ✅              |         |
|Optima 314         | Built in              | ✅              |         |
|Nilan CTS400       | Yes, nilan gateway    | ✅              | ✅     |
|Nilan CTS602       | Yes, nilan gateway    | ✅              | ✅     |
|Nilan CTS602 Light | Yes, nilan gateway    | ✅              |         |
|Nilan CTS602 Geo   | Yes, nilan gateway    | ✅              |         |

For any controllers that requires a gateway, it is mandetory that the device supports Modbus. Optima controllers delivered before 2014 might not have Modbus.

# How i got here
Genvex Connect and Nilan gateways both use the proprietary "Micro Nabto" protocol. Any mentions of it are very scarce online, with most official documentation being wiped from the internet after the companies release of "Nabto edge", which is highly incompatible with the older "Micro Nabto".

The usual connection flow is for the user to use the respective dedicathed app. The app loads a commically large 6MB+ binary client for Nabto communication. The binary is closed source and seems obfuscated to prevent easy "decompilation". 
This is also a huge issue as binaries are only available for Win32, Linux, Mac, Android and iOS. No generic linux ARM binaries are available and such using those to implement an Home Assistant custom component would exclude the most popular hosting devices, such as the Raspberry Pi.

The binary scans for any gateways by sending out a broadcast UDP packet. This packet either has a specific device identifier in it or a star (*) to request any gateway to respond.
Any available gateways will respond to the receiver with their unique identifier on the same UDP ip and port and the broadcast was sent.

The normal flow is then handled online, with the libary using a client certificate encrypted using the password supplied when first using the device. The flow unfurtunately is where i got stuck for a long time. 
The client requests a serverpeer id from the nabto server, which is propperly authenticated is sent back together with a NONCE and a server certificate. The client using the NONCE calculates a AES encryption key, which is later used to setup a direct local connection to the device.
Next the client sends a connection request to the nabto server. This request is encrypted using the server certificate public key and signed using the client certificate private key. The contents of this request is currently not known, as that would require extensive reverse engineering of the nabto client binary, and thus where i got stuck.

The server replies back, again encrypted. I am guessing the contents to be encrypted using the public RSA key from the client certificate. I have not looked into the contents of the reply, as i currently do not know the contents of the original request.
What is clear is that these packets sets up the communication on the local device where the encryption context for the connection is setup.

The client then connects locally to the device and is expected to provide all communication forwards in CRYPT payloads, encrypted using the AES keys which the server has set for the connection during the last two phases.
Lucklyli the Nabto binary has a lot of logging built in and actually displays the AES and HMAC keys during the connection request! 
Using that key i was able to decrypt and study the payloads, which matched the "Micro Nabto" device sourcecode i had found a while ago on their github.
Their device sourcecode contains details on the procotol used and allowed me to decode and even build my own packets.

However without understanding the client connection request sent to the server, this is not usefull.

That was until i tried using an extremely old version of the Nabto client binary. Which to my surprice talked with the device using cleartext CRYPT payloads! I had seen in the device sourcecode that if a "isLocal" flag i set for the connection, that any encryption can be specified to be used. However i couldn't figure out how to set the flag.
However this old client binary connected to a different port on the device. To my surprise, using that UDP port instead of the one used by the newer client libary, it actually set the isLocal flag and allowed for unencrypted CRYPT payloads!

From here i only had to implement the "Micro Nabto" protocol in my own portable libary.
I have only been able to test the Optima 270 implementation as i only have an Genvex ventilation unit with the Optima 270 controller (Has the gateway built in). 
However i have tried implementing the older controllers which should in theory be compatible. I have also added the Nilan CTS400 controller as the gateway for Nilan is built by the same company and uses the same command structure.

# Obligatory statement
I am not personally or in any way responsible for any damages should you choose to use the libary. No warranty provided. 
