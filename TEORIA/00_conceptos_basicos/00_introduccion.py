# ESTILO DE CÓDIGO

"""
no se van a seguir todas estas pautas a lo largo de estas explicaciones, sin embargo,
existen las PEP (Python Enchancement Proposal, o Propuestas de Mejora de Python) que
dictan ciertas recomendaciones a la hora de estructurar el código. He aquí las
recomendaciones más notorias:

- usar 4 espacios por nivel de sangrado -> mejora la legibilidad
- tamaño máximo de línea = 80 caracteres -> esto sirve para poder abrir varias ventanas
de una y leer el código completo de todas las ventanas
- usar líneas en blanco para agrupar partes del programa de forma visual

evidentemente, estas directrices no son obligatorias, aunque sí son muy recomendables
"""



# COMENTARIOS

"""
los comentarios son ignorados por el programa, son muy útiles para explicar el
código que se haya escrito

para escribir comentarios se usan las '#', lo que creará un comentario de una
única línea. Si queremos crear comentarios de varias líneas, crearemos un bloque
con tres guiones escribiendo entre dichos guiones toda la información -> """ """

por ejemplo:
"""

# esto es un comentario de una línea

"""
esto es un comentario
de más de una línea
"""



# VARIABLES

# sin variables
print("Hello World!")

# con variables
message = "Hello World!"
print(message)              # Hello World!

message = "Hello Python"    # cambio de valor
print(message)              # Hello Python


""" REGLAS PARA NOMBRAR UNA VARIABLE EN PYTHON
- los nombres de las variables sólo pueden contener letras, números y guiones bajos
- no se permiten espacios en los nombres de variables, pero se pueden usar guiones para separar palabras
- evita usar palabras clave y nombres de funciones como nombres de variables, esas palabras están reservadas
por Python para otros propósitos
- tenga cuidado al utilizar la "l" minúscula y la "O" mayúscula, pueden confundirse con "1" y "0".

usaremos variables en minúsculas usando el guión bajo para separar palabras -> my_variable, first_name, ...
"""

# ASIGNAR VARIOS VALORES A LA VEZ
name, username, age, height = "Nia", "nlarrea", 24, 1.63



# CONSTANTES

# constante = variable cuyo valor permanece invariable a lo largo de la vida de un programa
"""
Python no tiene tipos constantes incorporados. Usa nombres en mayúsculas para indicar que una variable debe
ser tratada como una constante y nunca ser cambiada
"""

PI = 3.14



# TIPOS DE DATOS

print(type(11))         # int
print(type(3.14))       # float
print(type("hello"))    # str
print(type(True))       # bool


# CAMBIO DE TIPO DE DATO

# python: type casting -> significa que se permite el cambio de tipo de dato

# NÚMEROS
print(float(2))     # 2.0   -> int a float
print(int(1.1))     # 1     -> float a int -> CUIDADO: haciendo esto se puede perder información!


# STRINGS = cadenas de texto
print(int("4"))         # 4     -> str a int
print(float("2.2"))     # 2.2   -> str a float
# print(int("a"))       # ValueError: invalid literal for int() with base 10: 'a'

print(str(34))          # 34    -> str a str
print(str(5.16))        # 5.16  -> float a str


# BOOLEANOS
print(bool(1))          # True  -> int a bool
print(bool(0))          # False -> int a bool

print(int(True))        # 1     -> bool a int
print(int(False))       # 0     -> bool a int