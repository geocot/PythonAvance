import matplotlib.pyplot as plt
x = [1,2,3]
y = [0,3,2]

x1 = [0,2,3]
y1 = [2,1,0]

plt.plot(x,y, x1, y1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Le graphique")
plt.legend(['Courbe 1', 'Courbe 2'])

plt.show()

