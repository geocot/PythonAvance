#Fonction commune
def compteur(maximum, nom):
    n=0
    while n<maximum:
        n+=1
    print(f'Fin {nom}')

################
##Sans thread###
################
import time
print('Début Sans thread')
depart = time.time()
compteur(100000000, 'Main')
fin = time.time()
print(f'Temps: {fin-depart} secs.')
print('***********************')


#avec thread
import threading

print('Début avec thread')
threadA = threading.Thread(target=compteur, args=(25000000, 'A'))
threadB = threading.Thread(target=compteur, args=(25000000, 'B'))
threadC = threading.Thread(target=compteur, args=(25000000, 'C'))
threadD = threading.Thread(target=compteur, args=(25000000, 'D'))

depart = time.time()
threadA.start()
threadB.start()
threadC.start()
threadD.start()

threadA.join()
threadB.join()
threadC.join()
threadD.join()


fin = time.time()
print(f'Temps: {fin - depart} secs.')

