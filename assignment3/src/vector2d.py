import math

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.polygon_num=0
        self.point_num=0

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def scale(self, scalar):
        return Vector2D(scalar * self.x, scalar * self.y)

    def abs(self, other):
        return math.sqrt((self.x-other.x) * (self.x-other.x) + (self.y-other.y) * (self.y-other.y))
