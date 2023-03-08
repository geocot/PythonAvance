class Personne:
    "Une classe personne"
    nbClasse = 0
    def __init__(self, nom):
        self._nom = nom
        Personne.nbClasse+=1

    def nbClassePersonne(cls):
        return "Le nombre de classe de Personne est de {}".format(cls.nbClasse)

p = Personne("Martin")
print(p.nbClassePersonne())