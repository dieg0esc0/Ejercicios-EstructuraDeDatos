class Vertice:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.grado = 0
        self.es_aislado = True

    
    def __str__(self):
        texto = self.nombre + " (grado: " + str(self.grado) + ")"
        if self.es_aislado == True:
            texto = texto + " [AISLADO]"
        return texto


class Arista:
    def __init__(self, nombre, id, extremo1, extremo2):
        self.nombre = nombre
        self.id = id
        self.extremo1 = extremo1
        self.extremo2 = extremo2

        
        if extremo1.id == extremo2.id:
            self.es_bucle = True
        else:
            self.es_bucle = False

    
    def es_paralela(self, otra):
        
        if self.id == otra.id:
            return False

        
        if self.extremo1.id == otra.extremo1.id and self.extremo2.id == otra.extremo2.id:
            return True

        
        if self.extremo1.id == otra.extremo2.id and self.extremo2.id == otra.extremo1.id:
            return True

        return False

    
    def incide_en(self, v):
        if self.extremo1.id == v.id or self.extremo2.id == v.id:
            return True
        return False

    
    def __str__(self):
        if self.es_bucle == True:
            return self.nombre + ": {" + self.extremo1.nombre + "} [BUCLE]"
        return self.nombre + ": {" + self.extremo1.nombre + ", " + self.extremo2.nombre + "}"


class Grafo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vertices = []
        self.aristas = []

    def agregar_vertice(self, v):
        self.vertices.append(v)

    def agregar_arista(self, a):
        self.aristas.append(a)

    
    def calcular_grado(self, v):
        grado = 0

        for a in self.aristas:
            if a.es_bucle == True and a.extremo1.id == v.id:
                grado = grado + 2
            elif a.es_bucle == False and a.incide_en(v) == True:
                grado = grado + 1

        v.grado = grado
        v.es_aislado = (grado == 0)
        return grado

    
    def calcular_grado_total(self):
        total = 0

        for v in self.vertices:
            total = total + self.calcular_grado(v)

        return total

    
    def obtener_adyacentes(self, v):
        adyacentes = []

        for a in self.aristas:
            if a.incide_en(v) == True:
                if a.es_bucle == True:
                    vecino = v
                elif a.extremo1.id == v.id:
                    vecino = a.extremo2
                else:
                    vecino = a.extremo1

                
                if vecino not in adyacentes:
                    adyacentes.append(vecino)

        return adyacentes

   
    def obtener_aristas_incidentes(self, v):
        incidentes = []

        for a in self.aristas:
            if a.incide_en(v) == True:
                incidentes.append(a)

        return incidentes

    
    def obtener_aristas_adyacentes(self, a):
        adyacentes = []

        for b in self.aristas:
            if b.id != a.id:
                if b.incide_en(a.extremo1) == True or b.incide_en(a.extremo2) == True:
                    adyacentes.append(b)

        return adyacentes

    
    def obtener_bucles(self):
        bucles = []

        for a in self.aristas:
            if a.es_bucle == True:
                bucles.append(a)

        return bucles

    
    def obtener_paralelas(self):
        paralelas = []

        for i in range(len(self.aristas)):
            for j in range(i + 1, len(self.aristas)):
                a1 = self.aristas[i]
                a2 = self.aristas[j]

                if a1.es_paralela(a2) == True:
                    paralelas.append("{" + a1.nombre + ", " + a2.nombre + "}")

        return paralelas

    
    def obtener_vertices_aislados(self):
        aislados = []

        self.calcular_grado_total()   

        for v in self.vertices:
            if v.es_aislado == True:
                aislados.append(v)

        return aislados

        
    def mostrar_tabla_extremos(self):
        print("\n--- Tabla Punto Extremo - Arista ---")
        print("| Arista | Puntos extremos")
        print("|--------|----------------")

        for a in self.aristas:
            if a.es_bucle == True:
                print("| " + a.nombre + "     | {" + a.extremo1.nombre + "} [BUCLE]")
            else:
                print("| " + a.nombre + "     | {" + a.extremo1.nombre + ", " + a.extremo2.nombre + "}")
    def __str__(self):
        return "Grafo [" + self.nombre + "]: |V| = " + str(len(self.vertices)) + ", |E| = " + str(len(self.aristas))



def imprimir_lista(titulo, lista):
    texto = ""
    for elemento in lista:
        texto = texto + str(elemento) + "   "
    print(titulo, texto)



g = Grafo("G1")

v1 = Vertice("v1", 1)
v2 = Vertice("v2", 2)
v3 = Vertice("v3", 3)
v4 = Vertice("v4", 4)
v5 = Vertice("v5", 5)

g.agregar_vertice(v1)
g.agregar_vertice(v2)
g.agregar_vertice(v3)
g.agregar_vertice(v4)
g.agregar_vertice(v5)

e1 = Arista("e1", 1, v1, v2)
e2 = Arista("e2", 2, v1, v3)
e3 = Arista("e3", 3, v1, v3)   
e4 = Arista("e4", 4, v2, v3)
e5 = Arista("e5", 5, v5, v5)  

g.agregar_arista(e1)
g.agregar_arista(e2)
g.agregar_arista(e3)
g.agregar_arista(e4)
g.agregar_arista(e5)

print(g)
g.mostrar_tabla_extremos()

print("\nGrado total:", g.calcular_grado_total())
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)

print()
imprimir_lista("Adyacentes de v1:", g.obtener_adyacentes(v1))
imprimir_lista("Adyacentes de v5:", g.obtener_adyacentes(v5))
imprimir_lista("Aristas incidentes en v3:", g.obtener_aristas_incidentes(v3))
imprimir_lista("Aristas adyacentes a e1:", g.obtener_aristas_adyacentes(e1))
imprimir_lista("Bucles:", g.obtener_bucles())
imprimir_lista("Paralelas:", g.obtener_paralelas())
imprimir_lista("Vértices aislados:", g.obtener_vertices_aislados())
