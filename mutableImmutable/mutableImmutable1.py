#La liste conserve le même id
liste = [1,2,3,4]
print(id(liste))
liste.append(5)
print(id(liste))

#La variable a change d'id
a=5
print(id(a))
a=7
print(id(a))

