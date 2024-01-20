"""
Se pueden almacenar funciones dentro de diccionarios. Éstas podrían ser después
ejecutadas utilizando la siguiente sintaxis:

    diccionario["nombre_de_la_clave"](parámetros)

Esto puede no ser habitual de utilizar, pero es un concepto que puede ser
interesante de utilizar en determinadas ocasiones.
"""

# CASO PRÁCTICO:
# Vamos a utilizar este método para obtener el tipo de dato de diferentes
# variables en formato string almacenadas en una lista. De esta forma, vamos a
# generar una lista de diccionarios que sigan el siguiente formato:
#   { tipo_de_dato: valor }

import re

# Creamos el diccionario
TYPE_OPTIONS = {
    "CodeValue":
        lambda value: value
        if re.match(r"(CD)+\d{6}", value)   # O cualquier tipo de cifrado que queramos usar
        else None,
    "BooleanValue":
        lambda value: value.lower() == "true"
        if re.match(r"(true|false)", value, re.I)
        else None,
    "NumericValue":
        lambda value: value
        if value.replace(".", "", 1).isnumeric()
        else None,
    "NoValue":
        lambda value: "UN"
        if value == "-"
        else None
}

# Lista con valores a analizar
VALUES = [
    "3.14",
    "true",
    "False",
    "CD123456",
    "-",
    "another string"
]

# Lógica para obtener un diccionario con los tipos de valores
values_with_types = []
for value in VALUES:
    for option in TYPE_OPTIONS:
        returned_value = TYPE_OPTIONS.get(option, None)(value)

        if not returned_value is None:
            values_with_types.append({
                option: returned_value
            })
            break
    
    # Podemos definir una forma de gestionar otros valores que no deseemos
    # clasificar con las funciones utilizadas
    if returned_value is None:
        values_with_types.append({
            "Undefined": value
        })

# Mostrar el resultado por consola
for value_with_type in values_with_types:
    print(value_with_type)

""" Se imprime:
{'NumericValue': '3.14'}
{'BooleanValue': True}
{'BooleanValue': False}
{'CodeValue': 'CD123456'}
{'NoValue': 'UN'}
{'Undefined': 'another string'}
"""

# Al ser una lista con diccionarios, éstos datos pueden ser accesibles más
# adelante de forma muy simple.

# Otra forma de mostrar los datos por consola
for value_with_type in values_with_types:
    print(f" - {next(iter(value_with_type))}: {next(iter(value_with_type.values()))}")

""" Se imprime:
 - NumericValue: 3.14
 - BooleanValue: True
 - BooleanValue: False
 - CodeValue: CD123456
 - NoValue: UN
 - Undefined: another string
"""