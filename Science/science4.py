import numpy as np
#3 équations avec 3 inconnus avec la méthode de Cramer
#2x+y-2z=-3
#x+4y-2z=4
#3x-y+z=8

#La matrice ne doit pas avoir de déterminant = 0
#2 1 -2
#1 4 -2
#3 1 5
a = np.array([[2,1,-2],
              [1,4,-2],
              [3,-1,1]])
#Déterminant de A
determinantA = np.linalg.det(a)
print(f"Déterminant de a est {determinantA} et est différent de 0")

#Pour trouver X
xa = np.array([[-3,1,-2],
               [4,4,-2],
               [8,-1,1]])

#Déterminant de XA
determinantXA = np.linalg.det(xa)
print(f"Déterminant de xa est {round(determinantXA)}")
print(f'La valeur de X est xa/a : {round(determinantXA/determinantA)}')

#Pour trouver Y
ya = np.array([[2,-3,-2],
              [1,4,-2],
              [3,8,1]])
#Déterminant de YA
determinantYA = np.linalg.det(ya)
print(f"Déterminant de ya est {round(determinantYA)}")
print(f'La valeur de Y est ya/a : {round(determinantYA/determinantA)}')

#Pour trouver Z
za = np.array([[2,1,-3],
              [1,4,4],
              [3,-1,8]])
#Déterminant de ZA
determinantZA = np.linalg.det(za)
print(f"Déterminant de za est {round(determinantZA)}")
print(f'La valeur de Z est za/a : {round(determinantZA/determinantA)}')