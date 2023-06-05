import matplotlib.pyplot as plt
x = [1,2,3]
y = [1,3,2]


plt.bar(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Le graphique")
plt.legend(['Données'])

plt.show()