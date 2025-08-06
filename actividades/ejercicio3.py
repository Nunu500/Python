#operadores aritmeticos 
#imprimir la suma de 3+4
print("La suma de 10 + 4 es: ", 3+4)

#Resolver todas las operaciones: 10-4, 10*4, 10/4, 10%4, 10//4, 10**4

#Resolver la ecuacion cuadratica: 2x²-7x+3 = 0
a = 2
b = -7
c = 3

#Operaciones con cadenas de texto
print("SNPP     " + "CTFPPJ " + " PROGRAMACION PYTHON" )
#print("AULA" + 2102) #aqui tendremos un error, 2102 no es una cadena de texto, usar str()

#Operaciones mixtas
print("Tun chi" * 5) 
print("Ja " * (2 ** 3)) 

#Operadores de comparacion
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

#Operaciones con cadenas de texto
print("python" > "PYTHON")
print("aaaaa" >= "abaa") # Ordenacion alfabetica por ASCII  
print(len("aaaa") >= len("abaa")) # Cuenta caracteres

print("python" != "PYTHON")

### Operadores Logicos

print(10 > 4 and "Z" > "A")
print(10 > 4 or "Z" > "A")
print(not(10 > 4) and "Z" > "A")
