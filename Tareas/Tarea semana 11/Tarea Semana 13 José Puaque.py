#José Andrés Puaque
class circulo:
    def __init__ (self, radio):
        self.radio = radio
    def obtenerperimetro (self):
        return (2 * self.radio) * 3.1416
    def obtenerarea (self):
        return 3.1416 * (self.radio**2)
    def obtenervolumen (self):
        return (4 * 3.1416 * (self.radio**3)) / 3

CantidadC = int(input("Ingrese la cantidad de círculos que quiera mostrar: "))
for i in range(CantidadC):
    clase = circulo (float(input("Radio: ")))
    print ("Perímetro circulo", i+1, "=", clase.obtenerperimetro())
    print ("Área circulo", i+1, "=", clase.obtenerarea())
    print ("Volumen circulo", i+1, "=", clase.obtenervolumen())
    i = i + 1
    