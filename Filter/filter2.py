listePrenoms= ["Alice", "Robert", "Martin", "Véronique"]
for p in filter(lambda prenom:prenom.startswith("M"), listePrenoms):
    print(p)
# Résultat:
# Martin



