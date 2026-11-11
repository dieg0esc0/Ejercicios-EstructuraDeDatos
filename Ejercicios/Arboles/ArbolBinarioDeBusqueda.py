class Nodo:
    def __init__(self, elemento):
        self.clave = elemento
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    
    def insertar(self, clave):
        self.raiz = self.insertar_rec(self.raiz, clave)

    def insertar_rec(self, raiz, clave):
        if raiz == None:
            return Nodo(clave)
        if clave < raiz.clave:
            raiz.izquierdo = self.insertar_rec(raiz.izquierdo, clave)
        elif clave > raiz.clave:
            raiz.derecho = self.insertar_rec(raiz.derecho, clave)
        return raiz

    
    def inorden(self):
        self.inorden_rec(self.raiz)

    def inorden_rec(self, raiz):
        if raiz != None:
            self.inorden_rec(raiz.izquierdo)
            print(raiz.clave, end=" ")
            self.inorden_rec(raiz.derecho)

    def preorden(self):
        self.preorden_rec(self.raiz)

    def preorden_rec(self, raiz):
        if raiz != None:
            print(raiz.clave, end=" ")
            self.preorden_rec(raiz.izquierdo)
            self.preorden_rec(raiz.derecho)

    def postorden(self):
        self.postorden_rec(self.raiz)

    def postorden_rec(self, raiz):
        if raiz != None:
            self.postorden_rec(raiz.izquierdo)
            self.postorden_rec(raiz.derecho)
            print(raiz.clave, end=" ")

    
    def buscar(self, clave):
        return self.buscar_rec(self.raiz, clave)

    def buscar_rec(self, raiz, clave):
        if raiz == None:                 
            return False
        if clave == raiz.clave:          
            return True
        if clave < raiz.clave:           
            return self.buscar_rec(raiz.izquierdo, clave)
        return self.buscar_rec(raiz.derecho, clave)   

    
    def eliminar(self, clave):
        self.raiz = self.eliminar_rec(self.raiz, clave)

    def eliminar_rec(self, raiz, clave):
        if raiz == None:                
            return None

        if clave < raiz.clave:
            raiz.izquierdo = self.eliminar_rec(raiz.izquierdo, clave)
        elif clave > raiz.clave:
            raiz.derecho = self.eliminar_rec(raiz.derecho, clave)
        else:
            
            if raiz.izquierdo == None and raiz.derecho == None:
                return None              
            if raiz.izquierdo == None:
                return raiz.derecho      
            if raiz.derecho == None:
                return raiz.izquierdo    

            
            raiz.clave = self.minimo(raiz.derecho)                    
            raiz.derecho = self.eliminar_rec(raiz.derecho, raiz.clave)  
        return raiz

    
    def minimo(self, raiz):
        while raiz.izquierdo != None:    
            raiz = raiz.izquierdo
        return raiz.clave



arbol = ArbolBinario()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(70)
arbol.insertar(60)
arbol.insertar(80)

print("Método auxiliar para encontrar el mínimo del subárbol de 70:")
print("Mínimo del subárbol de 70:", arbol.minimo(arbol.raiz.derecho))

print("Inorden:")
arbol.inorden()
print("\nPreorden:")
arbol.preorden()
print("\nPostorden:")
arbol.postorden()

clave_buscada = 40
print("\n\nBÚSQUEDA")
if arbol.buscar(clave_buscada):
    print("La clave", clave_buscada, "se encontró.")
else:
    print("La clave", clave_buscada, "no se encontró.")

print("\nELIMINACIÓN")
nodo = 20
arbol.eliminar(nodo)
print("Después de eliminar", nodo)
arbol.inorden()

nodo = 70
arbol.eliminar(nodo)
print("\nDespués de eliminar", nodo)
arbol.inorden()

nodo = 50
arbol.eliminar(nodo)
print("\nDespués de eliminar", nodo)
arbol.inorden()

