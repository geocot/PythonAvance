def mulp2(nombre):
    return nombre * 2
print(callable(mulp2)) #Résultat: True

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return

    @property
    def y(self):
        return

p = Point(10,10)
print(callable(Point)) #Résultat: True
print(callable(p)) #Résultat: False

