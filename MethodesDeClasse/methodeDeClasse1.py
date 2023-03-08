class Personne:
    "Une classe personne"
    nbClasse = 0 #C'est une variable de classe car elle n'est pas précédée de self.
    def __init__(self, nom):
        self._nom = nom
        Personne.nbClasse+=1
    @classmethod
    def nbClassePersonne(cls):
        return "Le nombre de classe de Personne est de {}".format(cls.nbClasse)

p = Personne("Martin")
print(Personne.nbClassePersonne()) # ou
print(p.nbClassePersonne()) #Car Python cherche par la hiérarchie (objet, ensuite classe)

