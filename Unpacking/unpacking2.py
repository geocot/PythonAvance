generateur = (x * x for x in range(3))

def afficheVecteur(x,y,z):
    print(f"<{x},{y},{z}>")

afficheVecteur(*generateur)
#Résultat: <0,1,4>

