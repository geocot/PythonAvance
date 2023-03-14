from enum import Enum, auto
from dataclasses import dataclass

class Mois(Enum):
    JANVIER = 1  # ou auto()
    FEVRIER = 2
    MARS = 3
    AVRIL = 4
    MAI = 5
    JUIN = 6
    JUILLET = 7
    AOUT = 8
    SEPTEMBRE = 9
    OCTOBRE = 10
    NOVEMBRE = 11
    DECEMBRE = 12


@dataclass
class Evennement:
    def __init__(self, jour: int, mois: Mois, annee: int):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __str__(self):
        return f"L'évennement est le {self.jour}/{self.mois}/{self.annee}."


e = Evennement(10, Mois.JANVIER, 2008)
print(e.mois.value) #Pour afficher la valeur
print(e)
# Résultats:
# 1
# L'évennement est le 10/Mois.JANVIER/2008.

