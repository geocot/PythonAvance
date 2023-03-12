class Point:
    "Point"
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __neg__(self):
        self._x *= -1
        self._y *= -1
        return  self

p1 = Point(1,1)
-p1
print(p1.x,p1.y)

