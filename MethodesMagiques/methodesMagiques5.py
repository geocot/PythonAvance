class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Seulement un nombre peut être ajouté
        if not isinstance(other, Point):
            return NotImplemented
        return Point(other.x + self.x, other.y + self.y)

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        return Point(self.x * other, self.y * other)

    def __str__(self):
        return "{},{}".format(self.x, self.y)

a = Point(2, 4)
print(a * 5)  # Retourne 10, 20
