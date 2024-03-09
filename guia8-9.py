#1. Validar la edad de un usuario.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def validar_edad(self, edad):
        current = self.head
        while current:
            if current.data == edad:
                return True
            current = current.next
        return False

# Ejemplo de uso:
edades_validas = LinkedList()
edades_validas.add(18)
edades_validas.add(21)
edades_validas.add(25)

edad_usuario = 21
if edades_validas.validar_edad(edad_usuario):
    print("La edad es válida.")
else:
    print("La edad no es válida.")
#2. Verificar el tipo de dato de una variable.
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def verificar_tipo(self, tipo):
        current = self.head
        while current:
            if isinstance(current.data, tipo):
                return True
            current = current.next
        return False

# Ejemplo de uso:
datos = LinkedList()
datos.add(10)
datos.add("cadena")
datos.add(3.14)

tipo_variable = str
if datos.verificar_tipo(tipo_variable):
    print(f"Se encontró al menos una variable de tipo {tipo_variable}.")
else:
    print(f"No se encontraron variables de tipo {tipo_variable}.")
#3. Validar el rango de una calificación.
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def validar_calificacion(self, calificacion):
        current = self.head
        while current:
            if current.data[0] <= calificacion <= current.data[1]:
                return True
            current = current.next
        return False

# Ejemplo de uso:
rangos_calificaciones = LinkedList()
rangos_calificaciones.add((0, 5))
rangos_calificaciones.add((6, 10))

calificacion = 7
if rangos_calificaciones.validar_calificacion(calificacion):
    print("La calificación es válida.")
else:
    print("La calificación no es válida.")
#4. Asegurar que una lista no esté vacía.
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def esta_vacia(self):
        return self.head is None

# Ejemplo de uso:
lista = LinkedList()
if lista.esta_vacia():
    print("La lista está vacía.")
else:
    print("La lista no está vacía.")
#5. Validar la igualdad de dos objetos.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def validar_igualdad(self, objeto):
        current = self.head
        while current:
            if current.data == objeto:
                return True
            current = current.next
        return False

# Ejemplo de uso:
objetos = LinkedList()
objetos.add([1, 2, 3])
objetos.add("cadena")
objetos.add(10)

objeto = "cadena"
if objetos.validar_igualdad(objeto):
    print("El objeto es igual a uno en la lista.")
else:
    print("El objeto no es igual a ninguno en la lista.")
#6. Asegurar que un ciclo while se ejecuta al menos una vez.
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def asegurar_while(self):
        if self.head is not None:
            current = self.head
            while True:
                # Aquí colocarías el código del ciclo while
                print("Ejecutando el ciclo while al menos una vez.")
                if current.next == self.head:
                    break
                current = current.next

# Ejemplo de uso:
circular_list = CircularLinkedList()
circular_list.add(1)
circular_list.add(2)
circular_list.add(3)

circular_list.asegurar_while()
#7. Asegurar que una función retorna un valor específico.
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def asegurar_retorno(self, valor_especifico):
        current = self.head
        while current:
            if current.data == valor_especifico:
                return True
            current = current.next
        return False

# Ejemplo de uso:
valores = LinkedList()
valores.add(10)
valores.add(20)
valores.add(30)

valor_especifico = 20
if valores.asegurar_retorno(valor_especifico):
    print("La función retorna el valor específico.")
else:
    print("La función no retorna el valor específico.")
#8. Validar el estado de una variable después de una operación.
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def validar_estado(self, estado_deseado):
        current = self.head
        while current:
            # Aquí colocarías la operación que cambia el estado
            current.data += 10
            if current.data == estado_deseado:
                return True
            current = current.next
        return False



###
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def buscar_nodo(self, valor):
        current = self.head
        while current:
            if current.data == valor:
                return current
            current = current.next
        return None

    def suma_nodos(self):
        suma = 0
        current = self.head
        while current:
            suma += current.data
            current = current.next
        return suma

    def longitud_lista(self):
        longitud = 0
        current = self.head
        while current:
            longitud += 1
            current = current.next
        return longitud

    def concatenar_listas(self, otra_lista):
        if not self.head:
            self.head = otra_lista.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = otra_lista.head

    def eliminar_duplicados(self):
        current = self.head
        valores = set()
        prev = None
        while current:
            if current.data in valores:
                prev.next = current.next
            else:
                valores.add(current.data)
                prev = current
            current = current.next

    def invertir_lista(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Ejemplo de uso:
lista = LinkedList()
lista.add(1)
lista.add(2)
lista.add(3)

# 10. Buscar nodo en la lista enlazada simple
valor_buscado = 2
nodo_encontrado = lista.buscar_nodo(valor_buscado)
if nodo_encontrado:
    print(f"El nodo con el valor {valor_buscado} fue encontrado en la lista.")
else:
    print(f"No se encontró ningún nodo con el valor {valor_buscado} en la lista.")

# 11. Suma de nodos
print("La suma de los nodos en la lista es:", lista.suma_nodos())

# 12. Longitud de la lista
print("La longitud de la lista es:", lista.longitud_lista())

# Ejemplo de otra lista enlazada
otra_lista = LinkedList()
otra_lista.add(4)
otra_lista.add(5)

# 13. Concatenar listas
lista.concatenar_listas(otra_lista)
print("La lista después de concatenar con otra lista:")
current = lista.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# 14. Eliminar duplicados
lista.add(3)  # Agregamos un valor duplicado
print("Lista antes de eliminar duplicados:")
current = lista.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
lista.eliminar_duplicados()
print("Lista después de eliminar duplicados:")
current = lista.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# 15. Invertir lista
print("Lista antes de invertir:")
current = lista.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
lista.invertir_lista()
print("Lista después de invertir:")
current = lista.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")