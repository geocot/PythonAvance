def saisons():
        _saisons = ["printemps", "été", "automne", "hiver"]
        for n in range(0,4):
            yield _saisons[n]

for s in saisons():
    print(s)  #Résultat: printemps, été, automne, hiver

