import math

class circle:
    def __init__(self, center: tuple, radius: float):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimetro(self):
        return 2 * math.pi * self.radius
    