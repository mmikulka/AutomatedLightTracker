from stupidArtnet import StupidArtnet
import time


class ArtNet:
    def __init__(self, target_ip='127.0.0.1', universe=0):
        self.anet = StupidArtnet(target_ip, universe, 512, 25, True, True)
        self.packet = bytearray(100)

    def start(self):
        self.anet.start()

    def stop(self):
        self.anet.stop()

    def updateAddressValue(self, addr, value):
        self.packet[addr - 1] = value

    def updatePacket(self):
        self.anet.set(self.packet)

    def blackout(self):
        self.anet.blackout()

    def flash(self):
        self.anet.flash_all()

    def __del__(self):
        self.anet.blackout()
        self.anet.stop()
        del self.anet

#Test for Artnet output
if __name__ == '__main__':
    anet = ArtNet('192.168.0.110')
    anet.start()
    anet.updateAddressValue(3, 255)
    anet.updateAddressValue(11, 255)
    anet.updateAddressValue(12, 255)
    anet.updateAddressValue(18, 128)
    anet.updateAddressValue(20, 128)
    anet.updateAddressValue(22, 128)
    anet.updatePacket()
    for i in range(100):
        anet.updateAddressValue(i, 255)
        anet.updatePacket()
        print(anet.anet)
        print(i)
        time.sleep(1)

