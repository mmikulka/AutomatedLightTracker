from PyQt6.QtWidgets import QDialog, QFileDialog
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from Space.space import Space
import numpy as np
import cv2


class SpaceSetup(QDialog):
    setupSpace = pyqtSignal(object)

    def __init__(self):
        super(SpaceSetup, self).__init__()
        loadUi('UI/QT Files/Setup Space.ui', self)
        self.space = Space()

        self.image = None

        self.label.mousePressEvent = self.getPos

        self.findImage.clicked.connect(self.imageSearch)

        self.save.clicked.connect(self.closeWindow)

    def imageSearch(self):
        fname = QFileDialog.getOpenFileName(self, "open Image",
                                            'C:', "ImageFiles(*.png *.jpg *.bmp)")

        pixmap = QPixmap(fname[0])
        self.image = cv2.imread(fname[0])
        self.label.setPixmap(pixmap.scaled(640, 480))
        self.marker1.setChecked(True)

    def getPos(self, event):
        x = event.position().x()
        y = event.position().y()
        self.mouseLocal.setText("x: %d /ty: %d)" % (x, y))
        #find what radial button is active
        if self.marker1.isChecked():
            self.marker1x.setText(str(x))
            self.marker1y.setText(str(y))
            self.marker2.setChecked(True)
        elif self.marker2.isChecked():
            self.marker2x.setText(str(x))
            self.marker2y.setText(str(y))
            self.marker3.setChecked(True)
        elif self.marker3.isChecked():
            self.marker3x.setText(str(x))
            self.marker3y.setText(str(y))
            self.marker4.setChecked(True)
        elif self.marker4.isChecked():
            self.marker4x.setText(str(x))
            self.marker4y.setText(str(y))
            self.marker1.setChecked(True)

    def spaceCalculations(self):
        ur = (float(self.marker1x.text()), float(self.marker1y.text()))
        dr = (float(self.marker2x.text()), float(self.marker2y.text()))
        dl = (float(self.marker3x.text()), float(self.marker3y.text()))
        ul = (float(self.marker4x.text()), float(self.marker4y.text()))
        cornerPts = np.array([ur, dr, dl, ul])
        self.space.calcBirdsEye(self.image, cornerPts, float(self.height.text()), float(self.width.text()))

    def closeWindow(self):
        # try:
        self.spaceCalculations()
        # except:
        #     print("Space not setup")
        if self.space.setup:
            self.setupSpace.emit(self.space)
        self.close()
