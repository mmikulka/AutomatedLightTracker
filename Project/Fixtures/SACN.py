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


