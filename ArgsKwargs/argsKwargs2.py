def exposant(e, *args):
    print(f"L'exposant est {e}") #Argument obligatoire
    for nombre in args:
        print(f"Le résultat de {nombre} exposant {e} est {nombre**e}")

exposant(2,1,2,3,4)

# Résultats:
# L'exposant est 2
# Le résultat de 1 exposant 2 est 1
# Le résultat de 2 exposant 2 est 4
# Le résultat de 3 exposant 2 est 9
# Le résultat de 4 exposant 2 est 16

