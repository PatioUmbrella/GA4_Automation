from PyQt5 import QtCore, QtGui, QtWidgets
import time
import csv
import pandas as pd
import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    MetricType,
    RunReportRequest
)
import numpy as np
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
from google.analytics.data_v1beta.types import OrderBy

userInput = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

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

#create frame button
        self.createreportbutton = QtWidgets.QPushButton(self.centralwidget)
        self.createreportbutton.setGeometry(QtCore.QRect(410, 470, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.createreportbutton.setFont(font)
        self.createreportbutton.setObjectName("createreportbutton")
        
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
        self.createreportbutton.clicked.connect(self.make_report)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_id(self):
        userInput.append(self.propertyidline.text())
        print(userInput)
    
    def add_key(self):
        userInput.append(self.apikeyline.text())
        print(userInput)

    def add_type(self):
        userInput.append(self.reporttypeline.text())
        print(userInput)

    def add_startdate(self):
        userInput.append(self.startdateline.text())
        print(userInput)

    def add_enddate(self):
        userInput.append(self.enddateline.text())
        print(userInput)

    def make_report(self):
        
        #run lines of code one section at a time
        #run
        #Set up global variables
        print("report started")
        time.sleep(5.5)
        
        #run
        print("step 1 started")
        time.sleep(5.5)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(userInput[2])
        property_id = str(userInput[1])
        client = BetaAnalyticsDataClient()
        print("step 1 finished")
        time.sleep(5.5)

        ## Format Report - run_report method
        #run
        print("step 2 started")
        time.sleep(5.5)
        def format_report(request):
            response = client.run_report(request)

            # Row index
            row_index_names = [header.name for header in response.dimension_headers]
            row_header = []
            for i in range(len(row_index_names)):
                row_header.append([row.dimension_values[i].value for row in response.rows])

            row_index_named = pd.MultiIndex.from_arrays(np.array(row_header), names = np.array(row_index_names))
            # Row flat data
            metric_names = [header.name for header in response.metric_headers]
            data_values = []
            for i in range(len(metric_names)):
                data_values.append([row.metric_values[i].value for row in response.rows])

            output = pd.DataFrame(data = np.transpose(np.array(data_values, dtype = 'f')),
                                index = row_index_named, columns = metric_names)
            return output

        print("step 2 finished")
        time.sleep(5.5)
        
        #run
        print("step 3 started")
        time.sleep(5.5)
        
        request = RunReportRequest(
                property='properties/'+property_id,
                dimensions=[Dimension(name="month"),
                            Dimension(name="browser")],
                metrics=[Metric(name="averageSessionDuration"),
                        Metric(name="totalUsers")],
                #order_bys = [OrderBy(dimension = {'dimension_name': 'month'}),
                #            OrderBy(dimension = {'dimension_name': 'sessionMedium'})],
                date_ranges=[DateRange(start_date=str(userInput[3]), end_date=str(userInput[4]))],
            )
        print("step 3 finished")
        time.sleep(5.5)

        #run
        #format
        print("step 4 started")
        time.sleep(5.5)
        format_report(request)
        print("step 4 finished")
        time.sleep(5.5)

        #run
        #output and export to CSV
        output_df = format_report(request)
        output_df.to_csv('GA4_python_output4.csv')
        print('Done! (step 5)')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutomateMe!1!"))
        self.reporttypebutton.setText(_translate("MainWindow", "Website or Mobile?"))
        self.propertyidbutton.setText(_translate("MainWindow", "Google Property ID"))
        self.apikeybutton.setText(_translate("MainWindow", "API Key"))
        self.startdatebutton.setText(_translate("MainWindow", "Start Date"))
        self.enddatebutton.setText(_translate("MainWindow", "End Date"))
        self.createreportbutton.setText(_translate("MainWindow", "Create Report"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())