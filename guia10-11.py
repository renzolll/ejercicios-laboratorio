class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.primero:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo

    def duplicar_nodos(self):
        nodo_actual = self.primero
        while nodo_actual:
            nuevo_nodo = Nodo(nodo_actual.dato)
            siguiente = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = siguiente
            nuevo_nodo.anterior = nodo_actual
            if siguiente:
                siguiente.anterior = nuevo_nodo
            nodo_actual = siguiente

    def imprimir_adelante(self):
        nodo_actual = self.primero
        while nodo_actual:
            print(nodo_actual.dato, end=" ")
            nodo_actual = nodo_actual.siguiente
        print()

    def imprimir_atras(self):
        nodo_actual = self.ultimo
        while nodo_actual:
            print(nodo_actual.dato, end=" ")
            nodo_actual = nodo_actual.anterior
        print()

# Ejercicio 1
print("Ejercicio 1:")
lista_ejercicio_1 = ListaDoblementeEnlazada()
for dato in [1, 2, 3, 4]:
    lista_ejercicio_1.agregar(dato)
print("Lista original hacia adelante:")
lista_ejercicio_1.imprimir_adelante()
print("Lista original hacia atrás:")
lista_ejercicio_1.imprimir_atras()
lista_ejercicio_1.duplicar_nodos()
print("Lista duplicada hacia adelante:")
lista_ejercicio_1.imprimir_adelante()
print("Lista duplicada hacia atrás:")
lista_ejercicio_1.imprimir_atras()
print()

# Ejercicio 2
print("Ejercicio 2:")
lista_ejercicio_2 = ListaDoblementeEnlazada()
for dato in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    lista_ejercicio_2.agregar(dato)
print("Lista hacia adelante:")
lista_ejercicio_2.imprimir_adelante()
print("Lista hacia atrás:")
lista_ejercicio_2.imprimir_atras()
pares = 0
impares = 0
nodo_actual = lista_ejercicio_2.primero
while nodo_actual:
    if nodo_actual.dato % 2 == 0:
        pares += 1
    else:
        impares += 1
    nodo_actual = nodo_actual.siguiente
print("Cantidad de nodos pares:", pares)
print("Cantidad de nodos impares:", impares)
print()

# Ejercicio 3
print("Ejercicio 3:")
lista_ejercicio_3 = ListaDoblementeEnlazada()
for dato in [1, 2, 3, 4, 5]:
    lista_ejercicio_3.agregar(dato)
print("Lista original hacia adelante:")
lista_ejercicio_3.imprimir_adelante()
print("Lista original hacia atrás:")
lista_ejercicio_3.imprimir_atras()
nuevo_dato = 15
posicion = 3
nodo_nuevo = Nodo(nuevo_dato)
nodo_actual = lista_ejercicio_3.primero
for _ in range(1, posicion - 1):
    nodo_actual = nodo_actual.siguiente
nodo_nuevo.siguiente = nodo_actual.siguiente
nodo_actual.siguiente = nodo_nuevo
nodo_nuevo.anterior = nodo_actual
if nodo_nuevo.siguiente:
    nodo_nuevo.siguiente.anterior = nodo_nuevo
print("Lista con el nuevo nodo insertado hacia adelante:")
lista_ejercicio_3.imprimir_adelante()
print("Lista con el nuevo nodo insertado hacia atrás:")
lista_ejercicio_3.imprimir_atras()
print()

# Ejercicio 4
print("Ejercicio 4:")
lista_ejercicio_4 = ListaDoblementeEnlazada()
for dato in [1, 2, 2, 3, 3, 4, 5, 5]:
    lista_ejercicio_4.agregar(dato)
print("Lista original hacia adelante:")
lista_ejercicio_4.imprimir_adelante()
print("Lista original hacia atrás:")
lista_ejercicio_4.imprimir_atras()
nodos_set = set()
nodo_actual = lista_ejercicio_4.primero
while nodo_actual:
    if nodo_actual.dato not in nodos_set:
        nodos_set.add(nodo_actual.dato)
    else:
        nodo_anterior = nodo_actual.anterior
        nodo_siguiente = nodo_actual.siguiente
        if nodo_anterior:
            nodo_anterior.siguiente = nodo_siguiente
        if nodo_siguiente:
            nodo_siguiente.anterior = nodo_anterior
    nodo_actual = nodo_actual.siguiente
print("Lista sin nodos duplicados hacia adelante:")
lista_ejercicio_4.imprimir_adelante()
print("Lista sin nodos duplicados hacia atrás:")
lista_ejercicio_4.imprimir_atras()
print()

# Ejercicio 5
print("Ejercicio 5:")
lista_ejercicio_5 = ListaDoblementeEnlazada()
for dato in [1, 2, 3, 4, 5, 6]:
    lista_ejercicio_5.agregar(dato)
print("Lista original hacia adelante:")
lista_ejercicio_5.imprimir_adelante()
print("Lista original hacia atrás:")
lista_ejercicio_5.imprimir_atras()
nodo_actual = lista_ejercicio_5.primero
while nodo_actual:
    nodo_actual.siguiente, nodo_actual.anterior = nodo_actual.anterior, nodo_actual.siguiente
    nodo_actual = nodo_actual.anterior
lista_ejercicio_5.primero, lista_ejercicio_5.ultimo = lista_ejercicio_5.ultimo, lista_ejercicio_5.primero
print("Lista invertida hacia adelante:")
lista_ejercicio_5.imprimir_adelante()
print("Lista invertida hacia atrás:")
lista_ejercicio_5.imprimir_atras()




class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def ver_tope(self):
        return self.items[-1]

# Ejercicio 6: Invertir una cadena utilizando una pila
def invertir_cadena(cadena):
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()
    return cadena_invertida

# Ejercicio 7: Convertir número decimal a binario utilizando una pila
def decimal_a_binario(decimal):
    pila = Pila()
    while decimal > 0:
        residuo = decimal % 2
        pila.apilar(residuo)
        decimal //= 2
    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())
    return binario

# Ejercicio 8: Evaluar una expresión posfija utilizando una pila
def evaluar_expresion_posfija(expresion):
    pila = Pila()
    operadores = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y}
    for token in expresion.split():
        if token.isdigit():
            pila.apilar(int(token))
        else:
            segundo_numero = pila.desapilar()
            primer_numero = pila.desapilar()
            resultado = operadores[token](primer_numero, segundo_numero)
            pila.apilar(resultado)
    return pila.ver_tope()

# Ejercicio 9: Verificar operadores anidados utilizando una pila
def verificar_operadores_anidados(expresion):
    pila = Pila()
    for caracter in expresion:
        if caracter in "([{":
            pila.apilar(caracter)
        elif caracter in ")]}":
            if pila.esta_vacia():
                return False
            tope = pila.desapilar()
            if (caracter == ")" and tope != "(") or (caracter == "]" and tope != "[") or (caracter == "}" and tope != "{"):
                return False
    return pila.esta_vacia()

# Ejercicio 10: Ordenar una pila de manera ascendente utilizando estructuras adicionales
def ordenar_pila(pila):
    pila_auxiliar = Pila()
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        while not pila_auxiliar.esta_vacia() and pila_auxiliar.ver_tope() > elemento:
            pila.apilar(pila_auxiliar.desapilar())
        pila_auxiliar.apilar(elemento)
    return pila_auxiliar

# Ejercicio 11: Eliminar elementos duplicados de una pila
def eliminar_duplicados(pila):
    elementos_vistos = set()
    pila_resultado = Pila()
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in elementos_vistos:
            elementos_vistos.add(elemento)
            pila_resultado.apilar(elemento)
    return pila_resultado

# Ejercicio 12: Implementar una calculadora sencilla utilizando una pila
def calcular_expresion(expresion):
    pila = Pila()
    for token in expresion.split():
        if token.isdigit():
            pila.apilar(int(token))
        else:
            segundo_numero = pila.desapilar()
            primer_numero = pila.desapilar()
            if token == "+":
                pila.apilar(primer_numero + segundo_numero)
            elif token == "-":
                pila.apilar(primer_numero - segundo_numero)
            elif token == "*":
                pila.apilar(primer_numero * segundo_numero)
            elif token == "/":
                pila.apilar(primer_numero / segundo_numero)
    return pila.ver_tope()

# Ejercicio 13: Comprobar si una palabra o frase es un palíndromo utilizando una pila
def es_palindromo(palabra):
    pila = Pila()
    for caracter in palabra:
        pila.apilar(caracter.lower())
    palabra_invertida = ""
    while not pila.esta_vacia():
        palabra_invertida += pila.desapilar().lower()
    return palabra.lower() == palabra_invertida

# Ejercicio 14: Simular el proceso de deshacer (undo) utilizando dos pilas
class EditorTexto:
    def __init__(self):
        self.pila_acciones = Pila()
        self.pila_deshacer = Pila()
        self.texto = ""

    def escribir(self, texto):
        self.texto += texto
        self.pila_acciones.apilar(("escribir", texto))
        self.pila_deshacer = Pila()

    def deshacer(self):
        if not self.pila_acciones.esta_vacia():
            accion, texto = self.pila_acciones.desapilar()
            if accion == "escribir":
                self.texto = self.texto[:-len(texto)]
                self.pila_deshacer.apilar(("escribir", texto))

    def rehacer(self):
        if not self.pila_deshacer.esta_vacia():
            accion, texto = self.pila_deshacer.desapilar()
            if accion == "escribir":
                self.texto += texto
                self.pila_acciones.apilar(("escribir", texto))

    def obtener_texto(self):
        return self.texto

