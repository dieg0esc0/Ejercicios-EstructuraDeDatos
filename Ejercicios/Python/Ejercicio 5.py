nombre_archivo = input('Ingresa un nombre de archivo: ')
archivo = open(nombre_archivo)

contador = 0

for linea in archivo:
    palabras = linea.split()

    cantidad_palabras = len(palabras)

    if cantidad_palabras > 0:
        primera_palabra = palabras[0]

        if primera_palabra == 'From':
            segunda_palabra = palabras[1]
            print(segunda_palabra)
            contador = contador + 1

print('Hay', contador, 'lineas en el archivo con la palabra From al inicio')