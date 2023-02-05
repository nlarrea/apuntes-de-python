# USAR BUCLES EN UN DICCIONARIO
"""
los diccionarios pueden contener tantos pares clave-valor como sean necesarios,
por ello, una forma rápida y útil de acceder a todos los componentes es usar
bucles sobre el diccionario
"""

# RECORRER LAS CLAVES Y LOS VALORES -> .items()
user = {
    "username": "nlarrea",
    "fist_name": "Naia",
    "last_name": "Larrea"
}

for key, value in user.items():
    print(f"Key: {key}\t\tValue: {value}")
""" imprime lo siguiente:
Key: username           Value: nlarrea
Key: fist_name          Value: Naia
Key: last_name          Value: Larrea
"""


# otro ejemplo
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
""" imprime lo siguiente:
Jen's favorite language is Python
Sarah's favorite language is C
Edward's favorite language is Ruby
Phil's favorite language is Python
"""



# RECORRER LAS CLAVES -> .keys()
"""
la forma predeterminada si no se utiliza ninguna función que especifique lo
contrario en python es recorrer las claves en los bucles, por tanto se puede
utilizar esta sintaxis:

for key in dictionary.keys():
    some_code

o la siguiente sintaxis (más recomendada):

for key in dictionary:
    some_code
"""

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

friends = ["phil", "sarah"]

for name in favorite_languages:
    print(name.title())
    if name in friends:
        print(f"\t{name.title()}, I see you love {language.title()}!")
""" se imprime lo siguiente:
Jen
Sarah
    Sarah, I see you love Python!
Edward
Phil
    Phil, I see you love Python!
"""



# RECORRER LOS PARES EN ORDEN
"""
esto es útil si se quieren mostrar datos a los usuarios de tal forma que se
localicen de forma sencilla y rápida en la lista
"""

exam_results = {
    "jen": 6,
    "sarah": 9,
    "edward": 7,
    "phil": 4
}

for name, mark in sorted(exam_results.items()):
    print(f"{name.title()}, your score is an {mark}.")
"""
Edward, your score is an 7.
Jen, your score is an 6.
Phil, your score is an 4.
Sarah, your score is an 9.
"""



# RECORRER LOS VALORES -> .values()
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(f"\t- {language.title()}")
""" se imprime lo siguiente:
The following languages have been mentioned:
    - Python
    - C
    - Ruby
    - Python
"""

""" EVITAR MOSTRAR VALORES REPETIDOS
si se desea que no se muestren valores repetidos, se puede utilizar un set

un set es un conjunto de valores donde no se pueden almacenar dos datos iguales

para crear un set se pueden utilizar {} sin pares clave-valor (puesto que eso
sería un diccionario), o bien la función set()
"""

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(f"\t- {language.title()}")
""" se imprime lo siguiente:

The following languages have been mentioned:
    - Python
    - Ruby
    - C

ya no hay valores repetidos """