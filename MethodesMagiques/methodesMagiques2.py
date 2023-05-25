class Planete:
    """Classe planète, permet de créer des planètes."""
    def __init__(self, nom, diametre):
        self._nom = nom
        self._diametre = diametre

    def __del__(self):
        print("Suppression")

print(Planete.__doc__)


