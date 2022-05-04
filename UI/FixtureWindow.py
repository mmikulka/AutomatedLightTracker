from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QTableView, QVBoxLayout
from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6 import QtCore
from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.uic import loadUi
from Fixtures.Fixtures import Fixture
import sys


class FixtureWindow(QWidget):
    closing = pyqtSignal()
    newFixtureList = pyqtSignal(object)

    def setupUi(self, fixtures):
        self.resize(640, 480)
        self.setStyleSheet("QPushButton{\n"
                           "border-radius: 8px;\n"
                           "background-color: rgb(161, 161, 161);\n"
                           "}")

        self.fixtures = fixtures

        #widget
        self.fixtureTable = QtWidgets.QTableView()
        self.editFixture = QtWidgets.QPushButton("editFixture", clicked=self.editFixture)
        self.editFixture.setMinimumSize(QtCore.QSize(0, 20))
        self.addFixture = QtWidgets.QPushButton("Add Fixture", clicked=self.addFixture)
        self.addFixture.setMinimumSize(QtCore.QSize(0, 20))
        self.removeFixtureBtn = QtWidgets.QPushButton("removeFixture", clicked=self.removeFixture)
        self.removeFixtureBtn.setMinimumSize(QtCore.QSize(0, 20))
        self.sACN = QtWidgets.QPushButton("sACN", clicked=self.updatesACN)
        self.sACN.setMinimumSize(QtCore.QSize(0, 20))
        self.closeBtn = QtWidgets.QPushButton("CloseBtn", clicked=self.closeWindow)
        self.closeBtn.setMinimumSize(QtCore.QSize(0, 20))

        #layout
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.fixtureTable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.editFixture)
        self.horizontalLayout.addWidget(self.addFixture)
        self.horizontalLayout.addWidget(self.removeFixtureBtn)
        self.horizontalLayout.addWidget(self.sACN)
        self.horizontalLayout.addWidget(self.closeBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.setLayout(self.verticalLayout)

        # convert fixture list to 2D list to setup fixture table
        fixtureList = []
        for fixture in fixtures:
            fixtureList.append(fixture.asList())
        fixtureModel = qtFixtureTable(fixtureList)
        self.fixtureTable.setModel(fixtureModel)

    def editFixture(self):
        pass #implemented later

    def addFixture(self):
        #open fixture edit window
        self.fixtureEditWindow = FixtureEditorWindow()
        self.fixtureEditWindow.show()
        #take fixture objecte add it to fixture list
        self.fixtureEditWindow.newFixture.connect(self.addFixToList)

    def addFixToList(self, fixture):
        self.fixtures.append(fixture)

    def removeFixture(self):
        pass

    def updatesACN(self):
        pass

    def closeWindow(self):
        self.closing.emit()
        self.newFixtureList.emit(self.fixtures)
        self.close()


# Class that takes care of creating the table model used by the Table view of Fixture window
class qtFixtureTable(QAbstractTableModel):
    def __init__(self, data, *args):
        super(qtFixtureTable, self).__init__()
        self._data = data

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
                return self._data[index.row()][index.column()]

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            try:
                value = int(value)
            except ValueError:
                return False
            self._data[index.row(), index.column()] = value
            return True
        return False

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            headers = ["Fixture Name", "X Postition", "Y Position", "Z Position", "Intensity Offset", "Pan Offset",
                       "Tilt Offset",
                       "# Addresses", "Universe", "Fixture Address", "Pan Degrees", "Tilt Degrees"]

            if orientation == Qt.Orientation.Horizontal:
                return headers[section]
            if orientation == Qt.Orientation.Vertical:
                return section + 1

    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable


class FixtureEditorWindow(QDialog):
    newFixture = pyqtSignal(object)

    def __init__(self, fixture=None):
        super(FixtureEditorWindow, self).__init__()
        loadUi('UI/QT Files/fixture Setup.ui', self)
        # all boxes should be empty
        self.saveButton.clicked.connect(self.saveFixture)
        self.cancelButton.clicked.connect(self.close)


    def addFixtureInfo(self, fixture):
        self.FixtureName.setText(fixture.fixtureName)
        self.zPos.setText(fixture.position[2])
        self.zRot.setText('0')
        self.xPos.setText(fixture.position[0])
        self.xRot.setText('0')
        self.yPos.setText(fixture.position[1])
        self.yRot.setText('0')
        self.totalNumAddresses.setText(fixture.totalNumAddr())
        self.startAddress.setText(fixture.fixtureAddr)
        self.Universe.setText(fixture.universe)
        self.panOffset.setText(fixture.panOffset)
        self.tiltOffset.setText(fixture.tiltOffset)
        self.intensityOffset.setText(fixture.intensityOffset)

        # self.manufacturer
        # self.FixtureName
        # self.zPos
        # self.zRot
        # self.xPos
        # self.xRot
        # self.yPos
        # self.yRot
        # self.totalNumAddresses
        # self.startAddress
        # self.Universe
        # self.panOffset
        # self.tiltOffset
        # self.intensityOffset

    def saveFixture(self):
        fixName = self.FixtureName.text()
        zpos = self.zPos.text()
        zRot = self.zRot.text()
        xPos = self.xPos.text()
        xRot = self.xRot.text()
        yPos = self.yPos.text()
        yRot = self.yRot.text()
        numAddr = self.totalNumAddresses.text()
        startAddr = self.startAddr.text()
        universe = self.Universe.text()
        panOff = self.panOffset.text()
        tiltOff = self.tiltOffset.text()
        intensOff = self.intensityOffset.text()
        print(zRot)


data = Fixture((0, 0, 28), 37, 0, 2, 43, 1, 44, 540, 270, "Solaspot")


def main(args):
    app = QApplication(args)
    window = FixtureWindow()
    window.setupUi([data])
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main(sys.argv)
