professeurs = ["Martin", "Jean", "Alice", "Robert"]
nbEtudiants = [10,25,24,33]
zipResul = zip(professeurs,nbEtudiants)
for t in zipResul:
    print(t)

# Résultats:
# ('Martin', 10)
# ('Jean', 25)
# ('Alice', 24)
# ('Robert', 33)

# ou utiliser ceci:
for nb, prf in zip(nbEtudiants,professeurs):
    print("Professeurs :  %s     Nb.Étudiants : %d" % (prf,nb))