# Crear una matriz bidimensional (3x3)
matriz = [
    [2, 4, 7],
    [9, 1, 6],
    [5, 8, 3]
]

# Valor que estamos buscando
valor_buscado = 7

# Inicializar variables para rastrear la posición del valor
fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break  # Detener la búsqueda una vez que se encuentra el valor
    if fila_encontrada != -1:
        break  # Salir del bucle exterior si se encuentra el valor

# Verificar si se encontró el valor y mostrar la posición
if fila_encontrada != -1:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")
