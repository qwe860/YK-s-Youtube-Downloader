from msilib.schema import CheckBox
from downloader_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pytube import YouTube
import ctypes
import validators
import json

proxy_handler = {
"http": "http://10.110.6.6:8080",
'https': 'https://10.110.6.6:8080'
}
#compat.install_proxy(proxy_handler)

class MainWindow(QtWidgets.QMainWindow, QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Kae's aWFuL Youtube Downloader!!?!?!")
        self.setWindowIcon(QtGui.QIcon('icon.png'))    
        self.browseButton.clicked.connect(lambda index = 0: self.getDirectory())
        self.downloadButton.clicked.connect(lambda index = 0: self.download())
        self.URLlineEdit.editingFinished.connect(lambda index = 0: self.Obtain_Info())
        self.downloadButton.setDisabled(True)

        self.SAVE_PATH = '/'
        

    def Obtain_Info(self):

        valid=validators.url(self.URLlineEdit.text())

        if valid:
            
            CheckBoxChecked = False

            if self.proxyCheckBox.isChecked():
                CheckBoxChecked = True

            self.url = self.URLlineEdit.text()
            self.worker2 = Worker2Thread(self.url, CheckBoxChecked)
            self.worker2.start()
            self.worker2.items.connect(self.UpdateItemList)
            self.worker2.error_message.connect(self.ErrorMsg)
            self.worker2.title.connect(self.ChangeTitle)
            self.worker2.finished.connect(self.obtain_completed)
            

    def getDirectory(self):
        response = QFileDialog.getExistingDirectory(
            self,
            caption='Select a folder'
        )
        self.destinationLineEdit.setText(response)
        self.SAVE_PATH = response
        print(response)

    def download(self):
        valid=validators.url(self.URLlineEdit.text())

        if valid==True:
            if self.destinationLineEdit.text() == '':
                QMessageBox.critical(self, 'Error', 
                'File directory cannot be empty!',
                QMessageBox.Ok)

            else:
                print("Url is valid")

                self.downloadButton.setDisabled(True)
                self.url = self.URLlineEdit.text()

                itag = '{' + self.comboBox.currentText() + '}'
                itag = itag.replace(' ', '')
                itag = json.loads(itag)
                EYEtag = itag['itag']

                self.worker = WorkerThread(self.url, self.SAVE_PATH, EYEtag)
                self.worker.start()
                self.worker.download_progress.connect(self.UpdateProgressBar)
                self.worker.error_message.connect(self.ErrorMsg)
                self.worker.finished.connect(self.completed)

        else:
            print("Invalid url")
            QMessageBox.critical(self, 'Error', 
            'Please make sure the URL is valid!',
            QMessageBox.Ok)
        
    def UpdateItemList(self, items):
        self.comboBox.clear()
        self.comboBox.addItems(items)
        print(items)

    def UpdateProgressBar(self, progress):
        self.progressBar.setValue(progress)

    def obtain_completed(self):
        self.downloadButton.setDisabled(False)

    def completed(self):
        self.downloadButton.setDisabled(False)
        QMessageBox.information(self, 'Information', "Download Complete!", QMessageBox.Ok)

    def ErrorMsg(self, error):
        QMessageBox.critical(self, 'Error', 
        'An unknown error occured. Please rectify it. I dunno what is going on. I just know that IT''S AN ERROR!: ' + error,
        QMessageBox.Ok)
    def ChangeTitle(self, title):

        title = '<html><head/><body><p><span style=\" color:#008200;\">' + title+'</span></p></body></html>'
        self.titleLabel.setText(title)

class Worker2Thread(QThread):
    items = pyqtSignal(list)
    error_message = pyqtSignal(str)
    title = pyqtSignal(str)
    def __init__(self, URL, proxyCheckBoxChecked):
        super(Worker2Thread, self).__init__()
        self.url = URL
        self.proxyCheckBoxChecked = proxyCheckBoxChecked

    def run(self):
        try:

            if self.proxyCheckBoxChecked:               
                yt = YouTube(self.url, proxies=proxy_handler)
                print('got proxy')
            else:
                yt = YouTube(self.url)
                print('no proxy')
            urgh  = yt.streams
            title = yt.title
            self.title.emit(title)
            index = 0
            strim = []

            for Stream in urgh:                
                print(Stream)

                if Stream.mime_type == 'video/mp4':
                    
                    if Stream.audio_codec:
                        elloh = '"itag":'+str(Stream.itag) + ',   "type":"'+Stream.type + '",   "resolution":"'+str(Stream.resolution)+'"' + ',   "vcodec":"'+Stream.video_codec+'"' + ',  "acodec":"'+Stream.audio_codec+'"' 
                        strim.append(elloh)

                    index+=1

                elif Stream.mime_type == 'audio/mp4':

                    elloh = '"itag":'+str(Stream.itag) + ',           "type":"'+Stream.type +'"'+',              "acodec":"'+Stream.audio_codec+'"'

                    strim.append(elloh)
                    index+=1

            self.items.emit(strim)

        except Exception as e:
            e = str(e)
            print(self.url)
            self.error_message.emit(e)
            
        
        


class WorkerThread(QThread):
    update_sheets = pyqtSignal(list)
    download_progress = pyqtSignal(int)
    error_message = pyqtSignal(str)

    def __init__(self, URL, file_path, itag):
        super(WorkerThread, self).__init__()
        self.url = URL
        self.file_path = file_path
        self.itag = itag

    def run(self):
        #link  = self.url
       
        try: 
            yt = YouTube(self.url, on_progress_callback=self.progress_function)
            stream = yt.streams.get_by_itag(self.itag) #https://github.com/pytube/pytube/issues/873
            # downloading the video 
            global filesize 
            filesize = stream.filesize
            stream.download(output_path=self.file_path)

        except Exception as e:
            '''QMessageBox.critical(self, 'Error', 
            'An unknown error occured. Please rectify it. I dunno what is going on. I just know that IT''S AN ERROR!',
            QMessageBox.Ok)'''
            e = str(e)
            print(e)
            self.error_message.emit(e)
            #self.terminate()

    def progress_function(self, chunk, file_handle, bytes_remaining):
        #print(round((1-bytes_remaining/stream.filesize)*100, 3), '% done...')

        progress = round((1 - (bytes_remaining/filesize)) * 100 ,0)
        progress = int(progress)
        self.download_progress.emit(progress)
        print(progress)


if __name__ == "__main__":
    import sys
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)
    myWidget = MainWindow()
    myWidget.show()
    sys.exit(app.exec_())
