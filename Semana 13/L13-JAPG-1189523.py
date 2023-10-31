class circulo:
    def __init__ (self, radio):
        self.radio = radio
    def obtenerperimetro (self):
        return (2 * self.radio) * 3.1416
    def obtenerarea (self):
        return 3.1416 * (self.radio**2)
    def obtenervolumen (self):
        return (4 * 3.1416 * (self.radio**3)) / 3
clase1 = circulo(10)
print (clase1.obtenerperimetro())
print (clase1.obtenerarea())
print (clase1.obtenervolumen())