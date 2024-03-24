# Diccionario
informacion_personal = {
'nombres':'Mirabá Suárez Kevin Alexander',
'edad':28,
'ciudad':'Quinindé',
'provincia':'Esmeraldas',
}

# Modificar el valor
informacion_personal['ciudad'] = 'La Unión'

# Agregar nueva clave:valor
informacion_personal['profesion'] = 'Estudiante'

# Verificar telefono y agregar
if 'telefono' in informacion_personal:
 print(informacion_personal['telefono'])
else:
 informacion_personal['telefono'] = '0969966956'

# Eliminar edad
informacion_personal.pop('edad')
print(informacion_personal)