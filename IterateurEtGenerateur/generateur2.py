def plagePersonalisee(minimum, maximum):
    "Permet à un usager de créer une plage personnalisée"
    for n in range(minimum,maximum):
        yield n

for n in plagePersonalisee(2,10):
    print(n)  #Résultat: 2,3,4,..9

