#)Ingresar números enteros hasta que se ingrese uno negativo y
#contar cuántos de ellos fueron pares,
#cuántos impares y cuántos nulos.
pares = 0
impares = 0
nulos = 0

print("Ingrese numeros enteros (ingrese un numero negativo para detenerse):")
num = int(input())

while num >= 0:
    if num == 0:
        nulos += 1
    elif num % 2 == 0:
        pares += 1
    else:
        impares += 1
    num = int(input())

print("numeros pares:", pares)
print("numeros impares:", impares)
print("numeros nulos:", nulos)