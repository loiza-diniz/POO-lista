import math

class circle:
    def __init__(self, center: tuple, radius: float):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimetro(self):
        return 2 * math.pi * self.radius
    
    def test_pertencente(self, point: tuple):
        x_centro, y_centro = self.center    
        x_ponto, y_ponto = point

        distancia = math.sqrt((x_ponto - x_centro) ** 2 + (y_ponto - y_centro) ** 2)
        return distancia <= self.radius