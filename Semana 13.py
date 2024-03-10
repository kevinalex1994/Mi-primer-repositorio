import random
# Definir las ciudades, días de la semana y semanas
ciudades = ['Esmeraldas', 'Santo Domingo', 'Loja']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = ['Semana 1', 'Semana 2', 'Semana 3']
# Generar datos aleatorios de temperaturas diarias para cada ciudad, día y semana
datos_temperaturas = [[[random.randint(20, 35) for _ in range(len(dias_semana))] for _ in range(len(ciudades))] for _ in range(len(semanas))]
# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad_index, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for semana_index, semana in enumerate(semanas):
        promedio_semana = sum(datos_temperaturas[semana_index][ciudad_index]) / len(datos_temperaturas[semana_index][ciudad_index])
        print(f"{semana}: {promedio_semana:.2f}°C")
def temperatura_promedio(ciudades_temperaturas):
    """
    Esta función calcula la temperatura promedio de un conjunto de ciudades.
    Args:
        ciudades_temperaturas (dict): Un diccionario que contiene nombres de ciudades como claves
                                      y listas de temperaturas como valores.
    Returns:
        dict: Un diccionario que contiene nombres de ciudades como claves
              y temperaturas promedio como valores.
    """
    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Creamos un diccionario de ciudades y temperaturas
ciudades_temperaturas = {
    "Esmeraldas": [22, 25, 26, 24, 23],
    "Santo Domingo": [28, 30, 29, 31, 27],
    "Loja": [21, 20, 22, 18, 19],
    "Cuenca": [32, 33, 34, 30, 32],
    "Quito": [26, 28, 27, 29, 25]
}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")