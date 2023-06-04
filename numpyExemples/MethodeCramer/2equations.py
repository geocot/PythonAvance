import numpy as np
#Préparation de la matrice
matrice = np.array([[2,3], [-3,2]])
print(matrice)
'''
[[ 2  3]
[-3  2]]
'''
#Calcul du déterminant
detMatrice = np.linalg.det(matrice) #13
#Préparationn de la matrice x
matriceX = np.array([[8,3], [1,2]])
#Déterminant de la matrice x
detMatriceX = np.linalg.det(matriceX)
#Préparationn de la matrice y
matriceY = np.array([[2,8], [-3,1]])
#Déterminant de la matrice y
detMatriceY = np.linalg.det(matriceY)
print("X est :", detMatriceX/detMatrice)
print("Y est :", detMatriceY/detMatrice)


