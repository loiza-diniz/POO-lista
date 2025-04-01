import math

class domino:
    def __init__(self, Lado_a = 0, Lado_b = 0):
        self.Lado_a = Lado_a
        self.Lado_b = Lado_b

    def mostrar_pontos(self):
        print("lado A: {self.Lado_a} lado B: {self.Lado_b}")

    def valor(self):
        return self.Lado_a + self.Lado_b