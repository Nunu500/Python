calificacion = 1
sumatoria = 0 
contador = 0
while(calificacion != 0):
    calificacion = int(input("Ingrese calificacion: "))
    if(calificacion != 0):
        if(calificacion >= 1 and calificacion <=5):
            sumatoria = sumatoria + calificacion
            contador = contador + 1
        else:
            print("Dato invalido")
print("------------------------")
print(f"Promedio general: {sumatoria / contador}")