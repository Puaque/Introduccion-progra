"""print("Hola mundo")
print("Soy Andres")


print("Hola mundo", end=" ")
print("soy Andres", end="")

La diferencia es que al usar end, hace un espacio pero nos coloca nuestra entrada en la misma linea, en cambio al no usar, se observa que es en la misma linea

Texto = input()
print(Texto + " hola")"""

print("Ingrese su nombre")
Texto= input()
print("Hola mundo")
print("soy " + Texto)

print("Hola mundo", end=" ")
print("soy " + Texto, end="")