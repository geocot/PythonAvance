#"Path" du fichier
cheminData = "donneesMoyAout.csv"
#Définition des listes
tempMoy = []
lat = []

#lecture du fichier
with open(cheminData, "r") as fichier:
    for ligne in fichier:
            ville,temperatureMoy,latitude, source = ligne.split(";")
            if ville.strip() != "Ville":  # Omet la première ligne
                print(ville, temperatureMoy, latitude)
                tempMoy.append(float(temperatureMoy.replace(",", "."))) #Permet de mettre en décimal anglais
                lat.append(float(latitude.replace(",", "."))) #Permet de mettre en décimal anglais


print ("\nValeurs des listes\n",tempMoy, "\n", lat ,"\n")

#Étape 1
#Commençons par calculer la somme des valeurs de x (temp. moyenne).
x_sum = 0
# calcul somme
for xi in tempMoy:
    x_sum += xi
# affichage
print("Somme des valeurs de x = ", x_sum)

#Même chose pour la somme des valeurs de latitudes et des valeurs de temp. moyenne au carré.
y_sum = 0.
for yi in lat:
    y_sum += yi
print("Somme des valeurs de y = ", y_sum, "\n")

#x carré
x2_sum = 0.
for xi in tempMoy:
    x2_sum += xi**2
print("somme des valeurs de x^2 = ", x2_sum, "\n")


#Il reste à calculer la somme des produits x(latitudes)×y(temp. moyenne).
#Pour parcourir à la fois la liste des valeurs de x(latitudes) et de y(temp. moyenne) on utilise la fonction zip qui joint deux listes.
for xi, yi in zip(tempMoy, lat):
    print("xi = ", xi, "\tyi = ", yi)

#Caluler la somme
xy_sum = 0.
for xi, yi in zip(tempMoy, lat):
    xy_sum += xi * yi
print("\nsomme des valeurs de x*y = ", xy_sum)

#Maintenant que nous disposons de toutes les valeurs nécessaires,
#il ne reste plus qu’à calculer aa et bb. Nous avons encore besoin du nombre de points.
#La fonction len donne le nombre d’éléments d’une liste.
nbPoints = len(tempMoy)
print("\nNombre de points = ", nbPoints)

#D’après les équations de la régression linéaire
a = (nbPoints * xy_sum - x_sum * y_sum) / (nbPoints * x2_sum - x_sum**2)
print("\na = ", a)

b = (x2_sum * y_sum - x_sum * xy_sum) / (nbPoints * x2_sum - x_sum**2)
print("\nb = ", b)

#Partie 2: Représentation graphique
#Import du  module
import matplotlib.pyplot as plt
#préparation du graphique
plt.plot(tempMoy, lat, "bo", label="Données") # Les points (x, y) représentés par des points
plt.plot( # droite de regression
    [tempMoy[0], tempMoy[-1]],                  # Valeurs de x(latitudes)
    [a * tempMoy[0] + b, a * tempMoy[-1] + b],  # Valeurs de y(temp. moyenne)
    "r-",                           # Couleur rouge avec un trait continu
    label="Régression")             # Légende
plt.xlabel("Température moyenne") # Nom de l'axe x
plt.ylabel("Latitude") # Nom de l'axe y
plt.xlim(5, 25) # Échelle axe x
plt.ylim(45, 63) # Échelle axe x
plt.legend()
plt.title("Régression Lineaire") # Titre de graphique
plt.show()


