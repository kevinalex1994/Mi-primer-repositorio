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