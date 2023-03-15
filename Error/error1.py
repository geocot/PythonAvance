def entrerPourcentage(valeur):
    if 0 <= valeur <= 100:
        return f"{valeur}%"
    else:
        raise ValueError("N'est pas entre 0 et 100")

print(entrerPourcentage(10)) #Résultat:10%
print(entrerPourcentage(125)) #Résultat:ValueError