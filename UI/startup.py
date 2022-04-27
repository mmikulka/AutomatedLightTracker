import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt6.uic import loadUi
import UI.CameraCalibration
import UI.ProjectWindow
from UI.SpaceSetup import SpaceSetup


class StartUp(QDialog):
    def __init__(self):
        super(StartUp, self).__init__()
        loadUi('UI/QT Files/Startup Window.ui', self)
        self.openProject.clicked.connect(self.browsefiles)
        self.newProject.clicked.connect(self.newproject)
        self.calibrateCamera.clicked.connect(self.calibratecamera)

    def browsefiles(self):
        fname = QFileDialog.getOpenFileNames(self, "open file", 'C:/Users/mattm/OneDrive - CSULB/School/Final Project/Automated Light Tracker')
        #self.fileName.setText(fname[0][0])

    #open main window
    def newproject(self):
        self.projectWindow = UI.ProjectWindow.ProjectWindow()
        self.spaceSetup = SpaceSetup()
        self.hide()
        self.spaceSetup.show()
        self.spaceWindow.setupSpace.connect(self.saveSpace)
        # self.projectWindow.show()

    def saveSpace(self, newSpace):
        pass



    def calibratecamera(self):
        self.camcalibration = UI.CameraCalibration.CameraCalibration()
        self.camcalibration.show()



# This will probably be done in a different file
# app = QApplication(sys.argv)
# camCalibration = CameraCalibration()
# widget = QtWidgets.QStackedWidget()
# widget.addWidget(camCalibration)
# widget.show()
# sys.exit(app.exec())