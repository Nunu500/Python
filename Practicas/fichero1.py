texto = input('Introduce un texto')
nombre_fichero = 'archivo-' + texto + '.txt'
f= open(nombre_fichero, 'w')
f.write(f'{texto}\n')
f.close()