# Multiplication par la droite

class Nombre:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __rmul__(self, other):
        return  Nombre(self.a * other, self.b * other)

    def __str__(self):
        return "{},{}".format(self.a, self.b)

n1 = Nombre(2, 4)
print(5 * n1) # Retourne 10, 20
print(n1 * 5) # Plante