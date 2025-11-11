# GenvexNabto
Library for local interfacing with HVAC systems running Genvex Connect or Nilan gateways. These systems are only officially cloud-accessible, but after extensive development, a local solution is now available. 

### Supported controller models
|Controller         | Gateway required     | Supported       | Tested  |
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

For controllers that require a gateway, it is mandatory that the device supports Modbus. Note that Optima controllers delivered before 2014 may not have Modbus support.

# How the libary works
Both Genvex Connect and Nilan gateways use the proprietary "Micro Nabto" protocol. Information about this protocol is limited, with most official documentation being removed from the internet following the companies' release of "Nabto Edge," which is largely incompatible with the older "Micro Nabto."

Typically, users connect via a dedicated app. The app loads a large, 6MB+ closed-source binary client for Nabto communication. A major limitation is that the binary is only available for Win32, Linux, Mac, Android, and iOS. There are no generic Linux ARM binaries, meaning implementing a Home Assistant custom component with these binaries would exclude widely used platforms like the Raspberry Pi.

The binary scans for available gateways by broadcasting a UDP packet. This packet either includes a specific device identifier or a wildcard (*) to request a response from any gateway. Gateways that are available will reply with their unique identifier over the same UDP IP and port to which the broadcast was sent.

While the normal connection process is handled online, it is encrypted and obfuscated. Significant progress has been made in reverse-engineering the online flow, leading to the discovery of a local connection method.

The local connection flow allows for direct communication with compatible gateways, using the user's email as the password.

# Obligatory statement
The contributors are not responsible for any damages resulting from the use of this libary. No warranty is provided.
