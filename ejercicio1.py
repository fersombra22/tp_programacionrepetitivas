# 1-Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("ingrese una palabra ")
i=0
for i in range(0,10,1) :
    print(f"{i} {palabra}")
