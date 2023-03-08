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
    x = Descripteur(-71,"coordX")
    y = Descripteur(46, "coordY")

class Ville():
    nom = Descripteur("Québec", "Nom")

p = Point()
print(p.x)
print(p.y)

v = Ville()
print(v.nom)

