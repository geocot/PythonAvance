import numpy as np

m = np.loadtxt("matrice.csv", delimiter=',', dtype=int)
print(m)

#Sauvegarde en format CSV
ms = np.array([[2,3,4],[1,6,6],[9,7,4]])
np.savetxt("test.csv",ms, delimiter=",", fmt="%i" )
"""
2,3,4
1,6,6
9,7,4
"""
