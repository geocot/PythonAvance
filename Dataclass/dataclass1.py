from dataclasses import dataclass

@dataclass
class Personne:
    prenom:str
    nom:str
    anneeNais: int = 1960 #C'est pour mettre des valeurs par défaut.

p = Personne("Robert", "Leclerc", 1984)
p.nom = "Bob"
print(p.nom, p.prenom, p.anneeNais)
