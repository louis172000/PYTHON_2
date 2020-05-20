from PySide2.QtWidgets import *


class LabeledTextField(QWidget):
    def __init__(self, text):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()
        self.objet_texte = QLabel(text)
        self.objet_edit = QTextEdit()
        self.objet_edit.setMaximumHeight(30)

        self.layout.addWidget(self.objet_texte)
        self.layout.addWidget(self.objet_edit)

        self.setLayout(self.layout)

class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.layout = QVBoxLayout()

        self.text_ip = LabeledTextField("IP address")
        self.text_user = LabeledTextField("User")
        self.text_pass = LabeledTextField("Password")

        self.setWindowTitle("Configuration")

        self.layout.addWidget(self.text_ip)
        self.layout.addWidget(self.text_user)
        self.layout.addWidget(self.text_pass)
        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = ConfigurationDialog()
   win.show()
   app.exec_()
