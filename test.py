import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber
import design

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 260, 431, 221))
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 180, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 100, 161, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 20, 161, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 190, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 190, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(210, 190, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.listWidget.setObjectName("listWidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 110, 81, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 110, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 20, 251, 71))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setObjectName("lcdNumber")
        self.listWidget.raise_()
        self.calendarWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.lcdNumber.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Время движения"))
        self.pushButton.setText(_translate("MainWindow", "Сбросить"))
        self.pushButton_2.setText(_translate("MainWindow", "Остановить"))
        self.pushButton_3.setText(_translate("MainWindow", "Начать движение"))
        self.checkBox.setText(_translate("MainWindow", "60 км/ч"))
        self.checkBox_2.setText(_translate("MainWindow", "80 км/ч"))
        self.checkBox_3.setText(_translate("MainWindow", "120 км/ч"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Чита"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Карымское"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Могоча"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Амазар"))


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow, QLCDNumber):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.Start_T)
        self.pushButton_2.clicked.connect(self.Stop_T)
        self.pushButton.clicked.connect(self.Reset_T)
        # self.t = StringVar()
        self.lcdNumber.setNumDigits(8)
        self.lcdNumber.display('00:00:00')

    def Start_T(self):
        global count
        count = 0
        ##self.start_timer()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime

    def Stop_T(self):
        global count
        count = 1

    def Reset_T(self):
        global count
        count = 1
        self.label.setText('00:00:00')

    def start_timer(self):
        global count
        self.timer()

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]
        self.lcdNumber.setNumDigits(8)
        self.lcdNumber.display(text)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
