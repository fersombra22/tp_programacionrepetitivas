#dado un número natural “A”, generar la tabla de multiplicar de dicho número, empleando sólo sumas
a = int(input("Ingrese un número : "))
b = int(input("Ingrese un número para determinar la cantidad de veces que se repite: "))
resultado = 0

for i in range(1, b+1):
        resultado += a
        j = resultado - a
        print(f"La suma {i} es: {j} + {a} = {resultado} ")
c = a * b
print(f"La multiplicación de: {a} x {b}, es: {c} ")