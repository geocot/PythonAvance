from concurrent.futures import ThreadPoolExecutor
def mul2(nombre):
    return nombre *2

liste = [x for x in range(0,10)]

executor = ThreadPoolExecutor(max_workers=8)

#soumission avec submit
f = executor.submit(mul2, liste) #Affiche directement les informations
print(f.result(timeout=5)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



'''
#Soumission avec map
for result in executor.map(mul2, liste):
   print(result)
'''


'''
#Utilisation de map sans thread
for result in map(mul2, liste):
   print(result)
'''
