nombre_archivo = input("Ingrese el nombre del archivo: ")
archivo = open(nombre_archivo)

palabras_lista = []

for linea in archivo:
    palabras = linea.split()
    for palabra in palabras:
        if palabras not in palabras_lista:
            palabras_lista.append(palabra)

palabras_lista.sort()
print(palabras_lista)

