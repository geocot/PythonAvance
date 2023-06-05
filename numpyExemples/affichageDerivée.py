import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 100) #Début, fin et nombre de données
y = 2*x
y2 = x**2

plt.plot(x, y)
plt.plot(x,y2)
plt.show()

