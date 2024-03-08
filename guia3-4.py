
import numpy as np


# Ejercicio 1: Imprimir los números pares del 1 al 100
def numeros_pares(n=2):
    if n <= 100:
        print(n)
        numeros_pares(n + 2)

numeros_pares()

# Ejercicio 2: Imprimir la suma de los números del 1 al n
def suma_hasta_n(n):
    if n == 1:
        return 1
    else:
        return n + suma_hasta_n(n - 1)

print("La suma de los números del 1 al n es:", suma_hasta_n(100))

# Ejercicio 3: Imprimir la pirámide de números del 1 al n
def piramide_numeros(n):
    if n > 0:
        piramide_numeros(n - 1)
        print(" " * (n - 1) + "* " * (n))

piramide_numeros(5)

# Ejercicio 4: Imprimir la pirámide de números invertidos del 1 al n
def piramide_numeros_invertidos(n):
    if n > 0:
        print("* " * n)
        piramide_numeros_invertidos(n - 1)

piramide_numeros_invertidos(5)

# Ejercicio 5: Imprimir la tabla de multiplicar del n
def tabla_multiplicar(n, i=1):
    if i <= 10:
        print(f"{n} x {i} = {n*i}")
        tabla_multiplicar(n, i + 1)

tabla_multiplicar(5)



# Ejercicio 6: Crear una matriz de números reales de tamaño 100x100
matriz_reales = np.random.rand(100, 100)

# Ejercicio 7: Crear una matriz de números complejos
matriz_complejos = np.random.rand(5, 5) + np.random.rand(5, 5) * 1j

# Ejercicio 8: Crear una matriz de matrices
matriz_de_matrices = np.array([[np.random.rand(2, 2), np.random.rand(2, 2)],
                                [np.random.rand(2, 2), np.random.rand(2, 2)]])

# Ejercicio 9: Acceder al elemento central de una matriz
def elemento_central(matriz):
    filas, columnas = matriz.shape
    fila_central = filas // 2
    columna_central = columnas // 2
    return matriz[fila_central, columna_central]

print("Elemento central de la matriz de números reales:", elemento_central(matriz_reales))

# Ejercicio 10: Sumar dos matrices de diferentes tamaños
matriz1 = np.random.rand(3, 3)
matriz2 = np.random.rand(3, 3)
suma_matrices = matriz1 + matriz2

# Ejercicio 11: Multiplicar una matriz por un número
matriz_a_multiplicar = np.random.rand(3, 3)
numero = 5
matriz_multiplicada = matriz_a_multiplicar * numero

# Ejercicio 12: Calcular la media de los elementos de una matriz
media_matriz = np.mean(matriz_reales)

# Ejercicio 2 del Ejercicio parte 01:
# Calcular la mediana y la desviación estándar de los elementos de una matriz
mediana_matriz = np.median(matriz_reales)
desviacion_estandar_matriz = np.std(matriz_reales)

# Ejercicio 3 del Ejercicio parte 01:
# Encontrar el elemento máximo de una matriz
elemento_maximo = np.max(matriz_reales)

# Ejercicio 4 del Ejercicio parte 01:
# Encontrar la submatriz de mayor suma de una matriz
def submatriz_mayor_suma(matriz):
    filas, columnas = matriz.shape
    max_suma = float('-inf')
    indices = None

    for i in range(filas):
        for j in range(columnas):
            for k in range(i, filas):
                for l in range(j, columnas):
                    suma_actual = np.sum(matriz[i:k+1, j:l+1])
                    if suma_actual > max_suma:
                        max_suma = suma_actual
                        indices = ((i, j), (k, l))
    return indices

submatriz_indices = submatriz_mayor_suma(matriz_reales)
submatriz_mayor = matriz_reales[submatriz_indices[0][0]:submatriz_indices[1][0]+1, submatriz_indices[0][1]:submatriz_indices[1][1]+1]

# Ejercicio 5 del Ejercicio parte 01:
# Encontrar la matriz de covarianza de dos matrices
matriz_covarianza = np.cov(matriz_reales, matriz_reales.T)