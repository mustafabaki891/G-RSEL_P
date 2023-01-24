from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class CustomDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("Hello")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        message = QLabel("Are you ok?")

        self.layout = QVBoxLayout()
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button = QPushButton("Press here")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        
    def button_clicked(self, s):
        print("clicked", s)

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Hello")
        dlg.setText("Are you ok")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Ok)

        button = dlg.exec()

        if button == QMessageBox.Ok:
            print("OK")
        elif button == QMessageBox.Yes:
            print("Yess")
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


