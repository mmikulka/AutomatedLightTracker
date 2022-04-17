import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QFileDialog
from PyQt6.uic import loadUi


class CameraCalibration(QDialog):
    def __init__(self):
        super(CameraCalibration, self).__init__()
        loadUi('UI/QT Files/Cam Calibration.ui', self)
        self.browse.clicked.connect(self.browsefiles)

    def browsefiles(self):
        fname = QFileDialog.getOpenFileNames(self, "open file", 'C:/Users/mattm/OneDrive - CSULB/School/Final Project/Automated Light Tracker/UI')
        self.fileName.setText(fname[0][0])

