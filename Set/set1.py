ensemble = {1,2,"Rouge", "Rouge", (1,2),(3,4)}
ensemble.update([10,"Bleu"])
print(ensemble)
#Résultat: {'Bleu', 1, 2, (1, 2), (3, 4), 10, 'Rouge'}
print(type(ensemble))
#Résultat: <class 'set'>
print(len(ensemble))
#Résultat: 7

