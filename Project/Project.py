import Tracker.Tracker
from Fixtures.Fixtures import Fixture
from Fixtures.SACN import SACN
from Space.space import Space
import socket
import Camera.CameraCalibration


class Project:
    def __init__(self):
        self.lights = [Fixture((3, 3, 20), 37, 0, 2, 43, 44, 1, 540, 270, "Solaspot")]
        self.sacn = SACN(socket.gethostbyname(socket.gethostname()))
        self.space = Space()

    def loadSettings(self):
        pass

    def updateSpace(self, newSpace:Space):
        self.space = newSpace

    def trackSubject(self, outputs, subjectID, fixtureNumbers=[1]): #need to change after fixture tests
        if fixtureNumbers is not None:
            x, y = self.getSubjectPos(outputs, subjectID)
            x, y = self.space.getXYCoordinates((x, y))
            for fixtureNumber in fixtureNumbers:
                dmxUpdates = self.lights[fixtureNumber].focusLight(x, y)
                self.sacn.updateFixtureValues(self.lights[fixtureNumber].fixtureAddr(), dmxUpdates)

    def getSubjectPos(self, data, subject):
        # search through data to find index of subject
        subjectIndex = -1
        for i, item in enumerate(data):
            if item[4] == subject:
                subjectIndex = i
        # take x1 + x2 and y2 this will be the position of the person
        x = data[subjectIndex][0] - data[subjectIndex][2]
        y = data[subjectIndex][3]
        return x, y

    def addLight(self, position:list, instensityAddr:int, pandAddr: int, tiltAddr: int, numAddr:int,
                 universe:int, fixtureAddr:int, totalPanDeg:float, totalTiltDeg:float, fixName="N/A"):
        self.lights.append(Fixture(position, instensityAddr, pandAddr, tiltAddr, numAddr, universe, fixtureAddr,
                                   totalPanDeg, totalTiltDeg, fixName))


    def removeLight(self, fixNumber:int):
        del self.lights[fixNumber]

    def adjustLightPosition(self, fixNumber:int, position:list):
        self.lights[fixNumber].position(position)

    def updateArtnetIP(self, ip):
        self.sacn.blackout()
        del self.sacn
        self.sacn(ip)
        self.start()
