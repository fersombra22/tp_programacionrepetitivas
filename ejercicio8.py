#Realiza un programa que escriba una pirámide de * de la siguiente forma 
n=int(input("ingrese un numero para realizar la piramide "))

for a in range(1,n,1):
    for b in range(1,a,1):
        print("*", end="") 
    print("")

