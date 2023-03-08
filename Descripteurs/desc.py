class Descripteur:
    def __get__(self,instance, type):
        return (instance._val)
    def __set__(self, instance, val):
        instance._val = val

class Planete:
    def __init__(self, nom):
        self._val = nom

    nomPlanete = Descripteur()

t = Planete("Terre")
print(t.nomPlanete)
t.nomPlanete = 'Mars'
print(t.nomPlanete)


class Personne:
    def __init__(self, nom):
        self._val = nom
    nom = Descripteur()

p = Personne("Couture")
print(p.nom)
p.nom = "Coutu"
print(p.nom)

