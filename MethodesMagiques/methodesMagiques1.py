class Planete:
    "Classe planete"
    def __init__(self, nom, diametre):
        self._nom = nom
        self._diametre = diametre

    def __str__(self):
        return f"Le nom est {self._nom} et le diamètre est de {self._diametre}"

terre = Planete("Terre", 12756.274)

print(terre)


