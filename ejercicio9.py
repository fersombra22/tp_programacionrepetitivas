#Realiza un script que escriba una pirámide de * de la  siguiente forma :
for i in range(1, 10):
    for a in range(1, i + 1):
        if i >= 1 and a == 1:
            print(1, end="")
        if i > 1 and (a == 2 or a == 3):
            print(2, end="")
        if i > 1 and (a == 3 or a == 4 or a == 5):
            print(3, end="")
        if i > 1 and (a == 6 or a == 7 or a == 8 or a == 9):
            print(4, end="")
    print("")