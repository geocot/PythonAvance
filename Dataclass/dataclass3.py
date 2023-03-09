from dataclasses import dataclass

@dataclass
class Personne:
    prenom:str
    nom:str
    anneeNais: int = 1960 #C'est pour mettre une valeur par défaut.

p = Personne("Robert", "Leclerc", 1984)

print(p) #Utilise la méthode magique __str__()
p2 = Personne("Robert", "Leclerc", 1984)

print(p==p2) #Utilise la méthode magique __eq__()


