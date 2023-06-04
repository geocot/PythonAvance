class Point:
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

    def __str__(self):
        return "({},{})".format(self._x, self._y)

    def __eq__(self, other):
        if self._y == other.y:
            if self._x == other.x:
                return True
        return False
    def __add__(self, other):
        return Point(self._x + other.x,self._y + other.y )
    def __mul__(self, other):
        return Point(self._x * other.x, self._y * other.y)


p1 = Point(1,2)
p2 = Point(1,2)
print(p1*p2)
