from PyQt5 import QtCore, QtGui, QtWidgets
import csv

userInput = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.propertyidline = QtWidgets.QLineEdit(self.centralwidget)
        self.propertyidline.setGeometry(QtCore.QRect(100, 150, 271, 51))
        self.propertyidline.setObjectName("propertyidline")
        self.propertyidbutton = QtWidgets.QPushButton(self.centralwidget)
        self.propertyidbutton.setGeometry(QtCore.QRect(410, 150, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.propertyidbutton.setFont(font)
        self.propertyidbutton.setObjectName("propertyidbutton")

        self.apikeybutton = QtWidgets.QPushButton(self.centralwidget)
        self.apikeybutton.setGeometry(QtCore.QRect(410, 230, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.apikeybutton.setFont(font)
        self.apikeybutton.setObjectName("apikeybutton")
        self.apikeyline = QtWidgets.QLineEdit(self.centralwidget)
        self.apikeyline.setGeometry(QtCore.QRect(100, 230, 271, 51))
        self.apikeyline.setObjectName("apikeyline")

        self.enddatebutton = QtWidgets.QPushButton(self.centralwidget)
        self.enddatebutton.setGeometry(QtCore.QRect(410, 390, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.enddatebutton.setFont(font)
        self.enddatebutton.setObjectName("enddatebutton")
        self.enddateline = QtWidgets.QLineEdit(self.centralwidget)
        self.enddateline.setGeometry(QtCore.QRect(100, 390, 271, 51))
        self.enddateline.setObjectName("enddateline")

        self.startdatebutton = QtWidgets.QPushButton(self.centralwidget)
        self.startdatebutton.setGeometry(QtCore.QRect(410, 310, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.startdatebutton.setFont(font)
        self.startdatebutton.setObjectName("startdatebutton")
        self.startdateline = QtWidgets.QLineEdit(self.centralwidget)
        self.startdateline.setGeometry(QtCore.QRect(100, 310, 271, 51))
        self.startdateline.setObjectName("startdateline")

        self.reporttypebutton = QtWidgets.QPushButton(self.centralwidget)
        self.reporttypebutton.setGeometry(QtCore.QRect(410, 70, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.reporttypebutton.setFont(font)
        self.reporttypebutton.setObjectName("reporttypebutton")
        self.reporttypeline = QtWidgets.QLineEdit(self.centralwidget)
        self.reporttypeline.setGeometry(QtCore.QRect(100, 70, 271, 51))
        self.reporttypeline.setObjectName("reporttypeline")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.propertyidbutton.clicked.connect(self.add_id)
        self.apikeybutton.clicked.connect(self.add_key)
        self.reporttypebutton.clicked.connect(self.add_type)
        self.startdatebutton.clicked.connect(self.add_startdate)
        self.enddatebutton.clicked.connect(self.add_enddate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_id(self):
        userInput.append(self.propertyidline.text())
    
    def add_key(self):
        userInput.append(self.apikeyline.text())

    def add_type(self):
        userInput.append(self.reporttypeline.text())

    def add_startdate(self):
        userInput.append(self.startdateline.text())

    def add_enddate(self):
        userInput.append(self.enddateline.text())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.propertyidbutton.setText(_translate("MainWindow", "Google Property ID"))
        self.apikeybutton.setText(_translate("MainWindow", "API Key"))
        self.enddatebutton.setText(_translate("MainWindow", "End Date"))
        self.startdatebutton.setText(_translate("MainWindow", "Start Date"))
        self.reporttypebutton.setText(_translate("MainWindow", "Website or Mobile?"))

    print(userInput)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())