print("Ejercicio")

X= input("ingrese un número ")
Y= input("ingrese otro número ")
X1=int(X)
Y1=int(Y)
A= X1+Y1
B= X1-Y1
C= X1*Y1
D= X1/Y1
E=X1%Y1
F=X1**Y1
G=X1//Y1

print("A continuación se presentan las operaciones a realizar")
print ("Suma = 1")
print("Resta = 2")
print("Multiplicación = 3")
print("División = 4")
print("Módulo = 5")
print("Exponenciación = 6")
print("Cociente = 7")
print("Escriba 8 para cerrar la calculadora cuando desee")
CondiciónINT=0
while CondiciónINT != 8:
    Condición= input("De acuerdo al menú desplegable, seleccione la operación a realizar ")
    CondiciónINT=int(Condición)
    if CondiciónINT == 1:
        print (X1, "+", Y1, "=", A)
    elif CondiciónINT == 2:
        print (X1, "-", Y1, "=", B)
    elif CondiciónINT == 3:
        print (X1, "*", Y1, "=", C)
    elif CondiciónINT == 4:
        print (X1, "/", Y1, "=", D)
    elif CondiciónINT == 5:
        print (X1, "%", Y1, "=", E)
    elif CondiciónINT == 6:
        print (X1, "**", Y1, "=", F)
    elif CondiciónINT == 7: 
        print (X1, "//", Y1, "=", G)
    elif CondiciónINT ==8:
        print ("Muchas gracias, vuelva pronto")
    else:
        print("La opción que seleccionó, no es válida")
