import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 100)
y = 2*x
y2 = x**2

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x,y2)
plt.show()