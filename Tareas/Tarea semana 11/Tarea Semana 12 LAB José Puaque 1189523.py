#José Andrés Puaque Guerra 1189523

class Números:
    N1 = ""
    N2 = ""
    def __init__ (self):
        self.N1 = input ("Ingrese el primer número: ")
        self.N2 = input ("Ingrese el segundo número: ")
    
    def Valores (self):
        
        self.RESTA = (self.N1, "-", self.N2, "=", int(self.N1)-int(self.N2))
        self.MULTI = (self.N1, "*", self.N2, "=", int(self.N1)*int(self.N2))
        self.DIV = (self.N1, "/", self.N2, "=", int(self.N1)/int(self.N2))
    
    def Suma(self):
        return float(self.N1), "+", float(self.N2), "=", float(self.N1)+float(self.N2)
    def Resta (self):
        return float(self.N1), "-", float(self.N2), "=", float(self.N1)-float(self.N2)
    def multi (self):
        return float(self.N1), "*", float(self.N2), "=", float(self.N1)*float(self.N2)
    def div (self):
        return float(self.N1), "/", float(self.N2), "=", float(self.N1)/float(self.N2)

Clase1 = Números ()
print ("Opciones: ")
print ("suma: 1")
print ("Resta: 2")
print ("Multiplicación: 3")
print ("Dividir: 4")
print ("Salir: 5")
NI = 0
while NI != 5:
    NI = float(input("Ingrese la opcion a elegir: "))
    if NI == 1:
        print (Clase1.Suma()) 
    elif NI == 2:
        print (Clase1.Resta())
    elif NI == 3:
        print (Clase1.multi())
    elif NI == 4:
        print (Clase1.DIV)
    elif NI == 5:
        print ("Gracias por usar el sistema")
    else:
        print ("Opción no válida, elegir una opción dentro del menú")
       





