import os

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QTimer
import simpleaudio


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Sobesedovanie()
        self.ui.setupUi(self)

k = 0
num = 0

class Ui_Sobesedovanie(object):
    def setupUi(self, form):
        form.setObjectName("Form")
        form.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(form)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(20, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 150, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 230, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 290, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 20, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setAutoExclusive(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 360, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 420, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(50, 490, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(50, 570, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("font: 16pt \"Segoe UI Emoji\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setChecked(True)
        self.checkBox.setGeometry(QtCore.QRect(320, 580, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 650, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 200, 360, 380))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/????????????/Downloads/gerb.png"))
        self.label_2.setObjectName("label_2")
        self.minutes = QtWidgets.QLabel(self.centralwidget)
        self.minutes.setGeometry(QtCore.QRect(730, 80, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.minutes.setFont(font)
        self.minutes.setObjectName("minutes")
        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)


    def retranslateUi(self, Sobesedovanie):
        _translate = QtCore.QCoreApplication.translate
        Sobesedovanie.setWindowTitle(_translate("Sobesedovanie", "MainWindow"))
        self.pushButton.setText(_translate("Sobesedovanie", "???????????????????? ?? ????????????"))
        self.pushButton_2.setText(_translate("Sobesedovanie", "???????????? ????????????"))
        self.pushButton_3.setText(_translate("Sobesedovanie", "???????????????????? ?? ??????????????????"))
        self.pushButton_5.setText(_translate("Sobesedovanie", "???????????????? ????????????"))
        self.pushButton_6.setText(_translate("Sobesedovanie", "?????????? ????????????????"))
        self.pushButton_7.setText(_translate("Sobesedovanie", "???????????????????? ?? ????????????????"))
        self.pushButton_8.setText(_translate("Sobesedovanie", "??????????????"))
        self.pushButton_9.setText(_translate("Sobesedovanie", "????????????"))
        self.pushButton_10.setText(_translate("Sobesedovanie", "????????!"))
        self.checkBox.setText(_translate("Sobesedovanie", "????????"))
        self.label.setText(_translate("Sobesedovanie", "???????? \"?????????? ???131\""))
        self.minutes.setText(_translate("Sobesedovanie", "0:00"))

        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)

        self.pushButton.clicked.connect(lambda: self.click1())
        self.pushButton_2.clicked.connect(lambda: self.click2())
        self.pushButton_3.clicked.connect(lambda: self.click3())
        self.pushButton_5.clicked.connect(lambda: self.click4())
        self.pushButton_7.clicked.connect(lambda: self.click5())
        self.pushButton_8.clicked.connect(lambda: self.click6())
        self.pushButton_9.clicked.connect(lambda: self.click7())
        self.pushButton_6.clicked.connect(lambda: self.nov_uchastnik())
        self.pushButton_10.clicked.connect(lambda: self.stop())
        self.timerDown = QTimer()

    def nov_uchastnik(self):
        global num
        num += 1

        self.starttime = 1
        self.timerDown = QTimer()
        self.timerDown.setInterval(1000)
        self.timerDown.timeout.connect(self.timer2)
        self.timerDown.start()

        self.recorder = QtMultimedia.QAudioRecorder()
        self.selected_audio_input = self.recorder.audioInput()
        self.recorder.setAudioInput(self.selected_audio_input)
        self.settings = QtMultimedia.QAudioEncoderSettings()
        self.selected_codec = "audio/pcm"
        self.settings.setCodec(self.selected_codec)
        self.settings.setSampleRate(192000)
        self.settings.setBitRate(128000)
        self.settings.setChannelCount(1)
        self.recorder.setEncodingSettings(self.settings, QtMultimedia.QVideoEncoderSettings(), "audio/x-wav")

        self.recorder.stop()

        print('da')

        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)



    def click1(self):
        global num
        self.pushButton.setEnabled(False)

        _translate = QtCore.QCoreApplication.translate
        self.minutes.setText(_translate("Sobesedovanie", "2:00"))

        self.starttime = 120
        self.timerDown = QTimer()
        self.timerDown.setInterval(1000)
        self.timerDown.timeout.connect(self.timer)
        self.timerDown.start()

        global k
        k = 1

    def click2(self):
        global num
        self.pushButton_2.setEnabled(False)
        _translate = QtCore.QCoreApplication.translate
        self.minutes.setText(_translate("Sobesedovanie", "2:00"))

        self.starttime = 120
        self.timerDown = QTimer()
        self.timerDown.setInterval(1000)
        self.timerDown.timeout.connect(self.timer)
        self.timerDown.start()

        global k
        k = 2

    def click3(self):
        global num
        self.pushButton_3.setEnabled(False)
        _translate = QtCore.QCoreApplication.translate
        self.minutes.setText(_translate("Sobesedovanie", "2:00"))

        self.starttime = 120
        self.timerDown = QTimer()
        self.timerDown.setInterval(1000)
        self.timerDown.timeout.connect(self.timer)
        self.timerDown.start()

        global k
        k = 3

    def click4(self):
        global num
        self.pushButton_5.setEnabled(False)
        _translate = QtCore.QCoreApplication.translate
        self.minutes.setText(_translate("Sobesedovanie", "3:00"))

        self.starttime = 180
        self.timerDown = QTimer()
        self.timerDown.setInterval(1000)
        self.timerDown.timeout.connect(self.timer)
        self.timerDown.start()
        global k
        k = 4

    def click5(self):
        global num
        self.pushButton_7.setEnabled(False)
        _translate = QtCore.QCoreApplication.translate
        self.minutes.setText(_translate("Sobesedovanie", "1:00"))

        self.starttime = 60
        self.timerDown = QTimer()
        self.timerDown.setInterval(1000)
        self.timerDown.timeout.connect(self.timer)
        self.timerDown.start()
        global k
        k = 5

    def click6(self):
        global num
        self.pushButton_8.setEnabled(False)
        _translate = QtCore.QCoreApplication.translate
        self.minutes.setText(_translate("Sobesedovanie", "3:00"))

        self.starttime = 180
        self.timerDown = QTimer()
        self.timerDown.setInterval(1000)
        self.timerDown.timeout.connect(self.timer)
        self.timerDown.start()
        global k
        k = 6

    def click7(self):
        global num
        self.pushButton_9.setEnabled(False)
        _translate = QtCore.QCoreApplication.translate
        self.minutes.setText(_translate("Sobesedovanie", "3:00"))

        self.starttime = 180
        self.timerDown = QTimer()
        self.timerDown.setInterval(1000)
        self.timerDown.timeout.connect(self.timer)
        self.timerDown.start()

        global k
        k = 7

    def stop(self):
        if self.timerDown.isActive():
            if self.checkBox.isChecked():
                beep = 'beep1.wav'
                beep_sound = simpleaudio.WaveObject.from_wave_file(beep)
                beep_sound.bytes_per_sample = 2
                beep_sound.num_channels = 1
                beep_sound.play()
        self.timerDown.stop()
        global k
        if k == 1:
            self.pushButton_2.setEnabled(True)
        if k == 2:
            self.pushButton_3.setEnabled(True)
        if k == 3:
            self.pushButton_5.setEnabled(True)
        if k == 4:
            self.pushButton_7.setEnabled(True)
        if k == 5:
            self.pushButton_8.setEnabled(True)
        if k == 6:
            self.pushButton_9.setEnabled(True)

    def ShubinkinBoh(self):
        print('S NAMI ROSSIYA')

    def timer(self):
        self.starttime -= 1
        self.minutes.setText(f'{self.starttime // 60}:{self.starttime % 60:02}')
        if self.starttime == 0:
            self.stop()

    def timer2(self):
        self.starttime -= 1
        if self.starttime == 0:
            name = "????????????????" + str(num)
            self.filename = os.path.join("D:/", name)
            print(self.filename)
            self.recorder.setOutputLocation(QtCore.QUrl.fromLocalFile(self.filename))
            self.recorder.record()

            self.stop()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
