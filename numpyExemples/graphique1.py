import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.legend(['sin(x)', 'cos(x)'])
plt.show()

