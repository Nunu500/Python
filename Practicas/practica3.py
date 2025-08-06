diccionario = {
    "hola": "hello",
    "adios":"goodbye",
    "perro":"dog",
    "gato": "cat"
}
while True:
    palabra = input("Introduce una palabra en español (0 para salir):").lower()

    if palabra == "0":
        print("Traduccion finalizada.")
        break 
    if palabra in diccionario:
        print(f"La traduccion de '{palabra}' es '{diccionario[palabra]}'.")
    else:
        print(f"La palabra '{palabra}' no esta en el diccionario.")
        opcion = input("Deseas agregarla? (s/n):").lower()
        if opcion == "s":
            traduccion = input("Introduce la traduccion en ingles: ").lower()
            diccionario[palabra] = traduccion 
            print(f"Palabra agregada: {palabra} -> {traduccion}")