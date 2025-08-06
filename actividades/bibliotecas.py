#Crear una aplicación Python que muestre una lista de aplicaciones de Windows y las permita invocar utilizando un dato ingresado por teclado. Las aplicaciones pueden ser el bloc de notas, la calculadora…
import os
while True:
     print("1. Calculadora")
     print("2. Chrome")
     print("0. Salir")
     opcion = input("Opcion: ")
     if(opcion == "1"):
          os.system("calc")
     elif( opcion == "2"):
          os.system("start chrome")
     elif( opcion == "0"):
          break
     else:
          print("????")
