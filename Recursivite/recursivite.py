def factoriel(n):
    if (n == 0):
        # Cas de sortie
        return 1
    else:
        return n * factoriel(n - 1)


print(factoriel(5))

"""
Comme vous pouvez le voir ci-dessus, 
il existe une relation entre chaque scénario
factoriel consécutif. 

Vous devriez remarquer que factoriel (4) = 4 x factoriel (3).
De même, factorielle (5) = 5 x factorielle (4). 
"""

