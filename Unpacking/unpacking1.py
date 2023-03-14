# vecteur = (0,1,1)
# print("<", vecteur[0], vecteur[1], vecteur[2], ">")
# #Résultat: < 0 1 1 >

vecteur = (0,1,1)
def afficheVecteur(x,y,z):
    print(f"<{x},{y},{z}>")

afficheVecteur(*vecteur)
#Résultat: <0,1,1>

