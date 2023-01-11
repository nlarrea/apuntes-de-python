# LISTAS

""" CONCEPTOS BÁSICOS DE LAS LISTAS
lista = colección de elementos en un orden particular

podemos poner todo lo que queramos en una lista, sin que sus elementos tengan
la necesitad de estar relacionados entre sí

si imprimimos una lista, se muestra la representación de la lista, incluyendo
los corchetes que la forman
"""

# 2 formas de declarar una lista:
my_list = list()
my_other_list = []

print(type(my_list))            # <class 'list'>
print(type(my_other_list))      # <class 'list'>



# LONGITUD DE UNA LISTA

my_list = ["Naia", "nlarrea", 24, 1.63]

print(my_list)          # ['Naia', 'nlarrea', 24, 1.63]
print(len(my_list))     # 4



# ACCEDER A LOS VALORES

"""
los valores son accesibles usando el index (posición) del elemento

se debe tener en cuenta que, como en la mayoría de lenguajes de programación,
el índice comienza por 0, no 1
"""

print(my_list[0])       # Naia
print(my_list[2])       # 24
print(my_list[-1])      # 1.63 -> el índice puede ser negativo

# LISTAS CON LISTAS U OTROS ELEMENTOS ITERABLES

my_nested_list = ["Naia", "nlarrea", 24, 1.63, ["Python", "JavaScript", "HTML", "CSS"]]

print(my_nested_list)           # ['Naia', 'nlarrea', 24, 1.63, ['Python', 'JavaScript', 'HTML', 'CSS']]
print(my_nested_list[4])        # ['Python', 'JavaScript', 'HTML', 'CSS']
print(my_nested_list[4][1])     # JavaScript



# CONVERTIR UN STRING EN LISTA

my_str = "Hola Mundo!"

# FORMA 1: constructor de lista -> list()
my_str_list = list(my_str)

print(my_str)                   # Hola Mundo!
print(type(my_str))             # <class 'str'>
print(my_str_list)              # ['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o', '!']
print(type(my_str_list))        # <class 'list'>

# FORMA 2: .split() -> especificar entre parénteris si queremos separarlo de alguna forma concreta
my_str_list = my_str.split()

print(my_str)                   # Hola Mundo!
print(type(my_str))             # <class 'str'>
print(my_str_list)              # ['Hola', 'Mundo!'] -> separa por los espacios por defecto
print(type(my_str_list))        # <class 'list'>



# CONCATENAR O SUMAR LISTAS

# operador de suma (+)

my_first_list = [2, 4, 6]
my_second_list = [1, 3, 5]

print(my_first_list + my_second_list)       # [2, 4, 6, 1, 3, 5]

"""
estas darían error
    print(my_first_list - my_second_list)
    print(my_first_list * my_second_list)

pero se puede hacer esto (repetir una lista n veces)
"""
print(my_first_list * 4)                    # [2, 4, 6, 2, 4, 6, 2, 4, 6, 2, 4, 6]

# método -> .extend()

my_first_list = [2, 4, 6]
my_second_list = [1, 3, 5]

my_first_list.extend(my_second_list)        # hace lo mismo que con el operador '+'
print(my_first_list)                        # [2, 4, 6, 1, 3, 5]



# CREAR LISTAS A PARTIR DE LISTAS

is_developer = True     # las listas pueden contener variables
my_other_list = ["Naia", "nlarrea", 24, 1.63, ["Python", "JavaScript", "HTML", "CSS"], is_developer]

print(my_other_list[-1])      # True -> valor de 'is_developer'
print(my_other_list[:3])      # ['Naia', 'nlarrea', 24]
print(my_other_list[1:-1])    # ['nlarrea', 24, 1.63, ['Python', 'JavaScript', 'HTML', 'CSS']]
print(my_other_list[::2])     # ['Naia', 24, ['Python', 'JavaScript', 'HTML', 'CSS']]
# la lista original no modifica, pero podemos guardar el resultado en una variable nueva o la misma

# ALIASING

a = ["pop", 10, 1.2]
b = a

b[0] = "rock"
print(a)    # ['rock', 10, 1.2]
print(b)    # ['rock', 10, 1.2]
"""
aunque modifique una de las dos (a ó b), realmente se modifican las dos listas

esto ocurre porque las dos variables están referenciadas a la misma lista, y
por tanto, al modificar CUALQUIERA de las dos, la otra se verá afectada también
"""

# SOLUCIÓN 1 -> .copy()

a = ["pop", 10, 1.2]
b = a.copy()

b[0] = "rock"
print(a)    # ['pop', 10, 1.2]
print(b)    # ['rock', 10, 1.2]
# solo se ha modificado la lista b

# SOLUCIÓN 2 -> b = a[:]

"""
esa línea de código permite copiar de forma independiente una lista en otra variable,
debido a que se le está indicando que cree una sublista desde el inicio hasta el final
de la lista a
"""



# AÑADIR ELEMENTOS A UNA LISTA (se modifica la lista original)

# insertar valor al final -> .append()
my_list = ["Naia", 24]

my_list.append(1.63)        # se debe realizar fuera del print
print(my_list)              # ['Naia', 24, 1.63]


# insertar valor en posición concreta -> .insert(pos, element)
# my_list = ['Naia', 24, 1.63] -> recordatorio

my_list.insert(1, "nlarrea")
print(my_list)              # ['Naia', 'nlarrea', 24, 1.63]



# ELIMINAR ELEMENTOS DE UNA LISTA (se modifica la lista original)

# indicar cuál es el elemento a elimminar
my_list.remove("Naia")
print(my_list)              # ['nlarrea', 24, 1.63]
"""
si hay elementos duplicados en una lista, elimina el primero que encuentre con
el valor que se le ha indicado
"""


# eliminar el último elemento -> .pop() -> devuelve el valor que elimina
my_list.pop()
print(my_list)              # ['nlarrea', 24]
print(my_list.pop())        # 24
print(my_list)              # ['nlarrea']

# eliminar elemento teniendo en cuenta su posición -> .pop(pos) -> devuelve el dato eliminado
my_list = [32, 24, 62, 52, 30, 30, 17]

my_list.pop(2)
print(my_list)              # [32, 24, 52, 30, 30, 17]

my_list = [32, 24, 62, 52, 30, 30, 17]
print(my_list.pop(2))       # 62


# eliminar todos los valores -> .clear()
my_list.clear()
print(my_list)              # []


# eliminar algunos valores o la variable entera -> del()
my_list = [32, 24, 62, 52, 30, 30, 17]

del(my_list[0])             # elimina el elemento en la posición 0
print(my_list)              # [24, 62, 52, 30, 30, 17]

del(my_list)                # elimina la variable entera
# print(my_list)            # NameError: name 'my_list' is not defined



# ORDENAR LISTAS

# ordenar permanentemente -> .sort() -> modifica la lista original

my_number_list = [1, 7, 3, 4, 0.3, 5.5]
my_str_list = ["a", "b", "h", "d", "E", "c"]

my_number_list.sort()           # números -> ordena de menor a mayor
print(my_number_list)           # [0.3, 1, 3, 4, 5.5, 7]

my_str_list.sort()              # str -> lo ordena alfabéticamente según ASCII
print(my_str_list)              # ['E', 'a', 'b', 'c', 'd', 'h']

# también se pueden ordenar de forma inversa -> parámetro: reverse = True
my_number_list.sort(reverse = True)
print(my_number_list)           # [7, 5.5, 4, 3, 1, 0.3]

my_str_list.sort(reverse = True)
print(my_str_list)              # ['h', 'd', 'c', 'b', 'a', 'E']


# ordenar de forma temporal -> sorted()

my_number_list = [1, 7, 3, 4, 0.3, 5.5]

print(my_number_list)           # [1, 7, 3, 4, 0.3, 5.5]
print(sorted(my_number_list))   # [0.3, 1, 3, 4, 5.5, 7] -> lista ordenada
print(my_number_list)           # [1, 7, 3, 4, 0.3, 5.5] -> no se ha modificado