import math

# Función para realizar la suma, resta, multiplicación y división de dos números
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir entre cero"
    return suma, resta, multiplicacion, division

# Función para verificar si un número es par o impar
def verificar_par_impar(numero):
    return "Par" if numero % 2 == 0 else "Impar"

# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    return (base * altura) / 2

# Función para calcular el factorial de un número
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

# Función para invertir una cadena de texto
def invertir_cadena(cadena):
    return cadena[::-1]

# Función para calcular la suma de los números pares en un rango
def suma_numeros_pares(inicio, fin):
    suma = 0
    for i in range(inicio, fin + 1):
        if i % 2 == 0:
            suma += i
    return suma

# Función para generar una lista de cuadrados de los primeros n números naturales
def lista_cuadrados(n):
    return [i ** 2 for i in range(1, n + 1)]

# Función para contar el número de vocales en una cadena de texto
def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    return sum(1 for char in cadena if char in vocales)

# Función para generar los primeros n números de la serie Fibonacci
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

# Función para ordenar una lista de números de menor a mayor
def ordenar_lista(lista):
    return sorted(lista)

# Función para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

# Función para generar la tabla de multiplicar de un número
def tabla_multiplicar(numero):
    tabla = []
    for i in range(1, 11):
        tabla.append(numero * i)
    return tabla

# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * radio ** 2

# Función para calcular la suma de los dígitos de un número entero
def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma
