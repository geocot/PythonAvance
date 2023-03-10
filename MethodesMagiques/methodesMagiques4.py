class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        return 
    
    @x.setter
    def x(self, value):
        pass

    @property
    def y(self):
        return

    @y.setter
    def y(self, value):
        pass
        
    def __eq__(self, other):
        if self._y == other.y:
            if self._x == other.x:
                return True
        return False



