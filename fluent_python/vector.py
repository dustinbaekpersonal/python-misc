import math


class Vector:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.x + other.x
        return Vector(x, y)
    
    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    # def __bool__(self):
    #     return bool(abs(self))