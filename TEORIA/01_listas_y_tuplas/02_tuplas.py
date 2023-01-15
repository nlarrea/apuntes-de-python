# TUPLAS

"""
las listas funcionan genial para almacenar datos de forma ordenada, sin embargo,
hay veces en las que no se quiere permitir modificar un elemento dentro de las
liastas. Para eso existen las tuplas
"""

# DEFINICIÓN
my_tuple = ()
my_other_tuple = tuple()

print(type(my_tuple))           # <class 'tupple'>
print(type(my_other_tuple))     # <class 'tupple'>



# ACCEDER A LOS VALORES
my_tuple = (200, 5.5, "nlarrea", True, ["JS", "HTML", "CSS"])
# no se está modificando el valor de la tupla, se está asignando otro valor a la variable
print(my_tuple)             # (200, 5.5, 'nlarrea', True, ['JS', 'HTML', 'CSS'])
print(my_tuple[0])          # 200
print(my_tuple[1])          # 5.5
print(my_tuple[2])          # nlarrea
print(my_tuple[3])          # True
print(my_tuple[4])          # ['JS', 'HTML', 'CSS']
print(my_tuple[4][2])       # CSS

# hemos dicho que no se pueden modificar los valores:
# my_tuple[0] = 100         # TypeError: 'tuple' object does not support item assignment

my_other_tuple = (2)
print(my_other_tuple)       # 2

print(my_tuple[-1])         # ['JS', 'HTML', 'CSS'] -> se pueden usar valores negativos

print(my_tuple[:])          # (200, 5.5, 'nlarrea', True, ['JS', 'HTML', 'CSS']) -> todos los elementos
print(my_tuple[1:3])        # (5.5, 'nlarrea')

print(my_tuple[::-1])       # (['JS', 'HTML', 'CSS'], True, 'nlarrea', 5.5, 200)



# JUNTAR TUPLAS
fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("tomato", "potato", "onion", "carrot")
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)        #('banana', 'orange', 'mango', 'lemon', 'tomato', 'potato', 'onion', 'carrot')



# LONGITUD DE UNA TUPLA
print(len(my_tuple))        # 5



# RECORRER TUPLAS COM BUC;ES
rugby_positions = (
    "loose-head prop", "hooker", "tight-head prop",
    "blind-side flanker", "second row", "second row",
    "open-side flanker", "number 8", "scrum-half",
    "fly-half", "left wing", "inside center",
    "outside center", "right wing", "full-back"
)

for player in rugby_positions:
    print(player)



# FUINCIONES PREDEFINIDAS
print(rugby_positions.count("hooker"))          # 1
print(rugby_positions.count("second row"))      # 2

print(rugby_positions.index("hooker"))          # 1
print(rugby_positions.index("second row"))      # 4 -> devuelve el index del primero



# "MODIFICAR" TUPLAS
"""
ya hemos dicho que las tuplas no se pueden modificar, sin embargo, puden ser
redefinidas. Vamos con un ejemplo:
"""

dimensions = (200, 50)              # tupla original -> no se pueden modificar valores
print("Dimensiones originales:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)             # redefinición de la variable -> nueva tupla, no reasignación
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)



# TRANSFORMAR TUPLAS EN LISTAS
fruits = ("banana", "lemon", "orange", "mango")
fruits = list(fruits)       # se convierte la tupla en lista

fruits[0] = "apple"         # se modifica el valor de la lista
print(fruits)               # ['apple', 'lemon', 'orange', 'mango']

fruits = tuple(fruits)      # se vuelve a convertir en tupla
print(fruits)               # ('apple', 'lemon', 'orange', 'mango')



# SABER SI UN ITEM ESTÁ EN LA TUPLA
fruits = ("banana", "lemon", "orange", "mango")
print("orange" in fruits)       # True
print("apple" in fruits)        # False



# ELIMINAR TUPLAS
del fruits