#Chargement des enregistrements
with open('enregistrement.txt', 'r') as f:
    enregistrements = f.readlines()

#Fonction commune
def recherche(minimum, maximum, data, aRechercher, id):
    nombre = 0
    for e in data[minimum:maximum]:
        if int(e) == aRechercher:
            nombre+=1

    print(f'Fin {id}: {nombre} éléments trouvés')

if __name__ == "__main__": #Sans ceci le multiprocesseur redémarre le script au complet

    ################
    ##Sans multiprocess###
    ################
    import time
    print('Début Sans Multiprocess')
    depart = time.time()
    recherche(0, 6000000, enregistrements, 1111, 'Main')
    fin = time.time()
    print(f'Temps: {fin-depart} secs.')
    print('***********************')


    #avec multiprocess
    from multiprocessing import Process

    print('Début avec Multiprocess')

    processA = Process(target=recherche, args=(0, 3000000, enregistrements, 1111, 'A'))
    processB = Process(target=recherche, args=(3000001, 6000000, enregistrements, 1111, 'B'))
    depart = time.time()
    processA.start()
    processB.start()

    processA.join()
    processB.join()

    fin = time.time()
    print(f'Temps: {fin - depart} secs.')

