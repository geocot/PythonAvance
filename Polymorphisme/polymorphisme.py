class Personne:
    def __init__(self, nom):
        self.nom = nom
    def affiche(self):
        print("je suis une personne")
class Etudiant(Personne):
    def __init__(self, nom, cne):
        super().__init__(nom)
        self.cne = cne
    def affiche(self):
        print("je suis un etudiant")
class Professeur(Personne):
    def __init__(self, nom, ppr):
        super().__init__(nom)
        self.ppr = ppr
    def affiche(self):
        print("je suis un professeur")


