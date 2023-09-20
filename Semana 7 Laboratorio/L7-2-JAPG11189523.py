print("Ejercicio 3: Jerarquía de operaciones")

Num1= input("Ingrese un número ")
Num2= input("Ingrese un segundo número ")
Num3= input("Ingrese un tercer número ")

NUM1=int(Num1)
NUM2=int(Num2)
NUM3=int(Num3)

print("A continuación se presentan las operaciones a realizar")
print ("a","*","b","+","c","=","1")
print("a","*","(","b","+","c",")","=","2")
print("a","/","(","b","*","c",")","=","3")
print("(","3","*","a",")","+","(","2","*","b",")","/","(","c","**","2",")","=","4")
print("Fórmula cuadrática = 5")
print("Coloque 6 para cerrar la calculadora")

CondicionINT=0 
while CondicionINT!=6:
    Condicion=input("De acuerdo con el menú desplegable, seleccione una operación a realizar ")
    CondicionINT=int(Condicion)
    if CondicionINT==1:
        print (NUM1,"*",NUM2,"+",NUM3,"=", NUM1*NUM2+NUM3)
    elif CondicionINT==2:
        print (NUM1,"*","(",NUM2,"+",NUM3,")","=", NUM1*(NUM2+NUM3))
    elif CondicionINT==3:
        print (NUM1,"/","(",NUM2,"*",NUM3,")","=", NUM1/(NUM2*NUM3))
    elif CondicionINT==4:
        print ("(","3","*",NUM1,")","+","(","2","*",NUM2,")","/","(",NUM3,"**","2",")","=", ((NUM1*3)+(NUM2*2))/(NUM3**2))
    elif CondicionINT==5:
        if NUM1!=0 and (NUM2**2)-(4*NUM1*NUM3)>=0:
            print ("(","(","-",NUM2,")","+","-","(","(","(",NUM2,"**","2",")","-","(","4","*",NUM1,"*",NUM3,")",")","**","0.5",")",")","/", "(","2","*",NUM1,")","=",
                "X1","=",(((-NUM2)+((NUM2**2)-(4*NUM1*NUM3))**0.5)/(NUM1*2)),
                "X2","=",(((-NUM2)-((NUM2**2)-(4*NUM1*NUM3))**0.5)/(NUM1*2)))
        else:
            print("No es posible realizar la formula cuadrática, asegurarse que los datos ingresados den una solución real o que la raíz no sea negativa.")
    elif CondicionINT==6:
        print("Muchas gracias, vuelva pronto")
    else:
        print("La opción que seleccionó, no es válida")