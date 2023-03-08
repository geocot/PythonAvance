class Personne:
    "Une classe personne"
    nbClasse = 0 #C'est une variable de classe car elle n'est pas précédée de self.
    def __init__(self, prenom, nom, courriel):
        self._prenom = prenom
        self._nom = nom
        self._courriel = courriel
        Personne.nbClasse+=1
    @classmethod
    def nbClassePersonne(cls):
        return "Le nombre de classe de Personne est de {}".format(cls.nbClasse)

    @classmethod #Surcharge du constructeur
    def from_string(cls, personne_str):
        prenom, nom, courriel = personne_str.split("-")
        return cls(prenom, nom, courriel)

    def __str__(self):
        return "Prénom: {}, Nom{}, Courriel{}".format(self._prenom, self._nom, self._courriel)

personne_str_1 = "Martin-Couture-aaa@aaa.ca"

personne1 = Personne.from_string(personne_str_1)
print(personne1)


