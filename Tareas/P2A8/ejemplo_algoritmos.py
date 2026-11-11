
def insercion(libros):
    lista = libros.copy()
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j]['titulo'] > actual['titulo']:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = actual
    return lista



def burbuja(productos):
    lista = productos.copy()
    for pasada in range(len(lista) - 1):
        for i in range(len(lista) - 1 - pasada):
            if lista[i]['precio'] > lista[i + 1]['precio']:
                temporal = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temporal
    return lista



def merge_sort(productos):
    if len(productos) <= 1:
        return productos.copy()

    mitad = len(productos) // 2
    izquierda = merge_sort(productos[:mitad])
    derecha = merge_sort(productos[mitad:])
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i]['precio'] <= derecha[j]['precio']:
            resultado.append(izquierda[i])
            i = i + 1
        else:
            resultado.append(derecha[j])
            j = j + 1

    
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i = i + 1
    while j < len(derecha):
        resultado.append(derecha[j])
        j = j + 1
    return resultado


libros = [
    {'id': 'L03', 'titulo': 'Pedro Páramo', 'ubicacion': 'A3'},
    {'id': 'L01', 'titulo': 'Don Quijote', 'ubicacion': 'A1'},
    {'id': 'L02', 'titulo': 'El principito', 'ubicacion': 'A2'},
]
productos = [
    {'sku': 'P03', 'nombre': 'Mouse', 'precio': 300},
    {'sku': 'P01', 'nombre': 'Teclado', 'precio': 500},
    {'sku': 'P02', 'nombre': 'Cable', 'precio': 100},
]

print('Libros por titulo:')
libros_ordenados = insercion(libros)
for libro in libros_ordenados:
    print(libro['titulo'])

print('Productos con burbuja:')
productos_ordenados = burbuja(productos)
for producto in productos_ordenados:
    print(producto['nombre'], producto['precio'])

print('Productos con Merge Sort:')
productos_ordenados = merge_sort(productos)
for producto in productos_ordenados:
    print(producto['nombre'], producto['precio'])


libros_por_id = {}
for libro in libros:
    codigo = libro['id']
    libros_por_id[codigo] = libro

productos_por_sku = {}
for producto in productos:
    codigo = producto['sku']
    productos_por_sku[codigo] = producto


codigo_buscado = 'L02'
if codigo_buscado in libros_por_id:
    print('Libro encontrado:', libros_por_id[codigo_buscado])
else:
    print('Libro no encontrado')

codigo_buscado = 'P03'
if codigo_buscado in productos_por_sku:
    print('Producto encontrado:', productos_por_sku[codigo_buscado])
else:
    print('Producto no encontrado')
