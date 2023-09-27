AccNUM=0
while AccNUM!= 3:
    print("\nMenú") #el \n es para un salto de línea, ya que al usar el comando end, se me colocaba en la misma línea. 
    print("1 = Factorial")
    print("2 = Secuencia de Fibonacci")
    print("3 = Salir")
    Accion= input("Del menú anterior elija una opción a realizar: ")
    AccNUM= int(Accion)
    if AccNUM<1 or AccNUM>3:
        print("Por favor seleccione un número válido")
    else:
        if AccNUM==1:
            Factorial=1
            OP1= input("Ingrese un número para calcular su factorial: ")
            OP1N=int(OP1)
            for I in range(1,OP1N+1):
                Factorial=Factorial*I
                I=I+1
            print("El factorial de", OP1N, "es", Factorial)
        elif AccNUM==2:
            OP2=input("Ingrese el número hasta donde quiera que llegue la sucesión Fibonacci: ")
            OP2N=int(OP2)
            N1=0
            N2=1 
            print(N1, N2, end=" ") #Definí e imprimí estas dos variables, ya que son los 2 primeros valores de la sucesión de Fibonacci y se me hace más fácil imprimirlos por separado
            for i in range(OP2N-2): #al igual que para el factorial, se define un for que recorra el número que definimos menos dos, esto ya que antes, definimos las 2 primeras variables, por lo que 2 iteraciones ya están hechas.
                N3=N1+N2 #aquí se suman los valores de N1 y N2 por lo que al inicio del ciclo tomará valor N3=1
                print(N3, end=" ") #imprimimos en consola el valor antes calculado, se usó el end para que se mostrará los valores impresos en una sola línea, así mismo, por esto se usó el \n al inicio del menú
                N1=N2 
                N2=N3 #aquí se dan nuevos valores a N1, a N2 y a N3 para continuar con el ciclo hasta llegar al valor de iteraciones colocadas en el rango
        elif AccNUM==3:
            print("Gracias por usar el programa")
