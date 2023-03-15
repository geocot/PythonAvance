import random
with open("enregistrement.txt", 'w') as f:
    for n in range (6000000):
        f.write(str(random.randrange(0,1000000))+"\n")


