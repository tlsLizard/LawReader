"""
La classe MainWindow hérite de la classe générée automatiquement
par pyside6-designer (Ui_MainWindow)
On peut surcharger les méthodes pour ajuster le comportement

commande pour générer classes python à partir des fichier .ui
```pyside6-uic xxx.ui -o ui_xxx.py```
"""

from PySide6.QtWidgets import QMainWindow

from . import ui_interface
import src.Model.Document
from PySide6.QtCore import QCoreApplication

class MainWindow(QMainWindow, ui_interface.Ui_MainWindow):
    def __init__(self, document=None):
        super(MainWindow, self).__init__()
        self.document = document  #  model

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        MainWindow.setObjectName(u"LawReader: MainWindow")
        MainWindow.resize(600, 200)


    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", f"LawReader - {str(self.document)}", None))