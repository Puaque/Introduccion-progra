print("Menú")
print("1 = Factorial")
print("2 = Secuencia de Fibonacci")
print("3 = Salir")

Accion= input("Del menú anterior elija una opción a realizar: ")
AccNUM= int(Accion)
Factorial=1
if AccNUM==1:
    OP1= input("Ingrese un número para calcular su factorial: ")
    OP1N=int(OP1)
    for I in range(1,OP1N+1):
        Factorial=Factorial*I
        I=I+1
        print(OP1N,"=",OP1N,"*",I-1,"=",Factorial)
