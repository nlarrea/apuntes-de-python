# STRINGS

# strings = series de caracteres -> cualquier cosa entre comillas es considerada un string para Python

"Esto es un string"
'Esto también es un string'

"Puedes 'entrecomillar' algo escribiendo el otro tipo de comilla"



# CAMBIAR MINÚSCULAS Y MAYÚSCULAS EN UN STRING CON MÉTODOS
name = "naia larrea"
print(name.title())     # Naia Larrea

name = "Naia Larrea"
print(name.upper())     # NAIA LARREA
print(name.lower())     # naia larrea
print(name)             # Naia Larrea -> el original no cambia



# USANDO VARIABLES EN LOS STRINGS & FORMATEO DE STRINGS
# f"" -> permite dar formato a los strings

first_name = "naia"
last_name = "larrea"
full_name = f"{first_name} {last_name}"

print(full_name.title())        # Naia Larrea



# AÑADIR ESPACIOS EN BLANCO A UN STRING -> TABULACIONES Y SALTOS DE LNEA
# tabulación    -> \t
print("Hello\tWorld!")      # Hello    World!

# nueva línea   -> \n
print("Hello\nWorld!")
# imprime:
"""
Hello
World!
"""

print("Students:\n\tJohn\n\tAnne\n\tJames")
# imprime:
"""
Students:
    John
    Anne
    James
"""



# ELIMINANDO ESPACIOS EN BLANCO
# .rstrip()     -> elimina los espacios en blanco situados a la derecha del string
# .lstrip()     -> elimina los espacios en blanco situados a la izquierda del string
# .strip()      -> elimina los espacios en blanco situados a ambos lados del string
# no modifican el string original -> ejemplos con .rstrip()

language = "python  "
print(language.rstrip())    # "python"      -> sin espacios en blanco
print(language)             # "python  "    -> con espacios en blanco

language = language.rstrip()
print(language)             # "python"      -> sin espacios en blanco



# DESEMPAQUETADO DE CARACTERES
a, b, c, d, e, f = "Python"

print(a)    # P
print(b)    # y
print(c)    # t
print(d)    # h
print(e)    # o
print(f)    # n

# si hay menos variables que longitud de string, da error



# DIVISIÓN
language = "Python"
language_slice = language[1:3]
print(language_slice) # yt

language_slice = language[1:]
print(language_slice) # ython

language_slice = language[:4]
print(language_slice) # Pyth

language_slice = language[-2]
print(language_slice) # o

language_slice = language[0:6:2]
print(language_slice) # Pto
# crea una especie de rango del 0 al 6 y dando saltos de 2 en 2

# reverse
language_slice = language[::-1]
print(language_slice) # nohtyP



# FUNCIONES DEL SISTEMA
language = "hello"

print(language.capitalize())        # Hello
print(language.upper())             # HELLO
print(language.count("l"))          # 2
print(language.isnumeric())         # False
print("1".isnumeric())              # True
print(language.lower())             # hello
print(language.upper().isupper())   # True
print(language.lower().isupper())   # False
print(language.startswith("He"))    # False
print(language.startswith("he"))    # True
print("he" == "He") # False -> no es lo mismo