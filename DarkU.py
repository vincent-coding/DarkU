# DarkU
# Created by vincent-coding
# Licences : GPL-3.0

# !usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, re, calendar, time, requests
from sys import platform

sys.dont_write_bytecode = True

if sys.version_info < (3, 8):
    sys.exit('This program only runs on Python 3.8')


# Import Module
try:
    from assets.color import color
except:
    sys.exit('The color.py file located in the assets folder is missing.')

try:
    from PyQt5 import QtWidgets, QtGui
    from PyQt5.QtWidgets import QMessageBox
except:
    sys.exit(color.red + "The PyQt5 module is missing.")

try:
    from pypresence import Presence
    imported = True
except:
    imported = False

try:
    from assets.tcpgecko import TCPGecko
except:
    sys.exit(color.red + "The local TCPGecko module could not be imported. Please check that it exists in the assets folder.")

try:
    import assets.gui as gui
except:
    sys.exit(color.red + "The gui.py file in the assets folder is missing!")

sep = os.path.sep

# Variables
version  = "2.3"
error    = 0
filePath = os.getcwd() + sep + "assets" + sep + "config.darku"
title    = "DarkU v" + version


EUR_554  = 0x105DD2A8
EUR_55X  = 0x105DD0A8
ALL_55X  = 0x105DD0A4

TITLE_ID_EUR = 0x0005001010040200
TITLE_ID_USA = 0x0005001010040100
TITLE_ID_JAP = 0x0005001010040000


# Discord RPC
if imported == True:
    try:
        RPC = Presence('694535619312877598')
        RPC.connect()
        RPC.update(
            state       = "Created by VCoding",
            details     = "Uses DarkU v" + version,
            start       = calendar.timegm(time.gmtime()),
            end         = None,
            large_image = "icons",
            large_text  = "DarkU v" + version,
            small_image = "copy",
            small_text  = "Created by VCoding",
            party_id = None, party_size = None
        )
    except:
        error = 1


def checkNumberAndDotOnly(strg, search=re.compile(r'[^0-9.]').search):
    return not bool(search(strg))

def checkIP(ip):
    pieces = ip.split('.')
    if len(pieces) != 4: return False
    try: return all(0<=int(p)<256 for p in pieces)
    except ValueError: return False


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.connected = False

        if os.path.exists(filePath):
            if os.path.isfile(filePath):
                f = open(filePath, "r+")
                self.ui.ipTextBox.setText(f.read())
                f.close()
            else:
                os.removedirs(filePath)

        self.ui.connectionButton.clicked.connect(self.connection)
        self.ui.disconnectionButton.clicked.connect(self.disconnection)
        self.ui.regionComboBox.currentTextChanged.connect(self.regionChanged)
        #self.ui.getCurrentColorButton.clicked.connect(self.getCurrentColor)
        self.ui.applyButton.clicked.connect(self.applyColor)
        
        try:
            r = requests.get('https://raw.githubusercontent.com/vincent-coding/DarkU/2.X/lastVersion')
            if r.status_code == 200:
                lastVer = r.text.replace("\n", "")
                if lastVer != version:
                    self.ui.newVersionLabel.setText("<html><head/><body><p><a href=\"https://github.com/vincent-coding/DarkU/releases/latest\"><span style=\" text-decoration: underline; color:#3498db;\">New update available (" + lastVer + ")</span></a></p></body></html>")
                else:
                    self.ui.newVersionLabel.setText("")
        except:
            self.ui.newVersionLabel.setText("Cannot detect if an update has been released.")

    
    def closeEvent(self, event):
        if self.connected == True:
            closeWindowQuestion = QMessageBox.question(self, title, "You are always connected to your WiiU.\nAre you sure you want to continue?")
            if closeWindowQuestion == QMessageBox.Yes:
                try:
                    self.gecko.s.close()
                except:
                    error = 2
                event.accept()
            else:
                event.ignore()

    def connection(self):
        wiiu_ip = self.ui.ipTextBox.text()
        if not wiiu_ip == "":
            if checkNumberAndDotOnly(wiiu_ip):
                if checkIP(wiiu_ip):
                    try:
                        self.gecko = TCPGecko(wiiu_ip)
                    except:
                        return QMessageBox.critical(self, title, "The connection to the console failed!")
                    
                    if not os.path.exists(filePath):
                        f = open(filePath, "w+")
                        f.write(wiiu_ip)
                        f.close()
                    else:
                        if not os.path.isfile(filePath):
                            os.removedirs(filePath)
                        f = open(filePath, "w+")
                        f.write(wiiu_ip)
                        f.close()
                    
                    self.ui.ipTextBox.setEnabled(False)
                    self.ui.connectionButton.setEnabled(False)
                    self.ui.disconnectionButton.setEnabled(True)
                    self.ui.regionComboBox.setEnabled(True)
                    self.connected = True

                    QMessageBox.information(self, title, "The connection to " + wiiu_ip + " was a success!")

                else:
                    QMessageBox.critical(self, title, "The IP address entered does not have a valid structure.\nExample: 127.0.0.1\nYour entry: " + wiiu_ip)
            else:
                QMessageBox.critical(self, title, "An ip address consists only of numbers and dots!\nExample: 127.0.0.1\nYour entry: " + wiiu_ip)
        else:
            QMessageBox.critical(self, title, "Please enter the ip address of your WiiU!")

    def disconnection(self):
        if self.connected == True:
            try:
                self.gecko.s.close()
                self.connected = False
                self.ui.ipTextBox.setEnabled(True)
                self.ui.connectionButton.setEnabled(True)
                self.ui.disconnectionButton.setEnabled(False)
                self.ui.regionComboBox.setEnabled(False)
                self.ui.versionComboBox.setEnabled(False)
                self.ui.colorComboBox.setEnabled(False)
                self.ui.applyButton.setEnabled(False)
                self.ui.getCurrentColorButton.setEnabled(False)
                self.ui.regionComboBox.setCurrentIndex(0)
                self.ui.versionComboBox.setCurrentIndex(0)
                self.ui.colorComboBox.setCurrentIndex(0)
                QMessageBox.information(self, title, "Disconnection of the console was successful!")
            except:
                QMessageBox.critical(self, title, "An error occurred when disconnecting the console!")

    def regionChanged(self):
        regionComboBox = self.ui.regionComboBox.currentIndex()
        if regionComboBox == 0:
            self.ui.versionComboBox.setEnabled(False)
            self.ui.colorComboBox.setEnabled(False)
            self.ui.applyButton.setEnabled(False)
            self.ui.getCurrentColorButton.setEnabled(False)
            #QMessageBox.critical(self, title, "Please select a region!")
        elif regionComboBox == 1 or regionComboBox == 2:
            if regionComboBox == 1:
                self.region = "EUR"
            elif regionComboBox == 2:
                self.region = "JAP-USA"
            else:
                return QMessageBox.critical(self, title, "An error has occurred!")
            self.ui.versionComboBox.setEnabled(True)
            self.ui.colorComboBox.setEnabled(True)
            self.ui.applyButton.setEnabled(True)
            #self.ui.getCurrentColorButton.setEnabled(True)
            self.ui.getCurrentColorButton.setEnabled(False)

    def applyColor(self):
        if self.ui.regionComboBox.currentIndex() == 0:
            return QMessageBox.critical(self, title, "An unknown error has occurred!")
        elif self.ui.versionComboBox.currentIndex() == 0:
            return QMessageBox.critical(self, title, "Please choose a version!")
        elif self.ui.colorComboBox.currentIndex() == 0:
            return QMessageBox.critical(self, title, "Please choose a colour!")
        
        if self.ui.regionComboBox.currentIndex() == 1:
            if self.ui.versionComboBox.currentIndex() == 1:
                usedRAM = EUR_55X
            elif self.ui.versionComboBox.currentIndex() == 2:
                usedRAM = EUR_554
            else:
                return QMessageBox.critical(self, title, "An unknown error has occurred!")
        elif self.ui.regionComboBox.currentIndex() == 2:
            usedRAM = ALL_55X

        color_index = self.ui.colorComboBox.currentIndex()
        if color_index == 1:
            self.gecko.pokemem(usedRAM, 0x3f800000)
            return QMessageBox.information(self, title, "The colour has been changed to: " + self.ui.colorComboBox.currentText())
        if color_index == 2:
            self.gecko.pokemem(usedRAM, 0x40000000)
            return QMessageBox.information(self, title, "The colour has been changed to: " + self.ui.colorComboBox.currentText())
        if color_index == 3:
            self.gecko.pokemem(usedRAM, 0x3E800000)
            return QMessageBox.information(self, title, "The colour has been changed to: " + self.ui.colorComboBox.currentText())
        if color_index == 4:
            self.gecko.pokemem(usedRAM, 0x3D800000)
            return QMessageBox.information(self, title, "The colour has been changed to: " + self.ui.colorComboBox.currentText())
        if color_index == 5:
            self.gecko.pokemem(usedRAM, 0x3C800000)
            return QMessageBox.information(self, title, "The colour has been changed to: " + self.ui.colorComboBox.currentText())
        if color_index == 6:
            self.gecko.pokemem(ram_55X, 0x3B800000)
            return QMessageBox.information(self, title, "The colour has been changed to: " + self.ui.colorComboBox.currentText())
        if color_index == 7:
            self.gecko.pokemem(usedRAM, 0x00000000)
            return QMessageBox.information(self, title, "The colour has been changed to: " + self.ui.colorComboBox.currentText())



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("DarkU v" + version)
    try:
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        window.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'assets' + os.path.sep + 'icons.png'))
    except:
        pass
    window.show()
    sys.exit(app.exec_())