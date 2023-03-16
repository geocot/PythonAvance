#Création d'un array
import numpy as np
tableau = np.array([1,2,3,4,5])

#Il est aussi possible de créer un array à partir d'une liste Python.
listePython = [10,20,30]
tableau2 = np.array(listePython)
print(tableau2.dtype) #Résultat: int32

listePython2 = [10,"20",30]
tableau3 = np.array(listePython2)
print(tableau3) #Résultat: ['10' '20' '30']

