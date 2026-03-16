from multimethod import multimethod
import math

class PoligonoRegular:

    @multimethod
    def __init__(self):
        self.n = 3
        self.lado = 1
        self.x = 0
        self.y = 0

    @multimethod
    def __init__(self, n:int, lado:float):
        self.n = n
        self.lado = lado
        self.x = 0
        self.y = 0

    @multimethod
    def __init__(self, n:int, lado:float, x:float, y:float):
        self.n = n
        self.lado = lado
        self.x = x
        self.y = y

    def getPerimetro(self):
        return self.n * self.lado

    def getArea(self):
        return (self.n * (self.lado ** 2)) / (4 * math.tan(math.pi / self.n))


p1 = PoligonoRegular()
print("Perimetro:", p1.getPerimetro())
print("Area:", p1.getArea())

p2 = PoligonoRegular(6, 4)
print("Perimetro:", p2.getPerimetro())
print("Area:", p2.getArea())

p3 = PoligonoRegular(10, 4, 5.6, 7.8)
print("Perimetro:", p3.getPerimetro())
print("Area:", p3.getArea())
