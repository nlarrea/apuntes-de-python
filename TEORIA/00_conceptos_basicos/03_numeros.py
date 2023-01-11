# NÚMEROS

"""
los tados de tipo numérico en Python son:

- int (integer)         = números enteros
- float (decimales)     = números con coma flotante
"""

# en el apartado de operadores ya se ha visto cómo trabajar con ellos, pero vamos a profuncizar más



# INTEGERS

# los integers pueden ser sumados, restados, multiplicados y divididos
print(3 + 2)        # 5
print(2 - 3)        # -1 -> números negativos
print(20 * 10)      # 200

print(16 / 8)       # 2.0 -> el resultado de una división nomral siempre será de tipo float
print(3 // 2)       # 1 -> si no queremos decimales, usar la división entera

print(10 % 3)       # 1 -> módulo = el resto de la división
print(10 ** 6)      # 1000000 -> exponente



# FLOATS

"""
se pueden hacer las mismas operaciones que las vistas con los datos de tipo int, sin embargo,
en ocasiones se reciben datos arbitrarios. Por ejemplo:
"""

print(0.2 + 0.1)    # 0.30000000000000004

"""
esto es un error que cometen todos los lenguajes de programación. Ocurre debido a cómo los ordenadores
representan los números de forma interna. Más adelante se verá cómo trabajar con ello o 'arreglarlo'
"""

print(3.1 + 2.1)        # 5.2
print(2.6 - 3.3)        # -0.6999999999999997
print(20.5 * 10.7)      # 219.35

print(16.2 / 8.2)       # 1.975609756097561
print(3.0 // 2.0)       # 1.0 -> si se usan floats, devuelve el decimal

print(10.7 % 3.7)       # 3.299999999999999
print(10.4 ** 6.4)      # 3228593.525492568



# OPERACIONES CON INTEGERS Y FLOATS

# siempre que se mezclen ints y floats en una operación, el resultado será de tipo float

print(1 + 2.0)      # 3.0
print(2 * 3.0)      # 6.0
print(3.0 ** 2)     # 9.0



# GUIONES EN NÚMEROS

"""
esta es una herramienta muy útil cuando queremos trabajar con números grandes (con muchos dígitos), y
es que Python permite agrupar los números utilizando guiones bajos para hacer que sean mucho más legibles

al imprimir un número definido con guiones, Python solo imprime los dígitos

se ignoran los guiones, aunque no se usen para agrupar números de 3 en 3, o siguiendo cualquier patrón, es
decir, que para Python 1000, 10_00 y 1_000 son el mismo número
"""

universe_age = 14_000_000_000       # es mucho más fácil de leer que 14000000000



# NÚMEROS COMPLEJOS -> j

print(3 + 1j)       # (3+1j)