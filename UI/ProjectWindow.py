import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi
import PyQt6.QtCore
from PyQt6.QtCore import *
import cv2
from Project.Project import Project
from Tracker.Tracker import Tracker
import UI.CameraCalibration
import UI.ArtnetWindow
import UI.FixtureSelection
import UI.SpaceSetup


class ProjectWindow(QMainWindow):
    def __init__(self):
        super(ProjectWindow, self).__init__()
        loadUi('UI/QT Files/mainWindow.ui', self)

        # setup subject selector dropdown menu
        self.subjectlist = [-1]
        self.subjectSelector.addItems(["None"])

        # setup camera selection dropdown
        self.cameraSelection.addItems(["01: USB Video"])

        # Project class creation
        self.currentProject = Project()

        # setup triggers
        self.actionCalibration.triggered.connect(self.calibrateCam)
        self.actionArtnet.triggered.connect(self.artnet)
        self.actionDMX.triggered.connect(self.DMX)
        self.selectLights.clicked.connect(self.fixtureSelection)
        self.spaceSetup.clicked.connect(self.setupSpaceWindow)

        # setup Camera View
        self.cameraViewThread = TrackerThread()
        self.cameraViewThread.start()
        self.cameraViewThread.imageUpdate.connect(self.ImageUpdateSlot)
        self.cameraViewThread.trackingData.connect(self.updateTracking)

    def updateTracking(self, data):
        self.updateSubjects(data)
        subjectToTrack = self.subjectSelector.currentText()
        if subjectToTrack != "None":
            subjectToTrack = int(subjectToTrack[9:])
            self.currentProject.trackSubject(data, subjectToTrack)

    def updateSubjects(self, data):
        if data is not None:
            newsubjects = []
            for row in data:
                newsubjects.append(row[4])
            for subject in self.subjectlist:
                if newsubjects.count(subject) == 0 and subject != -1:
                    self.subjectlist.remove(subject)
                    index = self.subjectSelector.findText("Subject: " + str(subject))
                    self.subjectSelector.removeItem(index)
            for subject in newsubjects:
                if self.subjectlist.count(subject) == 0:
                    self.subjectlist.append(subject)
                    self.subjectSelector.addItems(["Subject: " + str(subject)])
        else:
            self.subjectSelector.clear()
            self.subjectSelector.addItems(["None"])


    def ImageUpdateSlot(self, image):
        self.cameraView.setPixmap(QPixmap.fromImage(image))

    def saveSpace(self, space):
        self.currentProject.space = space

    def launch(self):
        self.show()
        self.w.show()

    def calibrateCam(self):
        self.camcalibration = UI.CameraCalibration.CameraCalibration()
        self.camcalibration.show()

    def cameraSelection(self):
        pass

    def artnet(self):
        self.artnet = UI.ArtnetWindow.ArtnetWindow()
        self.artnet.show()

    def DMX(self):
        pass

    def editFixtures(self):
        pass

    def selectLights(self):
        pass

    def fixtureSelection(self):
        self.fixtureSelection = UI.FixtureSelection.FixtureSelectionWindow()
        self.fixtureSelection.show()

    def setupSpaceWindow(self):
        self.spaceWindow = UI.SpaceSetup.SpaceSetup()
        self.spaceWindow.show()
        self.spaceWindow.setupSpace.connect(self.saveSpace)

    def saveSpace(self, space):
        self.currentProject.updateSpace(space)

class TrackerThread(QThread):
    imageUpdate = pyqtSignal(QImage)
    trackingData = pyqtSignal(object)

    def run(self):
        self.ThreadActive = True
        # capture = cv2.VideoCapture(0)
        # initialize tracking model
        yoloModel = "Tracker/yolov5/models/yolov5l.pt"
        deepsortModel = "osnet_x1_0"
        deepsortConfig = "Tracker/deep_sort/configs/deep_sort.yaml"
        source = '0'  # webcam
        classes = 0  # track humans only
        imgsz = [1920, 1280]
        device = 0
        tracker = Tracker(yoloModel, deepsortModel, deepsortConfig, source, classes, device, imgsz,
                          True)
        dataset = tracker.setup()

        while self.ThreadActive:
            for frame_idx, (path, img, im0s, vid_cap, s) in enumerate(dataset):
                img, outputs = tracker.detect(frame_idx, path, img, im0s, vid_cap, s, [0.0, 0.0, 0.0, 0.0], 0, "")

                FlippedImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0],
                                           QImage.Format.Format_RGB888)
                pic = convertToQtFormat.scaled(1088, 736, Qt.AspectRatioMode.KeepAspectRatio)
                print(outputs)
                self.imageUpdate.emit(pic)
                self.trackingData.emit(outputs)

    def stop(self):
        self.ThreadActive = False
        self.quit()
