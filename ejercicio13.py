#14) Dado un número natural N, verificar si es o no es primo. 
def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un número natural: "))

if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")