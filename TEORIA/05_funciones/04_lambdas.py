# LAMBDAS

"""
Las lambdas son funciones anónimas en una única línea. Son muy breves y simples
pero muy útiles cuando se pretenden realizar acciones muy concretas.

Pueden ejecutarse dentro de los parámetros de otras funciones y/o guardar la
función entera dentro de una variable.

SINTAXIS

lambda <argumentos>: lo_que_es_devuelto
"""

# guardamos la función en una variable
sum_two = lambda number_one, number_two: print(number_one + number_two)

# llamamos a la función
sum_two(4, 3)       # 7
sum_two(11, 23)     # 34


# también pueden retornar el valor
full_name = lambda first, last: f"{first} {last}"

print(f"Hi {full_name('Naia', 'Larrea')}")      # Hi Naia Larrea



# llamar una lambda desde una función

"""
'reduce' recibe dos parámetros:
    1. una función
    2. un iterable
e itera por todos los componentes devolviendo lo que le indique la función, y
solo devuelve un único valor, de ahí que se llame 'reduce'

Es un ejemplo perfecto para utilizar lambdas! Vamos a realizar la suma de todos
los elementos dentro de una lista utilizando una función lambda que recoja dos
números y los sume
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7]

sum_of_numbers = reduce((lambda total, current: total + current), numbers)
print(sum_of_numbers)           # 28