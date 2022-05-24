from msilib.schema import CheckBox
from downloader_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pytube import YouTube
from moviepy.editor import *
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
        self.browseButton.clicked.connect(lambda index = 0: self.getDirectory(self.destinationLineEdit, 'download'))
        self.downloadButton.clicked.connect(lambda index = 0: self.download())
        self.URLlineEdit.editingFinished.connect(lambda index = 0: self.Obtain_Info())
        self.downloadButton.setDisabled(True)

        self.trimButton.clicked.connect(lambda index = 0: self.Trim())
        self.browseButton_2.clicked.connect(lambda index = 0: self.getDirectory(self.vidPathLineEdit, 'trim'))

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
            

    def getDirectory(self, LineEdit, type):

        if type == 'download':
            response = QFileDialog.getExistingDirectory(
                self,
                caption='Select a folder'
            )

        else:
             response = QFileDialog.getOpenFileName(
                self,
                caption='Select a file',
                filter='Video file (*.mp4)'
            )
             LineEdit.setText(response[0])
             response = response[0]
             self.readVideoFile(response)
        '''try:
            LineEdit.setText(response)
        except:
            LineEdit.setText(response[0])
            self.readVideoFile(response[0])'''

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

    def UpdateDuration(self, clip_duration):
        print('clip duration: ', clip_duration)
        mins = clip_duration / 60
        secs = clip_duration % 60
        self.endMinSpinBox.setValue(mins)
        self.endMinSpinBox.setMaximum(mins)
        self.startMinSpinBox.setMaximum(mins)
        self.startSecSpinBox.setMaximum(secs)
        self.endSecSpinBox.setValue(secs)
        self.endSecSpinBox.setMaximum(secs)


    def readVideoFile(self, path):
        self.LoadVidWorker = LoadVideoThread(path)
        self.LoadVidWorker.start()
        self.LoadVidWorker.clip_duration.connect(self.UpdateDuration)
        self.LoadVidWorker.finished.connect(self.TrimCompleted)


    def TrimCompleted(self):
        QMessageBox.information(self, 'Information', "Trim Complete!", QMessageBox.Ok)

    def Trim(self):
        print('trim')
        start_min = self.startMinSpinBox.value()
        start_sec = self.startSecSpinBox.value()
        end_min = self.endMinSpinBox.value()
        end_sec = self.endSecSpinBox.value()

        start = start_min*60 + start_sec
        end = end_min*60 + end_sec

        self.trimWorker = Worker3Thread(self.SAVE_PATH, start, end)
        self.trimWorker.start()
        self.trimWorker.finished.connect(self.TrimCompleted)

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

    def progress_function(self, chunk, file_handle, bytes_remaining):

        progress = round((1 - (bytes_remaining/filesize)) * 100 ,0)
        progress = int(progress)
        self.download_progress.emit(progress)
        print(progress)
        
class LoadVideoThread(QThread):
    clip_duration = pyqtSignal(float)

    def __init__(self, file_path):
        super(LoadVideoThread, self).__init__()
        self.file_path = file_path

    def run(self):
        clip = VideoFileClip(self.file_path)
        duration = clip.duration
        self.clip_duration.emit(duration)


class Worker3Thread(QThread):
    global start_time
    global end_time

    def __init__(self, file_path, start, end):
        super(Worker3Thread, self).__init__()
        self.start_time = start
        self.file_path = file_path
        self.end_time = end

    def run(self):        
        print('start_time: ', self.start_time)
        print('end_time: ', self.end_time)
        clip = VideoFileClip(self.file_path)
        clip = clip.cutout(self.start_time, self.end_time)
        clip.write_videofile("edited.mp4")



if __name__ == "__main__":
    import sys
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)
    myWidget = MainWindow()
    myWidget.show()
    sys.exit(app.exec_())
