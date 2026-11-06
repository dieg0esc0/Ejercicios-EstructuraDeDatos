tabla = [None] * 10

def hash_func(x):
    return x % 10

def insertar(x):
    pos = hash_func(x)
    contador = 0
    while contador < 10:
        indice = (pos + contador) % 10
        if tabla[indice] == None:
            tabla[indice] = x
            return
        contador = contador + 1
    print("La tabla está llena")

def buscar(x):
    pos = hash_func(x)
    contador = 0
    while contador < 10:
        indice = (pos + contador) % 10
        if tabla[indice] == None:
            return -1
        if tabla[indice] == x:
            return indice
        contador = contador + 1
    return -1

def mostrar():
    i = 0
    while i < 10:
        print(i, "->", tabla[i])
        i = i + 1


cantidad = int(input("¿Cuántos números vas a ingresar? "))
i = 0
while i < cantidad:
    num = int(input("Número de empleado: "))
    insertar(num)
    i = i + 1

mostrar()

num = int(input("Número a buscar: "))
resultado = buscar(num)
if resultado == -1:
    print("No se encontró")
else:
    print("Encontrado en la posición", resultado)