from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys

class Planete:
    def __init__(self, nom, rang, distSol):
        self._nom = nom
        self._rang = rang
        self._distSol = distSol

    @property
    def nom(self):
        return self._nom

    @property
    def rang(self):
        return self._rang

    @property
    def distSol(self):
        return self._distSol

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Planètes")
        self.setGeometry(500,400,500,300)
        self._creationTableView()
        self.show()

    def _creationTableView(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnWidth(0,200)

        self.tableWidget.setItem(0,0,QTableWidgetItem("Nom"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Rang"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Distance soleil"))

        self.vBoite = QVBoxLayout()
        self.vBoite.addWidget(self.tableWidget)
        self.setLayout(self.vBoite)

    def sychroTableView(self, listePlanetes):
        self.tableWidget.clear()

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(listePlanetes)+1)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setItem(0,0,QTableWidgetItem("Nom"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Rang"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Distance soleil"))

        compteurItem = 1
        for planete in listePlanetes:
            self.tableWidget.setItem(compteurItem,0,QTableWidgetItem(planete.nom))
            self.tableWidget.setItem(compteurItem, 1, QTableWidgetItem(str(planete.rang)))
            self.tableWidget.setItem(compteurItem, 2, QTableWidgetItem(str(planete.distSol)))
            compteurItem +=1


class Controller:
    def __init__(self):
        self.listePlanetes = []

    def showFen(self, *args):
        self.windowFen = Window()
        self.windowFen.show()

    def ajoutPlanete(self, planete):
        self.listePlanetes.append(planete)
        self.windowFen.sychroTableView(self.listePlanetes)


def main():
    App = QApplication(sys.argv)
    controleur = Controller()
    controleur.showFen()
    p = Planete("Terre", 3, 150000000)
    controleur.ajoutPlanete(p)
    p = Planete("Vénus", 2, 85000000)
    controleur.ajoutPlanete(p)
    sys.exit(App.exec())

if __name__ == '__main__':
    main()