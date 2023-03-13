# saisons = ["printemps", "été", "automne", "hiver"]
# for saison in saisons:
#     print(saison)

#Faire un itérable de saisons
class ISaisons:
    def __init__(self):
        self._compteur = -1
        self._saisons = ["printemps", "été", "automne", "hiver"]

    def __iter__(self):
        return self

    def __next__(self):
        self._compteur +=1
        if self._compteur>3:
            raise StopIteration
        return self._saisons[self._compteur]

for s in ISaisons():
     print(s)

"""
Ou utiliser 
s = ISaisons()
print(next(s))
"""
