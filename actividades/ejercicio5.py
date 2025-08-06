num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 > num2:
    mayor = num1
elif num2 > num1:
    mayor = num2
else:
    print("ambos numeros son iguales: ", num1)
    if num1 % 2 == 0:
        print("Y es par.")
    else:
        print("Y es impar.")
        exit()

print("El numero mayor es:", mayor)
if mayor % 2 == 0:
    print("Es un numero par.")
else:
    print("Es un numero impar.")
    