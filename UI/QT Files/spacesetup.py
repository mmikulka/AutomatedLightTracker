# Form implementation generated from reading ui file 'Setup Space.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SetupSpace(object):
    def setupUi(self, SetupSpace):
        SetupSpace.setObjectName("SetupSpace")
        SetupSpace.resize(655, 515)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SetupSpace)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(SetupSpace)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label.mousePressEvent = self.getPos
        self.verticalLayout_3.addWidget(self.label)
        self.mouseLocal = QtWidgets.QLabel(SetupSpace)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mouseLocal.sizePolicy().hasHeightForWidth())
        self.mouseLocal.setSizePolicy(sizePolicy)
        self.mouseLocal.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.mouseLocal)
        self.findImage = QtWidgets.QPushButton(SetupSpace)
        self.findImage.setObjectName("findImage")
        self.verticalLayout_3.addWidget(self.findImage)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.marker1x = QtWidgets.QLineEdit(SetupSpace)
        self.marker1x.setObjectName("marker1x")
        self.gridLayout_2.addWidget(self.marker1x, 1, 2, 1, 1)
        self.marker1 = QtWidgets.QRadioButton(SetupSpace)
        self.marker1.setObjectName("marker1")
        self.gridLayout_2.addWidget(self.marker1, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(SetupSpace)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.height = QtWidgets.QLineEdit(SetupSpace)
        self.height.setObjectName("height")
        self.gridLayout.addWidget(self.height, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(SetupSpace)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(SetupSpace)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.width = QtWidgets.QLineEdit(SetupSpace)
        self.width.setObjectName("width")
        self.gridLayout.addWidget(self.width, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 4, 5, 1)
        self.marker2x = QtWidgets.QLineEdit(SetupSpace)
        self.marker2x.setObjectName("marker2x")
        self.gridLayout_2.addWidget(self.marker2x, 2, 2, 1, 1)
        self.marker2 = QtWidgets.QRadioButton(SetupSpace)
        self.marker2.setObjectName("marker2")
        self.gridLayout_2.addWidget(self.marker2, 2, 0, 1, 1)
        self.marker3 = QtWidgets.QRadioButton(SetupSpace)
        self.marker3.setObjectName("marker3")
        self.gridLayout_2.addWidget(self.marker3, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(SetupSpace)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.marker3x = QtWidgets.QLineEdit(SetupSpace)
        self.marker3x.setObjectName("marker3x")
        self.gridLayout_2.addWidget(self.marker3x, 3, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.marker4 = QtWidgets.QRadioButton(SetupSpace)
        self.marker4.setObjectName("marker4")
        self.verticalLayout.addWidget(self.marker4)
        self.gridLayout_2.addLayout(self.verticalLayout, 4, 0, 1, 1)
        self.marker4x = QtWidgets.QLineEdit(SetupSpace)
        self.marker4x.setObjectName("marker4x")
        self.gridLayout_2.addWidget(self.marker4x, 4, 2, 1, 1)
        self.marker1y = QtWidgets.QLineEdit(SetupSpace)
        self.marker1y.setObjectName("marker1y")
        self.gridLayout_2.addWidget(self.marker1y, 1, 3, 1, 1)
        self.marker2y = QtWidgets.QLineEdit(SetupSpace)
        self.marker2y.setObjectName("marker2y")
        self.gridLayout_2.addWidget(self.marker2y, 2, 3, 1, 1)
        self.marker3y = QtWidgets.QLineEdit(SetupSpace)
        self.marker3y.setObjectName("marker3y")
        self.gridLayout_2.addWidget(self.marker3y, 3, 3, 1, 1)
        self.marker4y = QtWidgets.QLineEdit(SetupSpace)
        self.marker4y.setObjectName("marker4y")
        self.gridLayout_2.addWidget(self.marker4y, 4, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(SetupSpace)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(SetupSpace)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.Save = QtWidgets.QPushButton(SetupSpace)
        self.Save.setObjectName("Save")
        self.verticalLayout_3.addWidget(self.Save)

        self.retranslateUi(SetupSpace)
        QtCore.QMetaObject.connectSlotsByName(SetupSpace)

    def retranslateUi(self, SetupSpace):
        _translate = QtCore.QCoreApplication.translate
        SetupSpace.setWindowTitle(_translate("SetupSpace", "Space Setup"))
        self.label.setText(_translate("SetupSpace", "TextLabel"))
        self.mouseLocal.setText(_translate("SetupSpace", "X: Y:"))
        self.findImage.setText(_translate("SetupSpace", "Select Image"))
        self.marker1.setText(_translate("SetupSpace", "Marker 1"))
        self.label_2.setText(_translate("SetupSpace", "Height/Width of Final Square"))
        self.label_5.setText(_translate("SetupSpace", "Width"))
        self.label_4.setText(_translate("SetupSpace", "Height"))
        self.marker2.setText(_translate("SetupSpace", "Marker 2"))
        self.marker3.setText(_translate("SetupSpace", "Marker 3"))
        self.label_7.setText(_translate("SetupSpace", "Active Marker"))
        self.marker4.setText(_translate("SetupSpace", "Marker 4"))
        self.label_8.setText(_translate("SetupSpace", "Pixel Location X"))
        self.label_9.setText(_translate("SetupSpace", "Pixel location Y"))
        self.Save.setText(_translate("SetupSpace", "Save"))


    def getPos(self, event):
        x = event.pos().x()
        y = event.pos().y()
        print(x)
        print(y)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SetupSpace = QtWidgets.QDialog()
    ui = Ui_SetupSpace()
    ui.setupUi(SetupSpace)
    SetupSpace.show()
    sys.exit(app.exec())
