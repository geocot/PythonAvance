listeNombre1 =[1,2,3,4,5]
listeNombre2 =[6,7,8,9,10]
listeNombre = [x * y for x,y in zip(listeNombre1,listeNombre2)]
print(listeNombre)
#Résultat: [6, 14, 24, 36, 50]

