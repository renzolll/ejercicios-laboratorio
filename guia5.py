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

# 11. Devuelve un conjunto con los números que están ordenados de menor a mayor
def numeros_ordenados_menor_a_mayor(conjunto):
    return sorted(conjunto)

# 12. Devuelve un conjunto con los números que están ordenados de mayor a menor
def numeros_ordenados_mayor_a_menor(conjunto):
    return sorted(conjunto, reverse=True)

# 13. Devuelve un conjunto con los números que están duplicados
def numeros_duplicados(conjunto):
    duplicados = set()
    unicos = set()
    for num in conjunto:
        if num in unicos:
            duplicados.add(num)
        else:
            unicos.add(num)
    return duplicados

# 14. Devuelve un conjunto con los números que no están duplicados
def numeros_no_duplicados(conjunto):
    return {num for num in conjunto if list(conjunto).count(num) == 1}

# 15. Devuelve un conjunto con los números primos y ordenados de menor a mayor
def numeros_primos_ordenados(conjunto):
    return sorted(numeros_primos(conjunto))

# 16. Devuelve un conjunto con las palabras que son palíndromos y están ordenadas de menor a mayor
def palindromos_ordenados(conjunto):
    palindromos_set = palindromos(conjunto)
    return sorted(palindromos_set)

# 17. Devuelve un conjunto con las palabras que tienen una longitud determinada y están ordenadas de menor a mayor
def palabras_longitud_ordenadas(conjunto, longitud):
    palabras_longitud_set = palabras_longitud_determinada(conjunto, longitud)
    return sorted(palabras_longitud_set)

# 18. Devuelve un conjunto con las palabras que contienen una letra determinada y están ordenadas de mayor a menor
def palabras_con_letra_ordenadas(conjunto, letra):
    palabras_con_letra_set = palabras_con_letra(conjunto, letra)
    return sorted(palabras_con_letra_set, reverse=True)

# 19. Devuelve un conjunto con los números que están ordenados de menor a mayor y que no están duplicados
def numeros_ordenados_no_duplicados(conjunto):
    numeros_ordenados = sorted(conjunto)
    return {num for num in numeros_ordenados if list(numeros_ordenados).count(num) == 1}

# 20. Devuelve un conjunto con las palabras que son palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor
def palindromos_longitud_ordenados(conjunto, longitud):
    palindromos_longitud_set = {palabra for palabra in conjunto if palabra == palabra[::-1] and len(palabra) == longitud}
    return sorted(palindromos_longitud_set)

# Ejemplo de uso:
if __name__ == "__main__":
    conjunto_numeros = {2, 3, 5, 7, 8, 10, 11, 13, 17, 19, 23, 2, 3, 5}
    conjunto_palabras = {"python", "level", "civic", "radar", "anagrama", "prueba", "palabra", "amor", "programación", "algoritmo"}

    print("10. Palabras con la letra 'a':", palabras_con_letra(conjunto_palabras, 'a'))
    print("11. Números ordenados de menor a mayor:", numeros_ordenados_menor_a_mayor(conjunto_numeros))
    print("12. Números ordenados de mayor a menor:", numeros_ordenados_mayor_a_menor(conjunto_numeros))
    print("13. Números duplicados:", numeros_duplicados(conjunto_numeros))
    print("14. Números no duplicados:", numeros_no_duplicados(conjunto_numeros))
    print("15. Números primos ordenados de menor a mayor:", numeros_primos_ordenados(conjunto_numeros))
    print("16. Palíndromos ordenados de menor a mayor:", palindromos_ordenados(conjunto_palabras))
    print("17. Palabras de longitud 7 ordenadas de menor a mayor:", palabras_longitud_ordenadas(conjunto_palabras, 7))
    print("18. Palabras con la letra 'a' ordenadas de mayor a menor:", palabras_con_letra_ordenadas(conjunto_palabras, 'a'))
    print("19. Números ordenados de menor a mayor y no duplicados:", numeros_ordenados_no_duplicados(conjunto_numeros))
    print("20. Palíndromos de longitud 5 ordenados de menor a mayor:", palindromos_longitud_ordenados(conjunto_palabras, 5))

