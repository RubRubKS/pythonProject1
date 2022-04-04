from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        cbutton = QCheckBox("I have a Cat")
        cbutton.setChecked(True)
        cbutton.animal = "Cat"
        cbutton.toggled.connect(self.onClicked)
        layout.addWidget(cbutton, 0, 0)

    def onClicked(self):
        cbutton = self.sender()
        print("Animal " + (cbutton.animal) + " is " + str(cbutton.isChecked()))

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())