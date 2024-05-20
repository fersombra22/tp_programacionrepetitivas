# Supongamos que una pareja adulta de conejos produce una nueva pareja de conejos
# cada mes y que cada pareja de conejitos llega a la adultez al cumplir un mes de vida.
# Si partimos entonces de una pareja recién nacida, al cabo de un mes tendremos una pareja adulta,
# 1 mes después habrá dos parejas (una adulta y una recién nacida) y así sucesivamente: 
# 0 mes 1 pareja recién nacida 
# 1 mes 1 pareja adulta 
# 2 meses 2 parejas (1 adulta y 1 recién nacida) 
# 3 meses 3 parejas (2 adultas y 1 recién nacida) 
# 4 meses 5 parejas (3 adultas y 2 recién nacidas) 
# Se trata entonces de escribir un programa que permita el ingreso de un número natural N y
# determine cuántos pares de conejos se habrán producido a partir de una sola pareja después de N meses,
# suponiendo que los conejos no son mortales y se siguen reproduciendo hasta el infinito. 

n = int(input("Ingrese el número de meses: "))
pareja_adulta = 0
pareja_nueva = 1
p=0
    
if n == 0:
        print(f"Después de: {n} meses, habrá 1 pareja nueva.")
elif n == 1:
        print(f"Después de: {n} meses, habrá 1 pareja adulta.")
else:
        for i in range(1, n + 1):
            parejas = pareja_adulta + pareja_nueva
            pareja_nueva = pareja_adulta
            pareja_adulta = parejas
            p = pareja_adulta + pareja_nueva
        print(f"Después de: {n} meses habra: {p} parejas. {pareja_adulta} adulta/s y {pareja_nueva} de recien nacidos).")