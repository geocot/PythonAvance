def uneFonction(texte, *args, **kwargs):
    print(texte) #Argument obligatoire
    if args: #Arguments optionnels
        print(args)
    if kwargs: #Arguments optionnels
        print(kwargs)

#Avec Args
#uneFonction() #Résultat: plantage
uneFonction("Allo")#Résultat: Allo
uneFonction("Allo", "1", 2, 3)
#Résultat: Allo
#          ('1',2,3)

#Avec Kwargs
uneFonction("Allo", valeur1 = 1, valeur2 = 2)
# Résultats: Allo
#            {'valeur1': 1, 'valeur2': 2}
