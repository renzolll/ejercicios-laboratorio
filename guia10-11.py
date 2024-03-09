class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

# 1. Crear una lista con al menos 4 nodos y duplicar cada nodo
def duplicar_nodos(lista):
    actual = lista
    while actual:
        duplicado = Nodo(actual.dato)
        duplicado.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = duplicado
        actual.siguiente = duplicado
        duplicado.anterior = actual
        actual = duplicado.siguiente

def imprimir_lista_adelante(lista):
    actual = lista
    while actual:
        print(actual.dato, end=" ")
        actual = actual.siguiente
    print()

def imprimir_lista_atras(lista):
    actual = lista
    while actual.siguiente:
        actual = actual.siguiente
    while actual:
        print(actual.dato, end=" ")
        actual = actual.anterior
    print()

# 2. Contar nodos pares e impares
def contar_nodos_pares_impares(lista):
    pares = 0
    impares = 0
    actual = lista
    while actual:
        if actual.dato % 2 == 0:
            pares += 1
        else:
            impares += 1
        actual = actual.siguiente
    return pares, impares

# 3. Insertar un nodo en posición específica
def insertar_nodo_posicion(lista, dato, posicion):
    nuevo_nodo = Nodo(dato)
    actual = lista
    for _ in range(posicion - 1):
        actual = actual.siguiente
    nuevo_nodo.siguiente = actual.siguiente
    if actual.siguiente:
        actual.siguiente.anterior = nuevo_nodo
    actual.siguiente = nuevo_nodo
    nuevo_nodo.anterior = actual

# 4. Eliminar nodos duplicados
def eliminar_nodos_duplicados(lista):
    nodos_vistos = set()
    actual = lista
    while actual:
        if actual.dato in nodos_vistos:
            actual.anterior.siguiente = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = actual.anterior
        else:
            nodos_vistos.add(actual.dato)
        actual = actual.siguiente

# 5. Invertir la lista
def invertir_lista(lista):
    actual = lista
    while actual.siguiente:
        actual = actual.siguiente
    while actual:
        print(actual.dato, end=" ")
        actual = actual.anterior
    print()

# Ejemplo de uso
# 1.
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)

nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3

duplicar_nodos(nodo1)
print("Lista original hacia adelante:")
imprimir_lista_adelante(nodo1)
print("Lista original hacia atrás:")
imprimir_lista_atras(nodo1)

# 2.
lista_numeros = Nodo(1)
for i in range(2, 10):
    nuevo_nodo = Nodo(i)
    actual = lista_numeros
    while actual.siguiente:
        actual = actual.siguiente
    actual.siguiente = nuevo_nodo
    nuevo_nodo.anterior = actual

print("Lista de números hacia adelante:")
imprimir_lista_adelante(lista_numeros)
print("Lista de números hacia atrás:")
imprimir_lista_atras(lista_numeros)

pares, impares = contar_nodos_pares_impares(lista_numeros)
print("Nodos pares:", pares)
print("Nodos impares:", impares)

# 3.
insertar_nodo_posicion(lista_numeros, 15, 3)
print("Lista con nodo insertado hacia adelante:")
imprimir_lista_adelante(lista_numeros)
print("Lista con nodo insertado hacia atrás:")
imprimir_lista_atras(lista_numeros)

# 4.
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(2)
nodo4 = Nodo(3)

nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3

print("Lista con nodos duplicados hacia adelante:")
imprimir_lista_adelante(nodo1)
eliminar_nodos_duplicados(nodo1)
print("Lista sin nodos duplicados hacia adelante:")
imprimir_lista_adelante(nodo1)

# 5.
lista_numeros = Nodo(1)
for i in range(2, 7):
    nuevo_nodo = Nodo(i)
    actual = lista_numeros
    while actual.siguiente:
        actual = actual.siguiente
    actual.siguiente = nuevo_nodo
    nuevo_nodo.anterior = actual


# Definición de la clase Pila
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

# 6. Utilizar una pila para invertir el orden de los caracteres de una cadena
def invertir_cadena(cadena):
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()
    return cadena_invertida

# 7. Convertir número decimal a binario utilizando una pila
def decimal_a_binario(decimal):
    pila = Pila()
    while decimal > 0:
        residuo = decimal % 2
        pila.apilar(str(residuo))
        decimal //= 2
    binario = ""
    while not pila.esta_vacia():
        binario += pila.desapilar()
    return binario

# 8. Evaluar una expresión matemática en notación posfija utilizando una pila
def evaluar_expresion_posfija(expresion):
    pila = Pila()
    operadores = {'+', '-', '*', '/'}
    for token in expresion.split():
        if token not in operadores:
            pila.apilar(int(token))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if token == '+':
                pila.apilar(operando1 + operando2)
            elif token == '-':
                pila.apilar(operando1 - operando2)
            elif token == '*':
                pila.apilar(operando1 * operando2)
            elif token == '/':
                pila.apilar(operando1 / operando2)
    return pila.desapilar()

# 9. Validar si los operadores en una expresión matemática están correctamente anidados
def validar_operadores_anidados(expresion):
    pila = Pila()
    for caracter in expresion:
        if caracter in "([{":
            pila.apilar(caracter)
        elif caracter in ")]}":
            if pila.esta_vacia():
                return False
            elif (caracter == ")" and pila.ver_tope() == "(") or (caracter == "]" and pila.ver_tope() == "[") or (caracter == "}" and pila.ver_tope() == "{"):
                pila.desapilar()
            else:
                return False
    return pila.esta_vacia()

#10 ordenar una pila de manera ascedente
def ordenar_pila_ascendente(pila):
    pila_auxiliar = []
    while pila:
        elemento = pila.pop()
        while pila_auxiliar and pila_auxiliar[-1] > elemento:
            pila.append(pila_auxiliar.pop())
        pila_auxiliar.append(elemento)
    while pila_auxiliar:
        pila.append(pila_auxiliar.pop())
# 11. Eliminar los elementos duplicados de una pila
def eliminar_duplicados_pila(pila):
    elementos_vistos = set()
    pila_temporal = Pila()
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in elementos_vistos:
            elementos_vistos.add(elemento)
            pila_temporal.apilar(elemento)
    while not pila_temporal.esta_vacia():
        pila.apilar(pila_temporal.desapilar())

# 12. Implementar una calculadora sencilla utilizando una pila para evaluar expresiones
def calcular_expresion(expresion):
    pila = Pila()
    for token in expresion.split():
        if token.isdigit():
            pila.apilar(int(token))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if token == '+':
                pila.apilar(operando1 + operando2)
            elif token == '-':
                pila.apilar(operando1 - operando2)
            elif token == '*':
                pila.apilar(operando1 * operando2)
            elif token == '/':
                pila.apilar(operando1 / operando2)
    return pila.desapilar()

# 13. Utilizar una pila para comprobar si una palabra o frase es un palíndromo
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    pila = Pila()
    for letra in palabra:
        pila.apilar(letra)
    palabra_invertida = ""
    while not pila.esta_vacia():
        palabra_invertida += pila.desapilar()
    return palabra == palabra_invertida

# 14. Implementar un sistema simple de "deshacer" utilizando dos pilas
class Deshacer:
    def __init__(self):
        self.acciones = Pila()
        self.deshaceres = Pila()

    def hacer(self, accion):
        self.acciones.apilar(accion)
        self.deshaceres = Pila()  # Reiniciar la pila de deshaceres después de una nueva acción

    def deshacer(self):
        if not self.acciones.esta_vacia():
            accion_deshacer = self.acciones.desapilar()
            self.deshaceres.apilar(accion_deshacer)
            return f"Deshecho: {accion_deshacer}"
        else:
            return "No hay acciones para deshacer"

    def rehacer(self):
        if not self.deshaceres.esta_vacia():
            accion_rehacer = self.deshaceres.desapilar()
            self.acciones.apilar(accion_rehacer)
            return f"Rehecho: {accion_rehacer}"
        else:
            return "No hay acciones para rehacer"

# Ejemplo de uso
# 11.
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(2)
pila.apilar(4)
print("Pila original:", pila.items)
eliminar_duplicados_pila(pila)
print("Pila sin duplicados:", pila.items)

# 12.
expresion = "3 4 + 5 *"
print("Resultado de la expresión:", calcular_expresion(expresion))

# 13.
palabra = "Anita lava la tina"
print(f"¿{palabra} es un palíndromo?:", es_palindromo(palabra))

# 14.
sistema_deshacer = Deshacer()
sistema_deshacer.hacer("Escribir texto")
sistema_deshacer.hacer("Borrar texto")
print(sistema_deshacer.deshacer())
print(sistema_deshacer.rehacer())

print("Lista original hacia adelante:")
imprimir_lista_adelante(lista_numeros)
print("Lista invertida hacia atrás:")
invertir_lista(lista_numeros)