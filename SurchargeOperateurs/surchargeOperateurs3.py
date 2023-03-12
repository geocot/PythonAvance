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

    def __add__(self, other):
        if type(other) == Point:
            self._x = self._x + other.x
            self._y = self._y + other.y
        if type(other) == int or type(other)==float:
            self._x = self._x + other
            self._y = self._y + other

        return self

    def __radd__(self, other):
        if type(other) == Point:
            self._x = self._x + other.x
            self._y = self._y + other.y

        if type(other) == int or type(other) == float:
            self._x = self._x + other
            self._y = self._y + other

            return self
    """
    La méthode __radd__() peut-être ramplacée par return self.__add__(other)
    """


    def __iadd__(self, other):
        if type(other) == Point:
            self._x = self._x + other.x
            self._y = self._y + other.y

        if type(other) == int or type(other) == float:
            self._x = self._x + other
            self._y = self._y + other

            return self

p1 = Point(1,1)
p2 = Point(2,2)
p1+=1
print(p1.x,p1.y)

