import time
liste = [x for x in range(100000)]

#Avec un objet immutable
depart = time.time()
resultat = ''
for n in liste:
    resultat = resultat + str(n)

#print(resultat)
fin = time.time()
print(f'Le temps est de {fin-depart} secondes.')

#Avec un objet mutable
depart = time.time()
resultat = []
for n in liste:
    resultat.append(str(n))

#print(resultat)
fin = time.time()
print(f'Le temps est de {fin-depart} secondes.')

