class Ajout():
    def __init__(self):
        #Initialisation du compteur.
        self.compteur = 0

    def __call__(self, valeur=None):
        #Méthode exécutée si l'objet est appelé comme une fonction.
        if valeur is not None:
            self.compteur += int(valeur)
        return self.compteur

    def reset(self):
        #Remise à zéro.
        self.compteur = 0

ajout = Ajout()
print(ajout(2)) #Résultat: 2
print(ajout(3)) #Résultat: 5


