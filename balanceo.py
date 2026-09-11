#Apuntes 4 de Septiembre 2026
def esta_balanceada(expresion):
    
    pila = []
    
    
    for letra in expresion:
        if letra == "()":
            pila.append(letra)
        elif letra == ")":
            pila.pop()
        return len(pila) == 0

print(esta_balanceada("x=(((y+2)*5)/2-5)*10"))
print(esta_balanceada("(()())"))