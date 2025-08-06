### String o cadenas de texto

nombre = "Tu nombre"
apellido = 'Apellido'

print(nombre + " " + apellido)

texto = "Este texto \n tiene salto de linea y \t tabulacion"
print(texto)

#Formateo

user, password, email = "CP", 12345, "admin@admin.com"
print("Su usuario y contraseña son {} {} y su email {}".format(user, password, email))
print("Su usuario y contraseña son %s %d y su email %s" % (user, password, email))
print("Su usuario y contraseña son " + user + " " + str(password) + " y su email" + email)
print(f"Su usuario y contraseña son {user} {password} y email {email}")
