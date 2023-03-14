def exposant(e, *args, **kwargs):
    print(f"L'exposant est {e}") #Argument obligatoire
    for nombre in args:
        print(f"Le résultat de {nombre} exposant {e} est {nombre**e}")
    minimum = kwargs.get('minimum')
    maximum = kwargs.get('maximum')
    if minimum and maximum:
        for n in range(minimum, maximum):
            print(f"Le résultat de {n} exposant {e} est {n**e}")

exposant(2,1,7,minimum=10, maximum=14)

# Résultats:
# L'exposant est 2
# Le résultat de 1 exposant 2 est 1
# Le résultat de 7 exposant 2 est 49
# Le résultat de 10 exposant 2 est 100
# Le résultat de 11 exposant 2 est 121
# Le résultat de 12 exposant 2 est 144
# Le résultat de 13 exposant 2 est 169

