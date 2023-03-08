class Descripteur:
    def __init__(self, valeur=None, nom=None):
        self._val = valeur
        self._nom = nom
    def __get__(self,instance, type):
        print("Retour de", self._nom)
        return (self._val)
    def __set__(self, instance, val):
        print("Change ", self._nom)
        self._val = val

class Point():
    x = Descripteur(nom="coordX")
    y = Descripteur(nom="coordY")

    def __init__(self, x,y):
        self.x = x
        self.y = y

class Ville():
    nom = Descripteur("Québec", "Nom")

p = Point("-71",46)
print(p.x)
print(p.y)

v = Ville()
print(v.nom)

