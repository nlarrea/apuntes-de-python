# STRINGS

# strings = series de caracteres -> cualquier cosa entre comillas es considerada un string para Python

"Esto es un string"
'Esto también es un string'

"Puedes 'entrecomillar' algo escribiendo el otro tipo de comilla"



# LONGITUD DE UN STRING -> len()

print(len("Esto es un string"))     # 17 -> los espacios en blanco también se cuentan
print(len("Hello World!"))          # 12



# CAMBIAR MINÚSCULAS Y MAYÚSCULAS EN UN STRING CON MÉTODOS

name = "naia larrea"
print(name.title())     # Naia Larrea

name = "Naia Larrea"
print(name.upper())     # NAIA LARREA
print(name.lower())     # naia larrea
print(name)             # Naia Larrea -> el original no cambia



# USANDO VARIABLES EN LOS STRINGS (FORMATEO DE STRINGS) -> 3 formas de hacerlo

name, surname, age = "Naia", "Larrea", 24

# PRIMERA FORMA: .format()

print("My name is {} {} and I'm {} years old".format(name, surname, age))
# imprime: My name is Naia Larrea and I'm 24 years old

# muestra los valores según el orden dentro de .format() -> cuidado con los posibles errores
print("My name is {} {} and I'm {} years old".format(name, age, surname))
# imprime: My name is Naia 24 and I'm Larrea years old

# posible solución: indicar la posición dentro del .format() entre las llaves
print("My name is {0} {2} and I'm {1} years old".format(name, age, surname))
# imprime: My name is Naia Larrea and I'm 24 years old


# SEGUNDA FORMA: %d, %s, ...

print("My name is %s %s and I'm %d years old" %(name, surname, age))
# imprime: My name is Naia Larrea and I'm 24 years old


# TERCERA FORMA: f"" -> permite dar formato a los strings

full_name = f"{name} {surname}"     # podemos guardar un string formateado en una variable

print(full_name.title())            # Naia Larrea



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