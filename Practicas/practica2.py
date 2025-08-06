#Escribir un programa para validar si los datos de acceso (usuario y contraseña) se encuentras en el diccionario.
#Validar a solo 3 intentos erroneos de contraseña utilizando el ciclo while.
usuarios = {"admin": "admin123", "Fernanfloo": "Chorizo"}
usuario = input("Ingrese su nombre de usuario: ")
if usuario in usuarios:
    intentos = 0
    while intentos < 3:
        contraseña = input("Ingrese contraseña")
        if contraseña == usuarios[usuario]:
            print("Acceso concedido :D")
            break
        else:
            intentos += 1
            print("Intente de nuevo :/.")
    else:
        print("Has alcanzado el maximo de intentos. Acceso denegado >:(")
else:    
     print("El usuario no existe.")   
        