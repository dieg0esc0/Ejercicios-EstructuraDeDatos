

 
postres = {
    "pastel de chocolate": ["harina", "azucar", "cacao", "huevos", "mantequilla"],
    "flan": ["huevos", "leche condensada", "leche evaporada", "vainilla"],
    "gelatina": ["grenetina", "azucar", "agua", "colorante"],
}
 
 
def imprimir_ingredientes(nombre):
    nombre = nombre.lower().strip()
 
    if nombre not in postres:
        print(f"El postre '{nombre}' no existe.")
        return
 
    ingredientes = postres[nombre]
    if len(ingredientes) == 0:
        print(f"'{nombre}' no tiene ingredientes registrados.")
        return
 
    print(f"Ingredientes de '{nombre}':")
    contador = 1
    for ing in ingredientes:
        print(f"  {contador}. {ing}")
        contador = contador + 1
 
 
def agregar_ingrediente(nombre, ingrediente):
    nombre = nombre.lower().strip()
    ingrediente = ingrediente.lower().strip()
 
    if nombre not in postres:
        postres[nombre] = []
        print(f"Postre '{nombre}' creado.")
 
    if ingrediente in postres[nombre]:
        print(f"'{ingrediente}' ya estaba en '{nombre}'.")
        return
 
    postres[nombre].append(ingrediente)
    print(f"Se agrego '{ingrediente}' a '{nombre}'.")
 
 
def eliminar_ingrediente(nombre, ingrediente=""):
    nombre = nombre.lower().strip()
 
    if nombre not in postres:
        print(f"El postre '{nombre}' no existe.")
        return
 
    if ingrediente == "":
        postres[nombre] = []
        print(f"Se eliminaron todos los ingredientes de '{nombre}'.")
        return
 
    ingrediente = ingrediente.lower().strip()
    if ingrediente in postres[nombre]:
        postres[nombre].remove(ingrediente)
        print(f"Se elimino '{ingrediente}' de '{nombre}'.")
    else:
        print(f"'{ingrediente}' no estaba en '{nombre}'.")
 
 
def menu():
    while True:
        print("\n--- Gestor de postres ---")
        print("1. Ver ingredientes de un postre")
        print("2. Agregar ingrediente")
        print("3. Eliminar un ingrediente")
        print("4. Eliminar todos los ingredientes de un postre")
        print("5. Salir")
 
        opcion = input("Elige una opcion: ")
 
        if opcion == "1":
            nombre = input("Nombre del postre: ")
            imprimir_ingredientes(nombre)
 
        elif opcion == "2":
            nombre = input("Nombre del postre: ")
            ingrediente = input("Ingrediente a agregar: ")
            agregar_ingrediente(nombre, ingrediente)
 
        elif opcion == "3":
            nombre = input("Nombre del postre: ")
            ingrediente = input("Ingrediente a eliminar: ")
            eliminar_ingrediente(nombre, ingrediente)
 
        elif opcion == "4":
            nombre = input("Nombre del postre: ")
            eliminar_ingrediente(nombre)
 
        elif opcion == "5":
            print("Saliendo...")
            break
 
        else:
            print("Opcion invalida, intenta de nuevo.")
 
 
menu()
 
