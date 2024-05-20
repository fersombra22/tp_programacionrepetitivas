# 	15) Calcular los primeros N números primos. 
n = int(input("Ingrese un número: "))
num = 2

while n > 0:
    x = 1
    contador = 0
    
    while x <= num / 2:
        if num % x == 0:
            contador += 1
        x += 1
    if contador == 1:
        print("El número", num, "es primo")
        n -= 1
    num += 1
