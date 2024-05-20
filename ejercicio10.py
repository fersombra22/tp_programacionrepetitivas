#Dado el número natural N, ingresar N 
#números naturales y calcular la suma total de esos N números. 
n=int(input("ingrese la cantidad de numero naturales a sumar "))
suma=0

for i in range(1,n+1,1):
    print(F"ingrese el numero {i} ")
    num=int(input())
    suma=suma+num
print(F"ls dums total de los: {n} numero es: {suma} ")
