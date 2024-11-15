import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi #load ui files
from mysql.connector import Error
from PyQt5.QtCore import QDate
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QVBoxLayout, QCalendarWidget
import siteQuerys

'''
https://www.youtube.com/watch?v=RxGlB9U64fg&list=PLs3IFJPw3G9KhF7BeGOItwoKKLD8e3Dwu&index=7
'''

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui", self)
        self.checksite.clicked.connect(self.gotositelookup)
        self.downloaddata.clicked.connect(self.gotodownload)

    def gotositelookup(self):
        sitelookupbox = SiteLookupScreen()
        widget.addWidget(sitelookupbox)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotodownload(self):
        download = DownloadScreen()
        widget.addWidget(download)
        widget.setCurrentIndex(widget.currentIndex()+1)

class DownloadScreen(QDialog):
    def __init__(self):
        super(DownloadScreen, self).__init__()
        loadUi("downloadscreen.ui", self)

        self.start_date = None
        self.end_date = None
        self.site = None
        self.calendarWidget.clicked.connect(self.date_selected)
        
        siteList = siteQuerys.loadsites()
        first_elements = [tup[0] for tup in siteList]
        self.comboBox.addItem("")
        self.comboBox.addItems(first_elements)
        
        self.comboBox.currentTextChanged.connect(self.text_changed)

        # self.downloaddata.clicked.connect(lambda: self.download_data(self.start_date, self.end_date, self.site))
        self.downloaddata.clicked.connect(self.download_data)
    
    def download_data(self):
        print("start date : ", self.start_date)
        print("end date :", self.end_date)
        print("site selected:", self.site)

    def text_changed(self, s):
        print("New site:", s)
        self.site = s
    

    def date_selected(self, selected_date):
        # Retrieve the selected date from the QCalendarWidget
        selected_date = self.calendarWidget.selectedDate()

        if self.start_date is None:
            self.start_date = selected_date
            self.startdate.setText(f"Start Date: {self.start_date.toString()}")
        elif self.end_date is None:
            self.end_date = selected_date
            if self.end_date < self.start_date:
                self.start_date, self.end_date = self.end_date, self.start_date  # Swap if needed
            self.startdate.setText(f"Start Date: {self.start_date.toString()}")
            self.enddate.setText(f"End Date: {self.end_date.toString()}")
        else:
            # Reset and start a new range selection
            self.start_date = selected_date
            self.end_date = None
            self.startdate.setText(f"Start Date: {self.start_date.toString()}")
            self.enddate.clear()
        

class SiteLookupScreen(QDialog):
    def __init__(self):
        super(SiteLookupScreen, self).__init__()
        loadUi("sitelookup.ui", self)
        self.checksite.clicked.connect(self.checksites)
        self.home.clicked.connect(self.gobacktowelcomescreen)
        
        siteList = siteQuerys.loadsites()
        first_elements = [tup[0] for tup in siteList]
        
        self.comboBox.addItems(first_elements)
        self.comboBox.activated.connect(self.activated)
        self.comboBox.currentTextChanged.connect(self.text_changed)
        self.comboBox.currentIndexChanged.connect(self.index_changed)
    
    def gobacktowelcomescreen(self):
        gohome = WelcomeScreen()
        widget.addWidget(gohome)
        widget.setCurrentIndex(widget.currentIndex()-1)
    
    def checksites(self):
        sitetoQuery = self.siteedit.text()
        print(sitetoQuery)

        queriedSite = siteQuerys.sitequery(sitetoQuery)
        print(queriedSite)
        if queriedSite == []:
            self.error.setText("Site does not exist")
            
        else:
            self.error.setText("Site Exists")



    def activated(self, index):
        print("Activated index:", index)

    def text_changed(self, s):
        print("Text changed:", s)

    def index_changed(self, index):
        print("Index changed", index)
        

    
app = QApplication(sys.argv)
welcome = WelcomeScreen()

widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")