import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QFileDialog
from PyQt6.uic import loadUi

class ArtnetWindow(QDialog):
    def __init__(self):
        super(ArtnetWindow, self).__init__()
        loadUi('UI/QT Files/Artnet Setup.ui', self)
