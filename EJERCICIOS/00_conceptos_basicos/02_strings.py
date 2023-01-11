# 01 - MENSAJE PERSONAL
"""
Usa una variable para representar el nombre de una persona e imprime un mensaje a esa persona.
Tu mensaje debe verse así:

“Hello Eric, would you like tolearn some Python today?”
"""

name = "Eric"

print(f"Hello {name}, would you like to learn some Python today?")



# 02 - NAME CASES
"""
Usa una variable para representar el nombre de una persona, y después, imprime ese nombre en
minúscula, mayúscula y mayúsculas de título.
"""

name = "naia"

print(name.upper())     # NAIA
print(name.lower())     # naia
print(name.title())     # Naia



# 03 - CITA FAMOSA
"""
Encuentra una cita de una persona famosa que admires. Imprime la cita y el nombre del autor.
Tu salida debe verse así, incluyendo las comillas:

Albert Einstein once said, “A person who never made a mistake never tried anything new.”
"""

# forma 1
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

# forma 2
print("Albert Einstein once said, \"A person who never made a mistake never tried anything new.\"")



# 04 - CITA FAMOSA 2
"""
Repite el ejercicio 05, pero esta vez, representa el nombre del personaje famoso en una variable
llamada famous_person. Después, crea tu mensaje guardándolo en una nueva variable llamada mensaje.
Imprime tu mensaje.
"""

famous_person = "Albert Einstein"
message = f"{famous_person} once said, \"A person who never made a mistake never tried anything new.\""

print(message)



# 05 - QUITANDO ESPACIOS
"""
Usa una variable para representar el nombre de una persona e incluya algunos caracteres
de espacio en blanco al principio y al final del nombre.
Asegúrate de utilizar cada combinación de caracteres, "\t" y "\n", al menos una vez.

Imprima el nombre una vez, de modo que se muestren los espacios en blanco alrededor del
nombre. A continuación, imprima el nombre utilizando cada de las tres funciones de
stripping: .lstrip(), .rstrip(), y .strip().
"""

name = "\tNaia\nLarrea    "

print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())