import matplotlib.pyplot as plt
etiquettes = 'Chats', 'Chiens', 'Ratons', 'Souris'
data = [15, 30, 45, 10]
plt.pie(data, labels=etiquettes)
plt.show()
