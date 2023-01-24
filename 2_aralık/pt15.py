from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("Arial", 14))
        self.setToolTip("Hello")
        btn = QPushButton("Button", self)
        btn.setToolTip("Clich here to contiune")
        btn.resize(btn.sizeHint())
        btn.move(100,100)
        btn.setGeometry(300,300,300,220)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


