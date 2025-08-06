#Desarrollado por Manuel
edad = int(input("Ingrese su edad: "))
print(f"Usted tiene {edad}años.")
if edad >= 18 and edad < 60:
 print("Usted es mayor de edad, puede acceder a licencia de adulto.")
elif edad < 18 and edad >= 16:
 print("Usted es menor de edad, puede acceder a licencia de menor.")
else:
 print("Usted no puede obtener aun una licencia.")
 print("Vuelva dentro de 4 años.")