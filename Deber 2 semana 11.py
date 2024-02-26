def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, (i, j)
    return False, None

# Definir una matriz 3x3 con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Definir el valor a buscar
valor_a_buscar = 5

# Realizar la búsqueda en la matriz
encontrado, posicion = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if encontrado:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
