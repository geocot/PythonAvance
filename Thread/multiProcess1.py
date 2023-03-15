#Fonction commune
def compteur(maximum, nom):
    n=0
    while n<maximum:
        n+=1
    print(f'Fin {nom}')

if __name__ == "__main__": #Sans ceci le multiprocesseur redémarre le script au complet

    ################
    ##Sans multiprocess###
    ################
    import time
    print('Début Sans Multiprocess')
    depart = time.time()
    compteur(100000000, 'Main')
    fin = time.time()
    print(f'Temps: {fin-depart} secs.')
    print('***********************')


    #avec multiprocess
    from multiprocessing import Process

    print('Début avec Multiprocess')
    processA = Process(target=compteur, args=(25000000, 'A'))
    processB = Process(target=compteur, args=(25000000, 'B'))
    processC = Process(target=compteur, args=(25000000, 'C'))
    processD = Process(target=compteur, args=(25000000, 'D'))

    depart = time.time()
    processA.start()
    processB.start()
    processC.start()
    processD.start()

    processA.join()
    processB.join()
    processC.join()
    processD.join()


    fin = time.time()
    print(f'Temps: {fin - depart} secs.')

