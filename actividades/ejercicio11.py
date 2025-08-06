#Encuentra los numeros primos.
numero = 100
while True:
    bandera = 0
    for x in range(2,numero):
        if(numero % x == 0):
            bandera = 1
    if bandera == 0:
        print(f"Es primo: {numero}")
    numero = numero + 1
