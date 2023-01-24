import sys
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton, QHBoxLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w=QWidget()
    layout=QHBoxLayout()
    btn=QPushButton("hello world")
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())