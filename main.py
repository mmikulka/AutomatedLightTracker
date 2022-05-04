from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog
import sys
import UI.startup
import UI.ProjectWindow
import UI.SpaceSetup

def main():
    app = QApplication(sys.argv)
    # startup = UI.startup.StartUp()
    startup = UI.ProjectWindow.ProjectWindow()
    # startup = UI.SpaceSetup.SpaceSetup()
    # startup.show()
    app.exec()


if "__main__" == __name__:
    main()
