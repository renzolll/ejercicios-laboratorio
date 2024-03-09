# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Función que devuelve un conjunto con los números primos de un conjunto dado
def numeros_primos(conjunto):
    return {num for num in conjunto if es_primo(num)}

# Función que devuelve un conjunto con las palabras que comienzan con una letra determinada
def palabras_con_letra(conjunto, letra):
    return {palabra for palabra in conjunto if palabra.startswith(letra)}

# Función que devuelve un conjunto con los números divisibles por un número determinado
def numeros_divisibles(conjunto, divisor):
    return {num for num in conjunto if num % divisor == 0}

# Función que devuelve un conjunto con los números que están en ambos conjuntos
def interseccion_entre_conjuntos(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

# Función que devuelve un conjunto con los números que están en el primer conjunto pero no en el segundo
def diferencia_entre_conjuntos(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

# Función que devuelve un conjunto con los números que están en el segundo conjunto pero no en el primero
def diferencia_entre_conjuntos_inversa(conjunto1, conjunto2):
    return conjunto2.difference(conjunto1)

# Función que devuelve un conjunto con las palabras que son anagramas
def anagramas(conjunto):
    anagrama_set = set()
    for palabra in conjunto:
        ordenada = ''.join(sorted(palabra))
        for otra_palabra in conjunto:
            if palabra != otra_palabra and ordenada == ''.join(sorted(otra_palabra)):
                anagrama_set.add(palabra)
                anagrama_set.add(otra_palabra)
    return anagrama_set

# Función que devuelve un conjunto con las palabras que son palíndromos
def palindromos(conjunto):
    return {palabra for palabra in conjunto if palabra == palabra[::-1]}

# Función que devuelve un conjunto con las palabras que tienen una longitud determinada
def palabras_longitud_determinada(conjunto, longitud):
    return {palabra for palabra in conjunto if len(palabra) == longitud}

# Ejemplo de uso:
if __name__ == "__main__":
    # Conjuntos de ejemplo
    conjunto_numeros = {2, 3, 5, 7, 8, 10, 11, 13, 17, 19, 23}
    conjunto_palabras = {"python", "palabra", "prueba", "amor", "programación", "algoritmo", "anagrama", "civic", "level", "radar"}

    # Ejemplo de uso de las funciones
    print("Números primos:", numeros_primos(conjunto_numeros))
    print("Palabras que comienzan con la letra 'p':", palabras_con_letra(conjunto_palabras, 'p'))
    print("Números divisibles por 3:", numeros_divisibles(conjunto_numeros, 3))
    print("Intersección entre conjuntos:", interseccion_entre_conjuntos(conjunto_numeros, {2, 3, 5, 7, 11}))
    print("Diferencia entre conjuntos:", diferencia_entre_conjuntos(conjunto_numeros, {2, 3, 5, 7, 11}))
    print("Diferencia entre conjuntos inversa:", diferencia_entre_conjuntos_inversa(conjunto_numeros, {2, 3, 5, 7, 11}))
    print("Anagramas:", anagramas(conjunto_palabras))
    print("Palíndromos:", palindromos(conjunto_palabras))
    print("Palabras de longitud 7:", palabras_longitud_determinada(conjunto_palabras, 7))

# 10. Devuelve un conjunto con las palabras que contienen una letra determinada
def palabras_con_letra(conjunto, letra):
    return {palabra for palabra in conjunto if letra in palabra}

# 11. Función para obtener los números ordenados de menor a mayor de un conjunto de números
def numeros_ordenados_menor_a_mayor(conjunto):
    return sorted(conjunto)

# 12. Función para obtener los números ordenados de mayor a menor de un conjunto de números
def numeros_ordenados_mayor_a_menor(conjunto):
    return sorted(conjunto, reverse=True)

# 13. Función para obtener los números duplicados de un conjunto de números
def numeros_duplicados(conjunto):
    duplicados = set()
    unicos = set()
    for num in conjunto:
        if num in unicos:
            duplicados.add(num)
        else:
            unicos.add(num)
    return duplicados

# 14. Función para obtener los números que no están duplicados de un conjunto de números
def numeros_no_duplicados(conjunto):
    return conjunto - numeros_duplicados(conjunto)

# 15. Función para obtener los números primos y ordenados de menor a mayor de un conjunto de números
def numeros_primos_ordenados(conjunto):
    primos = numeros_primos(conjunto)
    return sorted(primos)

# 16. Función para obtener las palabras que son palíndromos y ordenadas de menor a mayor de un conjunto de palabras
def palindromos_ordenados(conjunto):
    return sorted(palindromos(conjunto))

# 17. Función para obtener las palabras de una longitud determinada y ordenadas de menor a mayor de un conjunto de palabras
def obtener_palabras_longitud(palabras, longitud_deseada):
    # Filtrar las palabras que tienen la longitud deseada
    palabras_filtradas = [palabra for palabra in palabras if len(palabra) == longitud_deseada]
    # Ordenar las palabras de menor a mayor longitud
    palabras_ordenadas = sorted(palabras_filtradas, key=len)
    return palabras_ordenadas

# 18. Función para obtener las palabras que contienen una letra determinada y están ordenadas de mayor a menor de un conjunto de palabras
def palabras_con_letra_ordenadas_mayor_a_menor(conjunto, letra):
    palabras_filtradas = palabras_con_letra(conjunto, letra)
    return sorted(palabras_filtradas, reverse=True)

# 19. Función para obtener los números ordenados de menor a mayor y no duplicados de un conjunto de números
def numeros_ordenados_no_duplicados(conjunto):
    return sorted(numeros_no_duplicados(conjunto))

# 20. Función para obtener las palabras que son palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor de un conjunto de palabras
def palindromos_longitud_ordenados(conjunto, longitud):
    palindromos_filtrados = palindromos_ordenados(conjunto)
    return [palabra for palabra in palindromos_filtrados if len(palabra) == longitud]



