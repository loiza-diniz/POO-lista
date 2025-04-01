import math

class Domino:
    def __init__(self, Lado_a = 0, Lado_b = 0):
        self.Lado_a = Lado_a
        self.Lado_b = Lado_b

    def mostrar_pontos(self):
        print("lado A: {self.Lado_a} lado B: {self.Lado_b}")

    def valor(self):
        return self.Lado_a + self.Lado_b
    
    def __str__(self):
        return "dominó ({self.lado_a}, {self.lado_b})"
    
    # teste
d1 = Domino(2, 6)
d2 = Domino(4, 3)

d1.mostrar_pontos()
d2.mostrar_pontos()

print("total de pontos: ", d1.valor() + d2.valor())
print(d1)