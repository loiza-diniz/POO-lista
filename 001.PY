import math

class Circle:
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
    
    def __str__(self):
        return f"P={self.perimetro()} ,\nA={self.area()}"

 #Teste
c1 = Circle((2, 2), 3)
print(c1)
print(c1.test_pertencente((0, 0)))  #true
print(c1.test_pertencente((0, -1)))  #false


    