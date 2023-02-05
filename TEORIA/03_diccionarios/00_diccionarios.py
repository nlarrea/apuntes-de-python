# INTRODUCCIÓN A DICCIONARIOS
"""
los diccionarios son colecciones que almacenan datos utilizando pares de clave-
valor. Al igual que las listas, pueden contener cualquier tipo de dato en su
interior, pero esta vez se accede a los valores a través de las claves, no del
índice

SINTAXIS:
dictionary = {
    "key_1": value_1,
    "key_2": value_2
}

teniendo en cuenta que las claves deben ser integers o strings (lo cual es más
común que los integers), y que el valor puede ser cualquier tipo de dato
"""

# el diccionario más simple tendrá un único par clave-valor
user = {
    "username": "user123"
}



# ACCEDER A LOS VALORES
# volviendo al juego de los marcianitos, digamos que tenemos el siguiente ejemplo
alien_0 = {
    "color": "green",
    "points": 5
}

# acceder a sus datos con corchetes
print(alien_0["color"])         # green
print(alien_0["points"])        # 5
# print(alien_0["height"])      # KeyError: 'height' -> esa clave no existe

# acceder a sus datos con .get()
print(alien_0.get("color", "Key not found"))    # green
print(alien_0.get("height", "Key not found"))   # Key not found -> no da error



# AÑADIR PARES CLAVE-VALOR NUEVOS
"""
se pueden añadir pares clave-valor en cualquier momento a un diccionario, para
ello, basta con llamar al diccionario, utilizar los corchetes para definir la
nueva clave y asociarle un valor

dictionary["new_key"] = new_value
"""

print(alien_0)                  # {'color': 'green', 'points': 5}

# añadimos pares nuevos
alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)                  # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

""" 
sabiendo esto, se puede crear un diccionario vacío e ir introduciendo los datos
deseados a lo largo del programa

para definir un diccionario vacío, usar la siguiente sintaxis:

empty_dictionary = {}
"""



# MODIFICAR VALORES EN UN DICCIONARIO
"""
las modificaciones se realizan siguiendo el mismo procedimiento que para añádir
nuevos valores
"""

alien_0 = {"color": "green"}                # definición nueva del diccionario

alien_0["color"] = "yellow"                 # cambio de valor
print(f"The alien is {alien_0['color']}")   # The alien is yellow


# otro ejemplo -> vamos a mover el alien a la derecha
alien_0 = {
    "x_position": 0,
    "y_position": 25,
    "speed": "medium"
}

print(f"Original position: {alien_0['x_position']}")    # Original position: 0

# decidimos el incremento en base a la velocidad
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
elif alien_0["speed"] == "fast":
    x_increment = 3

# realizamos el cambio de valores
alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"New position: {alien_0['x_position']}")         # New position: 2

"""
únicamente modificando la velocidad del alien, se puede hacer que se comporte
de una forma u otra
"""



# ELIMINAR PARES CLAVE-VALOR
# OPCIÓN 1 -> del

"""
esta opción es totalmente válida, pero hay que tener en cuenta que se ha de
conocer perfectamente si el nombre de la clave existe o no en el diccionario,
en el caso de no existir esa clave y tratar de ejecutar 'del', se lanzaría un
error
"""

alien_0 = {
    "color": "green",
    "points": 5
}

print(alien_0)              # {'color': 'green', 'points': 5}

del alien_0["points"]
print(alien_0)              # {'color': 'green'}

# del alien_0["height"]     # KeyError: 'height' -> no existe esa clave


# OPCIÓN 2 -> .pop()
"""
esta opción nos permite gestionar de mejor manera la situación en el caso de que
no exista una clave que se ha intentado eliminar

.pop() recibe un primer argumento obligatorio donde se indica la clave del par
clave-valor que se quiere eliminar, y un segundo argumento opcional que indica
el mensaje a enviar si no existiera dicha clave

.pop() devolverá o el valor del par eliminado, o el mensaje en el caso de que
no existiera dicho par clave-valor
"""

alien_0 = {
    "color": "green",
    "points": 5
}

print(alien_0)              # {'color': 'green', 'points': 5}

removed_pair = alien_0.pop("points", "Pair not found")  # el mensaje que quieras
print(removed_pair)         # 5
print(alien_0)              # {'color': 'green'}

removed_pair = alien_0.pop("height", "Pair not found")
print(removed_pair)         # Pair not found -> no existe la clave 'height'
print(alien_0)              # {'color': 'green'} -> se queda como estaba

""" CUÁNDO USAR 'del' Y CUÁNDO USAR '.pop()'
ambas se pueden utilizar en cualquier momento, pero se debe tener en cuenta que
si se utiliza 'del', se debe tener un sistema de gestión de errores por si se
diera el caso de que la clave solicitada no existiera

mientras que con '.pop()' esto no sería necesario, aunque seguramente sí deba
realizarse alguna acción concreta si se recibe el mensaje de "no encontrado"
"""