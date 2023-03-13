class PlagePersonalisee:
    "Permet à un usager de créer une plage personnalisée"
    def __init__(self, minimum, maximum):
        self._maximum = maximum
        self._minimum = minimum

    def __iter__(self):
        return self

    def __next__(self):
        if self._minimum < self._maximum:
            retour = self._minimum
            self._minimum +=1
            return retour
        else:
            raise StopIteration

for n in PlagePersonalisee(2,10):
    print(n)  #Résultat: 2,3,4,..9


