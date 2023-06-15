from concurrent.futures import ThreadPoolExecutor
def mul2(nombre):
    return nombre *2

liste = [x for x in range(0,10)]
executor = ThreadPoolExecutor(max_workers=8)

#soumission avec submit
futures = [executor.submit(mul2, n) for n in liste] #Affiche directement les informations
for f in futures:
    print(f.result())# 0, 2, 4, 6, 8, 10, 12, 14, 16, 18



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
