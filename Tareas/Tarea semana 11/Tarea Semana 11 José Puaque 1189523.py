#José Andrés Puaque Guerra 1189523

print ("Ejercicio de la semana 11")
Cadena = input ("Por favor ingrese una cadena de caracteres: ")
Contador1 = 0
Contador0 = 0
ContadorC = 0
for i in Cadena:
    if i == "1":
        Contador1 = Contador1 + 1
    elif i == "0":
        Contador0 = Contador0 + 1
    else:
        ContadorC = ContadorC + 1


print ("Cantidad 0: ", Contador0)
print ("Cantidad 1: ", Contador1)
print ("Otros caracteres: ", ContadorC)


