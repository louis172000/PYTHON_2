from PySide2.QtWidgets import *


class SQLClientWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600, 400)

        self.layout = QVBoxLayout()

        self.Buttons = ButtonsPanel()
        self.layout.addWidget(self.Buttons)

        self.notificationPanel = QTextEdit()
        self.layout.addWidget(self.notificationPanel)

        self.resultTable = QTableWidget(5,3)
        self.layout.addWidget(self.resultTable)
        self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setLayout(self.layout)



class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()

        self.button_configure = QPushButton("Configure")
        self.button_connect = QPushButton("Connect")
        self.button_Disconnect = QPushButton("Disconnect")

        self.layout.addWidget(self.button_configure)
        self.layout.addWidget(self.button_connect)
        self.layout.addWidget(self.button_Disconnect)

        self.setLayout(self.layout)



app = QApplication([])
win = SQLClientWindow()
win.show()
app.exec_()
