# Ejercicio parte 01 – Colas:

class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        return self.items.pop(0)

    def frente(self):
        return self.items[0]

# 1. Verificar si una palabra es palíndroma
def es_palindroma(palabra):
    cola = Cola()
    for letra in palabra:
        cola.encolar(letra)
    while len(cola.items) > 1:
        if cola.desencolar() != cola.desencolar():
            return False
    return True

# 2. Sistema de gestión de pedidos
class SistemaGestionPedidos:
    def __init__(self):
        self.cola_pedidos = Cola()

    def agregar_pedido(self, pedido):
        self.cola_pedidos.encolar(pedido)

    def procesar_pedido(self):
        if not self.cola_pedidos.esta_vacia():
            return self.cola_pedidos.desencolar()
        else:
            return "No hay pedidos pendientes"

    def mostrar_estado_cola(self):
        if not self.cola_pedidos.esta_vacia():
            print("Pedidos pendientes:")
            for pedido in self.cola_pedidos.items:
                print(pedido)
        else:
            print("No hay pedidos pendientes")

# 3. Búsqueda de rutas en un laberinto (BFS)
from collections import deque

def buscar_camino_laberinto(laberinto, inicio, fin):
    visitado = set()
    cola = deque([(inicio, [])])
    while cola:
        actual, camino = cola.popleft()
        if actual == fin:
            return camino + [actual]
        if actual not in visitado:
            visitado.add(actual)
            for vecino in laberinto[actual]:
                cola.append((vecino, camino + [actual]))

# Ejercicios parte 02 - Árboles:

class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.hijo_izquierdo = None
        self.hijo_derecho = None

# 5. Contar nodos
def contar_nodos(arbol):
    if arbol is None:
        return 0
    return 1 + contar_nodos(arbol.hijo_izquierdo) + contar_nodos(arbol.hijo_derecho)

# 6. Contar nodos hoja
def contar_nodos_hoja(arbol):
    if arbol is None:
        return 0
    if arbol.hijo_izquierdo is None and arbol.hijo_derecho is None:
        return 1
    return contar_nodos_hoja(arbol.hijo_izquierdo) + contar_nodos_hoja(arbol.hijo_derecho)

# 7. Contar nodos internos
def contar_nodos_internos(arbol):
    if arbol is None or (arbol.hijo_izquierdo is None and arbol.hijo_derecho is None):
        return 0
    return 1 + contar_nodos_internos(arbol.hijo_izquierdo) + contar_nodos_internos(arbol.hijo_derecho)

# 8. Calcular altura del árbol
def altura_arbol(arbol):
    if arbol is None:
        return 0
    return 1 + max(altura_arbol(arbol.hijo_izquierdo), altura_arbol(arbol.hijo_derecho))

# 9. Calcular profundidad de un nodo
def profundidad_nodo(arbol, valor):
    return profundidad_nodo_aux(arbol, valor, 0)

def profundidad_nodo_aux(arbol, valor, profundidad_actual):
    if arbol is None:
        return None
    if arbol.dato == valor:
        return profundidad_actual
    izquierda = profundidad_nodo_aux(arbol.hijo_izquierdo, valor, profundidad_actual + 1)
    if izquierda is not None:
        return izquierda
    derecha = profundidad_nodo_aux(arbol.hijo_derecho, valor, profundidad_actual + 1)
    return derecha

# 10. Encontrar nodo mínimo
def encontrar_minimo(arbol):
    if arbol is None:
        return float('inf')
    min_izquierda = encontrar_minimo(arbol.hijo_izquierdo)
    min_derecha = encontrar_minimo(arbol.hijo_derecho)
    return min(arbol.dato, min_izquierda, min_derecha)

# 11. Encontrar nodo máximo
def encontrar_maximo(arbol):
    if arbol is None:
        return float('-inf')
    max_izquierda = encontrar_maximo(arbol.hijo_izquierdo)
    max_derecha = encontrar_maximo(arbol.hijo_derecho)
    return max(arbol.dato, max_izquierda, max_derecha)