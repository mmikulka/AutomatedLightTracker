import sacn
import time


class SACN:
    def __init__(self, deviceIP="127.0.0.1", multicast=True, target_ip='127.0.0.1', universe=3):
        self.deviceIP = deviceIP
        self.multicast = multicast
        self.targetIP = target_ip
        self.universe = universe
        self.packet = [0] * 512
        self.sender = sacn.sACNsender(deviceIP)
        self.sender.start()
        self.sender.activate_output(universe)
        self.sender[universe].multicast = multicast
        if not multicast:
            self.sender[universe].destination = target_ip

    def start(self):
        self.sender.start()

    def stop(self):
        self.sender.stop()

    def updateAddressValue(self, addr: int, value: int):
        self.packet[addr - 1] = value

    def updateFixtureValues(self, addr: int, values: list):
        for count, value in enumerate(values):
            self.packet[addr-1+count] = value

    def updatePacket(self):
        self.sender[self.universe].dmx_data = tuple(self.packet)

    def blackout(self):
        self.packet = [0] * 512
        self.sender[self.universe].dmx_data = tuple(self.packet)

    def flash(self):
        self.packet = [255] * 512
        self.sender[self.universe].dmx_data = tuple(self.packet)

    def __del__(self):
        self.blackout()
        self.stop()
        del self.sender


# Test for Artnet output
if __name__ == '__main__':
    stream = SACN("10.101.50.120")

    for i in range(100):
        stream.updateAddressValue(i, 255)
        stream.updatePacket()
        time.sleep(1)  # send the data for 10 seconds
    # sender = sacn.sACNsender("10.101.50.120")  # provide an IP-Address to bind to if you are using Windows and want to use multicast
    # sender.start()  # start the sending thread
    # sender.activate_output(1)  # start sending out data in the 1st universe
    # sender[1].multicast = True  # set multicast to True
    # # sender[1].destination = "192.168.1.20"  # or provide unicast information.
    # # Keep in mind that if multicast is on, unicast is not used
    # sender[1].dmx_data = (255, 255, 255, 255)  # some test DMX data

    stream.stop()  # do not forget to stop the sender

# Custom implementation Not currently working
# import socket
# import time
#
# data = [0]*638
#
# data = bytearray(data)
#
# #preamble Size
# data[0:2] = 0x00,0x10
#
# #postambleSize = "\x00\x00"
# data[2:4] = 0x00,0x00
#
# #acnPacketIdentifier = "ASC-E1.17\x00\x00\x00"
# data[4:16] = bytes("ASC-E1.17\x00\x00\x00", 'utf-8')
#
# #flagsAndLength = "\x72\x6e"
# data[16:18] = 0x72,0x6e
#
# #vector = "\x00\x00\x00\x04"
# data [18:22] = 0x00,0x00,0x00,0x04
#
# #CID = "Python CMD ACN  "
# #data[22:37] = bytes("ChamSys\xac\x11\x1f", 'utf-8')
# data[22:38] = 0x43,0x68,0x61,0x6d,0x53,0x79,0x40,0x00,0x80,0x00,0xac,0x11,0x1e,0x28,0x0,0x0
#
# #framingFlagsAndLength = "\x72\x58"
# data [38:40] = 0x72,0x58
#
# #framingVector = "\x00\x00\x00\x02"
# data[40:44] = 0x00,0x00,0x00,0x02
#
# #sourceName = "streamingACN transmission test - python to sACN".ljust(64, ' ')
# sourceName = "ChamSys MagicQ".ljust(64, '\x00')
# data[44:108] = bytes(sourceName, 'utf-8')
#
# #priority = "\x64"
# data[108] = 0x64
#
# #reservedWord = "\x00\x00"
# data[109:111] = 0,0
#
# #sequenceNumber = "\x00"
# data[111] = 0x7e
#
# #options = "\x00"
# data[112] = 0
#
# #universe = "\x00\x01"
# data[113:115] = 0x00,0x01
#
# #DMPFlagsAndLength = "\x72\x0b"
# data[115:117] = 0x72,0x0b
#
# #DMPvector = "\x02"
# data[117] = 0x02
#
# #addressDataType = "\xa1"
# data[118] = 0xa1
#
# #firstPropertyAddress = "\x00\x00"
# data[119:121] = 0x00,0x00
#
# #addressIncrement = "\x00\x01"
# data[121:123] = 0x00,0x01
#
# #propertyValueCount = "\x02\x01"
# data[123:125] = 0x02,0x01
#
# data[125] = 0x70
# data[136] = 0x80
#
# sacnSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #setups the UDP socket
# sacnSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sacnSocket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton('192.168.0.159'))
# sacnSocket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
# sacnSocket.bind(('192.168.0.159', 5568))
#
# while True:
#     sacnSocket.sendto(data, ('192.168.0.110', 5568))
#     if (data[111] == 255):
#         data[111] = 0
#         data[157] = 0
#     else:
#         data[111] += 1
#         data[157] += 1
#     print (data[111])
#     time.sleep(0.1)
