from collections import deque
print("escribe una palabra palindorma: ")
palabra=input()
# 1. Verificar si una palabra es palíndroma utilizando una cola
def es_palindromo(palabra):
    cola = deque(palabra)
    while len(cola) > 1:
        if cola.popleft() != cola.pop():
            return False
    return True

print(es_palindromo(palabra))