print("Realiza un triangulo y cuadrado")
tamaño = int(input("Ingrese el tamaño de las figuras: "))
for x in range(1, tamaño + 1):
    print(" * " * x)
print(" ")
for x in range(tamaño):
    print(" * " * tamaño)

print("Realiza un triángulo y cuadrado huecos")
tamaño = int(input("Ingrese el tamaño de las figuras: "))

print("\nTriángulo hueco:")
for x in range(1, tamaño + 1):
    if x == 1:
        print(" * ")
    elif x == tamaño:
        print(" * " * x)
    else:
        print(" *" + "   " * (x - 2) + " *")

print("\nCuadrado hueco:")
for i in range(tamaño):
    if i == 0 or i == tamaño - 1:
        print(" * " * tamaño)
    else:
        print(" * " + "   " * (tamaño - 2) + " *")