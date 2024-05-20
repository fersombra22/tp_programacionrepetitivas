# Dado el número natural N, ingresar N números naturales y calcular: 
# 	a) Valor mínimo ingresado en la lista 
# 	b) Cantidad de veces que se ingresaron dos números iguales en forma consecutiva 
# 	c) La cantidad máxima de números que se ingresaron en forma creciente en forma consecutiva. 
# 	d) Valor promedio de todos los números ingresados. 
n = int(input("Ingrese la cantidad de números naturales: "))
num = int(input("Ingrese el primer número natural: "))
minimo = num
cantidadConsecutivos = 0
maxConsecutivos = 0
suma = num
numeroAnterior = num
promedio = 0.0
for i in range(2, n + 1):
    num = int(input("Ingrese el siguiente número natural: "))
    if num < minimo:
        minimo = num
    if num == numeroAnterior:
        cantidadConsecutivos += 1
    if num > numeroAnterior:
        maxConsecutivos += 1
    else:
        maxConsecutivos = 0
    suma += num
    numeroAnterior = num
promedio = suma / n
print("El valor mínimo ingresado es:", minimo)
print("La cantidad de veces que se ingresaron dos números iguales consecutivos es:", cantidadConsecutivos)
print("La cantidad máxima de números que se ingresaron en forma creciente consecutiva es:", maxConsecutivos)
print("El valor promedio de todos los números ingresados es:", promedio)