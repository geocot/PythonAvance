class PourcentageError(Exception):
    def __init__(self, valeur):
        Exception.__init__(self,valeur)
        #Ou utilise super().__init__(valeur)

def entrerPourcentage(valeur):
    if 0 <= valeur <= 100:
        return f"{valeur}%"
    else:
        raise PourcentageError("N'est pas entre 0 et 100")

print(entrerPourcentage(10)) #Résultat:10%
print(entrerPourcentage(125)) #Résultat:PourcentageError: N'est pas entre 0 et 100

