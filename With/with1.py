#Sans l’utilisation du with
fichier = open('cheminAcces', 'w')
try:
    fichier.write('Bonjour')
finally:
    fichier.close()

#Avec l’utilisation du with
with open('cheminAcces', 'w') as fichier:
    fichier.write('Bonjour')

