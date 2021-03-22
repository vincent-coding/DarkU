from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 340)
        MainWindow.setMinimumSize(QtCore.QSize(300, 340))
        MainWindow.setMaximumSize(QtCore.QSize(300, 340))
        MainWindow.setStyleSheet("background: #333; \n"
"color: #fff;\n"
"\n"
"QPushButton {\n"
"    background-color:  #444444;\n"
"    border-radius: 0px;\n"
"    padding: 5px 10px 5px 10px;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #555555;\n"
"    color: #fff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.getCurrentColorButton = QtWidgets.QPushButton(self.centralwidget)
        self.getCurrentColorButton.setEnabled(False)
        self.getCurrentColorButton.setStyleSheet("QPushButton {\n"
"    background-color:  #444444;\n"
"    border-radius: 0px;\n"
"    padding: 5px 10px 5px 10px;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color:#373737;\n"
"    color: #808080;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #555555;\n"
"    color: #fff;\n"
"}")
        self.getCurrentColorButton.setObjectName("getCurrentColorButton")
        self.gridLayout.addWidget(self.getCurrentColorButton, 9, 0, 1, 2)
        self.versionComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.versionComboBox.setEnabled(False)
        self.versionComboBox.setStyleSheet(" QComboBox {\n"
"     border: none;\n"
"     border-radius: 3px;\n"
"     padding: 1px 18px 1px 3px;\n"
"     min-width: 6em;\n"
" }\n"
" QComboBox:!editable, QComboBox::drop-down:editable {\n"
"      background:  #444;\n"
" }\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"     background: #555;\n"
" }\n"
" QComboBox:on { \n"
"     padding-top: 3px;\n"
"     padding-left: 4px;\n"
" }\n"
" QComboBox QAbstractItemView {\n"
"     border: 2px solid #444;\n"
"     selection-background-color: #444;\n"
" }\n"
"QComboBox:disabled {\n"
"    background: #373737;\n"
"    color: #808080;\n"
"}")
        self.versionComboBox.setObjectName("versionComboBox")
        self.versionComboBox.addItem("")
        self.versionComboBox.addItem("")
        self.versionComboBox.addItem("")
        self.gridLayout.addWidget(self.versionComboBox, 6, 0, 1, 2)
        self.disconnectionButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectionButton.setEnabled(False)
        self.disconnectionButton.setStyleSheet("QPushButton {\n"
"    background-color:  #444444;\n"
"    border-radius: 0px;\n"
"    padding: 5px 10px 5px 10px;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color:#373737;\n"
"    color: #808080;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #555555;\n"
"    color: #fff;\n"
"}")
        self.disconnectionButton.setObjectName("disconnectionButton")
        self.gridLayout.addWidget(self.disconnectionButton, 3, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 2)
        self.colorComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.colorComboBox.setEnabled(False)
        self.colorComboBox.setStyleSheet(" QComboBox {\n"
"     border: none;\n"
"     border-radius: 3px;\n"
"     padding: 1px 18px 1px 3px;\n"
"     min-width: 6em;\n"
" }\n"
" QComboBox:!editable, QComboBox::drop-down:editable {\n"
"      background:  #444;\n"
" }\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"     background: #555;\n"
" }\n"
" QComboBox:on { \n"
"     padding-top: 3px;\n"
"     padding-left: 4px;\n"
" }\n"
" QComboBox QAbstractItemView {\n"
"     border: 2px solid #444;\n"
"     selection-background-color: #444;\n"
" }\n"
"QComboBox:disabled {\n"
"    background: #373737;\n"
"    color: #808080;\n"
"}")
        self.colorComboBox.setObjectName("colorComboBox")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.gridLayout.addWidget(self.colorComboBox, 7, 0, 1, 2)
        self.ipTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.ipTextBox.setEnabled(True)
        self.ipTextBox.setStyleSheet("QLineEdit {\n"
"    background-color:  #444;\n"
"    border-radius: 0px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QLineEdit:disabled {\n"
"    background-color:#373737;\n"
"    color: #808080;\n"
"}")
        self.ipTextBox.setObjectName("ipTextBox")
        self.gridLayout.addWidget(self.ipTextBox, 1, 0, 1, 2)
        self.connectionButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectionButton.setEnabled(True)
        self.connectionButton.setTabletTracking(False)
        self.connectionButton.setStyleSheet("QPushButton {\n"
"    background-color:  #444444;\n"
"    border-radius: 0px;\n"
"    padding: 5px 10px 5px 10px;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color:#373737;\n"
"    color: #808080;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #555555;\n"
"    color: #fff;\n"
"}")
        self.connectionButton.setObjectName("connectionButton")
        self.gridLayout.addWidget(self.connectionButton, 2, 0, 1, 2)
        self.wiiuIpLabel = QtWidgets.QLabel(self.centralwidget)
        self.wiiuIpLabel.setObjectName("wiiuIpLabel")
        self.gridLayout.addWidget(self.wiiuIpLabel, 0, 0, 1, 2)
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setEnabled(False)
        self.applyButton.setStyleSheet("QPushButton {\n"
"    background-color:  #444444;\n"
"    border-radius: 0px;\n"
"    padding: 5px 10px 5px 10px;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color:#373737;\n"
"    color: #808080;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #555555;\n"
"    color: #fff;\n"
"}")
        self.applyButton.setObjectName("applyButton")
        self.gridLayout.addWidget(self.applyButton, 8, 0, 1, 2)
        self.copyrightLabel = QtWidgets.QLabel(self.centralwidget)
        self.copyrightLabel.setStyleSheet("a {\n"
"    color: red;\n"
"}")
        self.copyrightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.copyrightLabel.setOpenExternalLinks(True)
        self.copyrightLabel.setObjectName("copyrightLabel")
        self.gridLayout.addWidget(self.copyrightLabel, 11, 0, 1, 2)
        self.newVersionLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setKerning(True)
        self.newVersionLabel.setFont(font)
        self.newVersionLabel.setTextFormat(QtCore.Qt.RichText)
        self.newVersionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newVersionLabel.setOpenExternalLinks(True)
        self.newVersionLabel.setObjectName("newVersionLabel")
        self.gridLayout.addWidget(self.newVersionLabel, 10, 0, 1, 2)
        self.regionComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.regionComboBox.setEnabled(False)
        self.regionComboBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.regionComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.regionComboBox.setStyleSheet(" QComboBox {\n"
"     border: none;\n"
"     border-radius: 3px;\n"
"     padding: 1px 18px 1px 3px;\n"
"     min-width: 6em;\n"
" }\n"
" QComboBox:!editable, QComboBox::drop-down:editable {\n"
"      background:  #444;\n"
" }\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"     background: #555;\n"
" }\n"
" QComboBox:on { \n"
"     padding-top: 3px;\n"
"     padding-left: 4px;\n"
" }\n"
" QComboBox QAbstractItemView {\n"
"     border: 2px solid #444;\n"
"     selection-background-color: #444;\n"
" }\n"
"QComboBox:disabled {\n"
"    background: #373737;\n"
"    color: #808080;\n"
"}")
        self.regionComboBox.setObjectName("regionComboBox")
        self.regionComboBox.addItem("")
        self.regionComboBox.addItem("")
        self.regionComboBox.addItem("")
        self.gridLayout.addWidget(self.regionComboBox, 5, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DarkU - v???"))
        self.getCurrentColorButton.setText(_translate("MainWindow", "Get current colour"))
        self.versionComboBox.setItemText(0, _translate("MainWindow", "-- Choose the version of your WiiU --"))
        self.versionComboBox.setItemText(1, _translate("MainWindow", "5.5.3"))
        self.versionComboBox.setItemText(2, _translate("MainWindow", "5.5.4 / 5.5.5"))
        self.disconnectionButton.setText(_translate("MainWindow", "Disconnection"))
        self.colorComboBox.setItemText(0, _translate("MainWindow", "-- Choose background colour --"))
        self.colorComboBox.setItemText(1, _translate("MainWindow", "Default"))
        self.colorComboBox.setItemText(2, _translate("MainWindow", "White"))
        self.colorComboBox.setItemText(3, _translate("MainWindow", "Light Grey"))
        self.colorComboBox.setItemText(4, _translate("MainWindow", "Grey"))
        self.colorComboBox.setItemText(5, _translate("MainWindow", "Dark Grey"))
        self.colorComboBox.setItemText(6, _translate("MainWindow", "Very Dark Grey"))
        self.colorComboBox.setItemText(7, _translate("MainWindow", "Black"))
        self.colorComboBox.setItemText(8, _translate("MainWindow", " Dark Mode (Coming Soon)"))
        self.connectionButton.setText(_translate("MainWindow", "Connection"))
        self.wiiuIpLabel.setText(_translate("MainWindow", "WiiU IP:"))
        self.applyButton.setText(_translate("MainWindow", "Apply"))
        self.copyrightLabel.setText(_translate("MainWindow", "<html><head/><body><p>© 2021 - By VCoding | <a href=\"https://github.com/vincent-coding/DarkU\"><span style=\" text-decoration: underline; color:#3498db;\">Github</span></a></p></body></html>"))
        self.regionComboBox.setItemText(0, _translate("MainWindow", "-- Choose the region of your WiiU --"))
        self.regionComboBox.setItemText(1, _translate("MainWindow", "EUR"))
        self.regionComboBox.setItemText(2, _translate("MainWindow", "USA / JAP"))
