# Dado el número natural N, calcular el factorial de N. 
# El factorial de N es la multiplicación de 1 hasta N.
# Por ejemplo, F(5)! = 1.2.3.4.5 = 120

N = int(input("Ingrese un numero que desea saber su factorial "))
factorial = 1
for i in range(1, N + 1):
        factorial *= i

print(f"El factorial de: {N} es: {factorial} ")