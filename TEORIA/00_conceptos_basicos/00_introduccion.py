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



# COMENTARIOS

# esto es un comentario de una línea

"""
esto es un comentario
de más de una línea
"""