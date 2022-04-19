import numpy as np
# from SACN import SACN
import socket
import time

class Fixture:
    def __init__(self, position: list, intensityAddr: int, panAddr: int, tiltAddr: int, totalNumAddresses: int,
                 universe: int, fixtureAddr: int, totalPanDeg: float, totalTiltDeg: float, fixtureName="N/A"):
        self._pos = position
        self._intensity_offset = intensityAddr
        self._pan_offset = panAddr
        self._tilt_offset = tiltAddr
        self._fixtureName = fixtureName
        # self._num_addr = totalNumAddresses #try not using
        self._universe = universe
        self._fixtureAddr = fixtureAddr
        self._totalPanDeg = totalPanDeg  # pan can go between 0 and max
        self._totalTiltDeg = totalTiltDeg / 2  # straight down o tilt at 0.
        self._tilt = 0  # tilt starts straight downs
        self._pan = self._totalPanDeg / 2  # pan starts 1/2 way to max
        self._panVect = (position[0], position[1] + 1)
        self._dmx_vals = [0] * totalNumAddresses
        self._dmx_vals[self._pan_offset] = 128
        self._dmx_vals[self._tilt_offset] = 128
        self._dmx_vals[self._intensity_offset] = 255

        #for Solaspots
        self._dmx_vals[5] = 255
        self._dmx_vals[6] = 255
        self._dmx_vals[7] = 255
        self._dmx_vals[8] = 255
        self._dmx_vals[9] = 55
        self._dmx_vals[14] = 127
        self._dmx_vals[15] = 255
        self._dmx_vals[19] = 127
        self._dmx_vals[20] = 255
        self._dmx_vals[25] = 127
        self._dmx_vals[26] = 255
        self._dmx_vals[34] = 255
        self._dmx_vals[36] = 255
        self._dmx_vals[37] = 255
        self._dmx_vals[38] = 0
        self._dmx_vals[41] = 135


    def focusLight(self, x, y, z=5):
        # Tilt
        # convert x, y, z coordinates to vectors)
        self.__calc_tilt(x, y, z)
        # Pan
        self.__calc_pan(x, y)
        return self._dmx_vals

    def homeFixture(self):
        self._pan = self._totalpanDeg / 2
        self.tilt = 0
        self.panVect = (self._pos[0], self._pos[1] - 1)
        self.dmx_vals[self._pan_offset] = 128
        self.dmx_vals[self._tilt_offset] = 128

    @property
    def position(self):
        return self._pos

    @position.setter
    def position(self, position:list):
        self._pos = position

    @property
    def dmxVals(self):
        return self._dmx_vals

    @property
    def fixtureAddr(self):
        return self._fixtureAddr

    @fixtureAddr.setter
    def fixtureAddr(self, value):
        if value < 0 or value > 255 - len(self.dmxVals):
            raise ValueError("DMX address out of range")
        self._fixtureAddr = value

    @property
    def universe(self):
        return self._universe

    @universe.setter
    def universe(self, val):
        self._universe = val

    def dmxValues(self):
        return self._dmx_vals

    def __calc_tilt(self, x, y, z):
        vect1 = (0, 0, 5)
        vect2 = (x - self._pos[0], y - self._pos[1], self._pos[2] - z)
        # convert to unit vectors
        unitVect1 = vect1 / np.linalg.norm(vect1)
        unitVect2 = vect2 / np.linalg.norm(vect2)
        # find radian angle between the two vectors
        rad = np.arccos(np.clip(np.dot(unitVect1, unitVect2), -1.0, 1.0))
        # convert radians to degrees
        angle = np.rad2deg(rad)
        # convert degree to dmx value
        # print("current tilt: " + str(self._tilt))
        # print("angle calculated: " + str(angle))
        self._tilt = angle
        # print("new tilt: " + str(self._tilt))
        self._dmx_vals[self._tilt_offset] = self.__tilt_angle_to_dmx(self._tilt)

    def __calc_pan(self, x, y):
        cosTh = np.dot(self._panVect, (x, y))
        sinTh = np.cross(self._panVect, (x, y))
        angle = np.rad2deg(np.arctan2(sinTh, cosTh))
        self._pan = self._pan - angle
        self._panVect = (x, y)
        panChange = self.__pan_angle_to_dmx(angle)
        self._dmx_vals[self._pan_offset] += panChange

    # calculate the dmx value for specified angle
    def __pan_angle_to_dmx(self, angle):
        return int(angle * (255.0 / self._totalPanDeg))

    # calculate the dmx value for specified angle
    def __tilt_angle_to_dmx(self, angle):
        return int(angle * (128.0 / self._totalTiltDeg))


if __name__ == "__main__":
    lights = [Fixture((0, 0, 28), 37, 0, 2, 43, 1, 44, 540, 270, "Solaspot")]
    # self.sacn = SACN(socket.gethostbyname(socket.gethostname()))
    sacn = SACN(socket.gethostbyname(socket.gethostname()))
    sacn.updateFixtureValues(lights[0].fixtureAddr, lights[0].dmxValues())
    sacn.updatePacket()
    time.sleep(1)
    lights[0].focusLight(-10, 20, 5)
    sacn.updateFixtureValues(lights[0].fixtureAddr, lights[0].dmxValues())
    print(lights[0].dmxValues())
    sacn.updatePacket()
    time.sleep(1)
    lights[0].focusLight(-11, 20, 5)
    sacn.updateFixtureValues(lights[0].fixtureAddr, lights[0].dmxValues())
    print(lights[0].dmxValues())
    sacn.updatePacket()
    time.sleep(1)
    lights[0].focusLight(-10, 20, 5)
    sacn.updateFixtureValues(lights[0].fixtureAddr, lights[0].dmxValues())
    print(lights[0].dmxValues())
    sacn.updatePacket()
    time.sleep(1)
    lights[0].focusLight(-11, 20, 5)
    sacn.updateFixtureValues(lights[0].fixtureAddr, lights[0].dmxValues())
    print(lights[0].dmxValues())
    sacn.updatePacket()
    time.sleep(10)
    sacn.stop()