# vamos a usar bucles directamente durante estos ejercicios

print("01 - PERSONA\n")
"""
Crea un diccionario para almacenar información sobre una persona que conozcas.
Guarda:
    - Su nombre.
    - Su apellido.
    - Su edad.
    - Su ciudad.
Imprime cada dato.
"""

person = {
    "name": "Haizea",
    "surname": "Albarracín",
    "age": 5,
    "city": "Murcia"
}

for person_info in person.values():
    print(person_info)



print("\n\n02 - NÚMEROS FAVORITOS")
"""
Usa un diccionario para almacenar los números favoritos de las personas. Usa 5
nombres y utilízalos como claves del diccionario. Piensa el número favorito de
cada una de esas personas.
Imprime cada nombre y número favorito.
"""

favorite_numbers = {
    "naia": 11,
    "cristina": 5,
    "irene": 10,
    "javi": 23
}

for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}")



print("\n\n03 - GLOSARIO")
"""
- Piensa en 5 palabras de código que hayas aprendido hasta ahora. Úsalas como
claves del diccionario y guarda su significado como valor.
- Imprime cada par clave-valor dejando una línea en blanco entre pares y da el
formato que desees de tal forma que quede perfectamente legible.
"""

strings_glossary = {
    "capitalize()": "Return a copy of the string with its first character capitalized and the rest lowercased.",
    "lower()": "Return a copy of the string with all the cased characters 4 converted to lowercase.",
    "isupper()": "Return True if all cased characters in the string are uppercase.",
    "find()": "Return the lowest index in the string where substring sub is found.",
    "strip()": "Return a copy of the string with the leading and trailing characters removed."
}

for code_word, meaning in sorted(strings_glossary.items()):
    print(f"\n{code_word}:")
    print(f"\t{meaning}")



print("\n\n04 - RÍOS")
"""
Crea un diccionario que contenga tres ríos importantes y el país que recorren.

- Usa un bucle para imprimir una frase mostrando los valores y claves.
- Usa un bucle para imprimir el nombre de cada río.
- Usa un bucle para imprimir el nombre de cada país.
"""

rivers = {
    "nile": "egypt",
    "amazon": "peru",
    "mississippi": "montana",
    "chang jiang": "china",
    "ob": "rusia"
}

for name, location in rivers.items():
    print(f"The {name.title()} River runs through {location.title()}.")

print("These are the names of the rivers:")
for river in rivers:
    print(f"\t- {river.title()}")

print("These are the locations:")
for location in rivers.values():
    print(f"\t- {location.title()}")



print("\n\n05 - SONDEOS\n")
"""
Partiendo del siguiente código:

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

- Crea una lista con las personas que aún no han hecho la encuesta de cuál es
su lenguaje favorito. Incluye nombres que ya estén en el diccionario y otros
que no estén aún.
- Crea un bucle para recorrer la lista de personas que debería hacer la encuesta
e imprime un mensaje de agradecimiento si ya la habían realizado. Si aún no la
han respondido, imprime un mensaje invitando a que lo hagan.
"""

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

names = ["cristina", "sarah", "naia", "jen"]

for name in names:
    if name in favorite_languages.keys():
        print(f"Hi {name.title()}, thank you for taking the poll!")
    else:
        print(f"{name.title()}, please take our poll!")