#Code de base pour utiliser les fichiers UI de QTDesigner directement. 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog #Ajouter les modules necessaires
from PyQt5 import uic

class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()
        #Chargement du ficier UI
        uic.loadUi('demo.ui', self)

        #Affiche l'inteface
        self.setWindowTitle('Démo')
        self.show()

#Initialisation de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
