# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloader_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.URLlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.URLlineEdit.setGeometry(QtCore.QRect(60, 25, 441, 20))
        self.URLlineEdit.setObjectName("URLlineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.destinationLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.destinationLineEdit.setGeometry(QtCore.QRect(70, 70, 351, 20))
        self.destinationLineEdit.setReadOnly(True)
        self.destinationLineEdit.setObjectName("destinationLineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_2.setObjectName("label_2")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(427, 70, 75, 23))
        self.browseButton.setObjectName("browseButton")
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(210, 200, 75, 23))
        self.downloadButton.setObjectName("downloadButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 240, 481, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 130, 491, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 91, 16))
        self.label_3.setObjectName("label_3")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 160, 491, 16))
        self.titleLabel.setObjectName("titleLabel")
        self.proxyCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.proxyCheckBox.setGeometry(QtCore.QRect(460, 200, 51, 17))
        self.proxyCheckBox.setObjectName("proxyCheckBox")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 310, 491, 111))
        self.groupBox.setObjectName("groupBox")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(430, 50, 41, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 50, 41, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 50, 41, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.browseButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.browseButton_2.setGeometry(QtCore.QRect(407, 19, 75, 23))
        self.browseButton_2.setObjectName("browseButton_2")
        self.destinationLineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.destinationLineEdit_2.setGeometry(QtCore.QRect(50, 20, 351, 20))
        self.destinationLineEdit_2.setReadOnly(True)
        self.destinationLineEdit_2.setObjectName("destinationLineEdit_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(100, 50, 41, 16))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(356, 50, 30, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 41, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 50, 41, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.browseButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.browseButton_3.setGeometry(QtCore.QRect(200, 80, 75, 23))
        self.browseButton_3.setObjectName("browseButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "URL"))
        self.label_2.setText(_translate("MainWindow", "Destination"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
        self.label_3.setText(_translate("MainWindow", "Select Download:"))
        self.titleLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#008200;\">Video Title Goes Here</span></p></body></html>"))
        self.proxyCheckBox.setText(_translate("MainWindow", "Proxy"))
        self.groupBox.setTitle(_translate("MainWindow", "Video Trimmer"))
        self.label_9.setText(_translate("MainWindow", ":"))
        self.label_6.setText(_translate("MainWindow", "Start"))
        self.browseButton_2.setText(_translate("MainWindow", "Browse"))
        self.label_8.setText(_translate("MainWindow", ":"))
        self.label_7.setText(_translate("MainWindow", "End"))
        self.label_4.setText(_translate("MainWindow", "Video"))
        self.browseButton_3.setText(_translate("MainWindow", "Trim Video"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

