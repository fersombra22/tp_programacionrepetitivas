#Algoritmo que imprima los primeros 10 números de la tabla del 2 (for)

tabla = int(input("Ingrese una tabla para conocer sus valores: "))
for i in range(1,11,1):
        print(tabla, "x", i, "=", i * tabla)