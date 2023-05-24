# Multiplication
class Nombre:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        # Seulement un nombre peut être ajouté
        if not isinstance(other, Nombre):
            return NotImplemented
        return Nombre(other.a + self.a, other.b + self.b)

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        return Nombre(self.a * other, self.b * other)

    def __str__(self):
        return "{},{}".format(self.a, self.b)

a = Nombre(2, 4)
print(a * 5)  # Retourne 10, 20

