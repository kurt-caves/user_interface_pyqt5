import sys
import os
# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi #load ui files
from mysql.connector import Error
from PyQt5.QtCore import QDate
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QVBoxLayout, QCalendarWidget, QFileDialog
import siteQuerys

'''
https://www.youtube.com/watch?v=RxGlB9U64fg&list=PLs3IFJPw3G9KhF7BeGOItwoKKLD8e3Dwu&index=7
'''
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        ui_file = resource_path("welcomescreen.ui")  # Dynamically locate the .ui file
        loadUi(ui_file, self)
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
        ui_file = resource_path("downloadscreen.ui")  # Dynamically locate the .ui file
        loadUi(ui_file, self)
        self.home.clicked.connect(self.gobacktowelcomescreen)

        self.start_date = None
        self.end_date = None
        self.site = None
        self.calendarWidget.clicked.connect(self.date_selected)
        
        # site name drop down 
        siteList = siteQuerys.loadsites()
        first_elements = [tup[0] for tup in siteList]
        self.comboBox.addItem("")
        self.comboBox.addItems(first_elements)
        self.comboBox.currentTextChanged.connect(self.setsite)

        # self.comboBox_2.addItem("")
        self.comboBox_2.currentTextChanged.connect(self.setfile)

        # when downloaddata button is clicked
        self.downloaddata.clicked.connect(self.download_data)

        # when update button is clicked
        self.update.clicked.connect(self.tablesearch)


    def tablesearch(self):
        # clear the error text
        self.error.setText("")
        
        start_date_str = self.start_date.toString('yyyy-MM-dd')
        end_date_str = self.end_date.toString('yyyy-MM-dd')
        site = self.site
        print("start date:",start_date_str)
        print("end date: ", end_date_str)
        print("site: ", site)

        fileList = siteQuerys.filetype(site, start_date_str, end_date_str)
        if fileList == [] or fileList == None:
            self.error.setText("No records, try another date")
        else:
            files = [tup[0] for tup in fileList]
            print(files)
            self.comboBox_2.addItems(files)
        
    def setfile(self, s):
        self.file = s

    def download_data(self):
        start_date_str = self.start_date.toString('yyyy-MM-dd')
        end_date_str = self.end_date.toString('yyyy-MM-dd')
        site = self.site
        value = siteQuerys.datadownload(site, start_date_str, end_date_str, self.file)
        print(value)



    def setsite(self, s):
        self.site = s
    
    def gobacktowelcomescreen(self):
        gohome = WelcomeScreen()
        widget.addWidget(gohome)
        widget.setCurrentIndex(widget.currentIndex()+1)
    

    def date_selected(self, selected_date):
        #clear the file dropdown box
        self.comboBox_2.clear()
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
        ui_file = resource_path("sitelookup.ui")  # Dynamically locate the .ui file
        loadUi(ui_file, self)
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
        widget.setCurrentIndex(widget.currentIndex()+1)
    
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