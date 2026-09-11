
cola = []
contador_id = 1
 
 
def agregar_trabajo():
    global contador_id
    nombre = input("Nombre del documento a imprimir: ")
    paginas = int(input("Número de páginas: "))
 
    trabajo = {
        "id": contador_id,
        "nombre": nombre,
        "paginas": paginas
    }
 
    cola.append(trabajo)
    print("Trabajo agregado a la cola con ID:", contador_id)
    contador_id = contador_id + 1
 
 
def procesar_trabajo():
    if len(cola) == 0:
        print("No hay trabajos en la cola para imprimir.")
    else:
        trabajo = cola.pop(0) 
        print("Imprimiendo documento:", trabajo["nombre"])
        print("Páginas:", trabajo["paginas"])
        print("Trabajo con ID", trabajo["id"], "completado.")
 
 
def mostrar_cola():
    if len(cola) == 0:
        print("La cola de impresión está vacía.")
    else:
        print("--- Trabajos en espera ---")
        posicion = 1
        for trabajo in cola:
            print(posicion, "-> ID:", trabajo["id"], "| Documento:", trabajo["nombre"], "| Páginas:", trabajo["paginas"])
            posicion = posicion + 1
 
 
def mostrar_menu():
    print("\n===== COLA DE IMPRESIÓN =====")
    print("1. Agregar trabajo de impresión")
    print("2. Procesar (imprimir) siguiente trabajo")
    print("3. Ver trabajos en cola")
    print("4. Salir")
 
 

opcion = 0
 
while opcion != 4:
    mostrar_menu()
    opcion = int(input("Elige una opción: "))
 
    if opcion == 1:
        agregar_trabajo()
    elif opcion == 2:
        procesar_trabajo()
    elif opcion == 3:
        mostrar_cola()
    elif opcion == 4:
        print("Cerrando el simulador de impresión...")
    else:
        print("Opción no válida, intenta de nuevo.")
 
