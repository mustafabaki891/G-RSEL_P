import sys
from PyQt5 import QtWidgets, QtGui

app = QtWidgets.QApplication(sys.argv)

w = QtWidgets.QWidget()

w.resize(500, 500)

w.move(300,100)
w.setWindowTitle("Hello World")

w.setWindowIcon(QtGui.QIcon('pattern.png'))

w.show()

sys.exit(app.exec_())