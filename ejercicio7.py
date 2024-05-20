# En los inicios de las redes de computadoras,
# cuenta la leyenda que se debían interconectar cada máquina con el resto de las computadoras
# utilizando un cable para cada conexión individual. El ejercicio consiste en determinar la cantidad
# de cables necesarios para conectar N computadoras utilizando contadores y acumuladores. 
# Ej) Para 2 computadoras, 1 cable.
# Para 3 computadoras, 3 cables.
# Para 4 computadoras, 6 cables.

n = int(input("Ingrese la cantidad de computadoras: "))
total_cables = 0
if n > 10 :
    n=int (input("ingrese un numero menor o igual a 10 " ))
elif n<=10:
   for i in range(2, n + 1):
        total_cables += i - 1
        print(f"Para {i}, computadoras se necesitan: {total_cables}, cables.")

n = int(input("Ingrese la cantidad de computadoras: "))
total_cables = 0
if n > 12 :
    n=int (input("ingrese un numero menor o igual a 10 " ))
elif n<=12:
   for i in range(2, n + 1):
        total_cables += i - 1
        print(f"Para {i}, computadoras se necesitan: {total_cables}, cables.")
