#Vidéo et explication disponible ici: https://youtu.be/vwAo6CCu0QA
listeTempMoy = []
listeLatitude = []

with open("donneesMoyAout.csv", "r") as fichierCSV:
    for ligne in fichierCSV:
        ville,tempMoy,latitude,source = ligne.split(";")
        if ville.strip() != "Ville":
            listeTempMoy.append(float(tempMoy.replace(",", ".")))
            listeLatitude.append(float(latitude.replace(",", ".")))

nbItems = len(listeTempMoy)

# X=Température moyenne
# Y=Latitude

#Somme des X
sommeX = 0
for x in listeTempMoy:
    sommeX += x

#Somme des Y
sommeY = 0
for y in listeLatitude:
    sommeY += y

#Somme des X2
sommeX2 = 0
for x in listeTempMoy:
    sommeX2 += x**2

#Somme XY
sommeXY = 0
for x, y in zip(listeTempMoy,listeLatitude):
    sommeXY += x*y

#Trouver a de y=ax+b
a = (nbItems*sommeXY - sommeX * sommeY) / (nbItems * sommeX2 - sommeX**2)
print("a:",a)
#Trouver b de y=ax+b
b = (sommeX2 * sommeY - sommeX * sommeXY)/(nbItems * sommeX2- sommeX**2)
print("b:",b)

import matplotlib.pyplot as plt
plt.plot(listeTempMoy,listeLatitude, "bo", label="Données")
plt.plot(
    [listeTempMoy[0],listeTempMoy[-1]],
    [a*listeTempMoy[0] + b, a * listeTempMoy[-1] + b],
    "r-",
    label="Droite"
)

plt.xlabel("Température moyenne")
plt.ylabel("Latitude")
plt.legend()
plt.title("Régression")
plt.show()
