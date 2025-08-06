notas = []
for x in range(3):
    nota = 0
    while nota < 1 or nota > 5:
     nota = int(input(f"ingrese la nota {x+1}: "))
    notas.append(nota)
suma = 0
for x in range(len(notas)):
 suma = suma + notas[x]
promedio = suma / len(notas)
print(f"Promiedo: {suma / len(notas)} ")
if (promedio > 1.7):
   print("Aprobado ;)")
else:
  print("Reprobado :c")