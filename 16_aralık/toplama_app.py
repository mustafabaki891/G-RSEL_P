from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
from toplama import Ui_Form

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.initUI()
        

    def initUI(self):
        self.ui.setupUi(self)

    def toplamaYap(self):
        sayi1 = int(self.ui.txtSayi1.text())
        sayi2 = int(self.ui.txtSayi2.text())
        toplam = sayi1 + sayi2
        self.ui.lblSonuc.setText(str(toplam))

    def carpmaYap(self):
        sayi1 = int(self.ui.txtSayi1.text())
        sayi2 = int(self.ui.txtSayi2.text())
        carpim = sayi1 * sayi2
        self.ui.lblSonuc.setText(str(carpim))        

    def bolmeYap(self):
        sayi1 = int(self.ui.txtSayi1.text())
        sayi2 = int(self.ui.txtSayi2.text())
        bolum = sayi1 / sayi2
        self.ui.lblSonuc.setText(str(bolum))        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


