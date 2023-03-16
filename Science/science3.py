#Création d'un array
import numpy as np
tab1 = np.array([1,2,3])
tab2 = np.array([4,5,6])
tab3 = np.array([[1,1,1],[1,1,1]])
print(tab1+tab2) #Résultat: [5 7 9]
print(tab1-tab2) #Résultat: [-3 -3 -3]
print(tab1*tab2) #Résultat: [ 4 10 18]
print(tab1*tab3) #Résultat: [[1 2 3] [1 2 3]]

