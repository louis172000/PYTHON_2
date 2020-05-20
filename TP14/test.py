import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

# creation de la fenetre
fen = QWidget()

# creation du premier bouton
bouton1 = QPushButton("mon premier bouton dans un QHBoxLayout")
# creation du deuxieme bouton
bouton2 = QPushButton("mon deuxieme bouton dans un QHBoxLayout")

# creation du gestionnaire de mise en forme de type QHBoxLayout
layout = QHBoxLayout()
# ajout du premier bouton au gestionnaire de mise en forme
layout.addWidget(bouton1)
# ajout du deuxieme bouton au gestionnaire de mise en forme
layout.addWidget(bouton2)
# on fixe le QHBoxLayout comme gestionnaire de mise en forme de la fenetre
fen.setLayout(layout)

fen.show()

app.exec_()