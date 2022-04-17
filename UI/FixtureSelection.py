from PyQt6.QtWidgets import QDialog, QFileDialog
from PyQt6.uic import loadUi

class FixtureSelectionWindow(QDialog):
    def __init__(self):
        super(FixtureSelectionWindow, self).__init__()
        loadUi('UI/QT Files/Fixture Assignment.ui', self)


#fname = QFileDialog.getOpenFileNames(self, "open file", 'C:/Users/mattm/OneDrive - CSULB/School/Final Project/Automated Light Tracker')