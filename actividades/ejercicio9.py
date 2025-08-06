inicio = 0 
limite = 0
inicio = int(input("Ingrese el valor de inicio: "))
limite = int(input("Ingrese el valor del fin: "))
for x in range(inicio,limite):
    if x % 2 == 0:
        print(f" | {x}", end=" ")