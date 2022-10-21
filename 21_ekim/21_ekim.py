import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()

    layout = QHBoxLayout()
    btn = QPushButton("Click")
    btn2 = QPushButton("Click 2")
    btn3 = QPushButton("Click 3")

    layout.addWidget(btn)
    layout.addWidget(btn2)
    layout.addWidget(btn3)

    w.setLayout(layout)

    w.resize(350,153)
    w.setWindowTitle("Button Example")
    w.show()
    sys.exit(app.exec_())