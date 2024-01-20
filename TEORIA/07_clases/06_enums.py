"""
Los Enums son una forma muy rápida de almacenar y acceder a valores. Se generan
a partir de clases y su uso puede ser muy útil a la hora de querer acceder a
ciertos datos.
"""

from enum import Enum


# Crear un Enum
class MyData(Enum):
    name = "Naia"
    username = "nlarrea"
    age = 25


# Acceder a los datos de un Enum
print(f"{MyData.username.name}: {MyData.username.value}")
""" Se imprime:
username: nlarrea
"""


"""
Para acceder a los valores se usa la siguiente sintaxis:

    enum_class_name.variable_name.value -> nlarrea

Para acceder al nombre de la variable, se sustituye 'name' por value:

    enum_class_name.variable.name -> username
"""

# Otro ejemplo:
print(f"{MyData.name.name}: {MyData.name.value}")
""" Se imprime:
name: Naia
"""


# Otro ejemplo práctico - almacenar funciones
"""
Vamos a usar un Enum para almacenar funciones, de la misma forma que lo hicimos
en el punto 04 de teoría de los diccionarios.

ENUNCIADO:
Vamos a usar un Enum para almacenar funciones. Estas funciones serán llamadas a
través de un bucle para obtener los tipos de datos de una serie de strings en
una lista, y almacenar estos resultados en un diccionario con el formato:
    
    tipo_de_dato: valor
"""

import re       # -> para el ejemplo que vamos a usar sólo

# Necesitaremos crear una clase para poder ejecutar las funciones
class FunctionProxy:
    """ Permitir llamar a las funciones. """

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)
    

class TypeOptions(Enum):
    """ Contiene las funciones a las que tendremos que llamar. """

    CodeValue = FunctionProxy(
        lambda value: value
        if re.match(r"(CD)+\d{6}", value)   # O cualquier tipo de cifrado que queramos usar
        else None
    )
    BooleanValue = FunctionProxy(
        lambda value: value.lower() == "true"
        if re.match(r"(true|false)", value, re.I)
        else None
    )
    NumericValue = FunctionProxy(
        lambda value: value
        if value.replace(".", "", 1).isnumeric()
        else None
    )
    NoValue = FunctionProxy(
        lambda value: "UN"
        if value == "-"
        else None
    )


# Definimos la lista de valores
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
for list_value in VALUES:
    for type_option in TypeOptions:
        returned_value = type_option.value(list_value)

        if not returned_value is None:
            values_with_types.append({
                type_option.name: returned_value
            })
            break

    if returned_value is None:
        values_with_types.append({
            "Undefined": list_value
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