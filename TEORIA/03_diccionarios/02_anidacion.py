# LISTA DE DICCIONARIOS
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
""" se imprime lo siguiente:
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
"""


# crear 30 aliens verdes
aliens = []

for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# mostrar los 5 primeros
for alien in aliens[:5]:
    print(alien)
print("...")

# mostrar la cantidad de aliens creada
print(f"\nTotal number of aliens: {len(aliens)}")

""" con este código se imprime lo siguiente:
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...

Total number of aliens: 30
"""

# si se quisiera modificar el valor de los 3 primeros, se podría hacer lo siguiente
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"

# mostrar los 5 primeros
for alien in aliens[:5]:
    print(alien)
print("...")

# mostrar la cantidad de aliens creada
print(f"\nTotal number of aliens: {len(aliens)}")

""" con este código se imprime lo siguiente:
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...

Total number of aliens: 30
"""



# DICCIONARIO CON LISTA
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"]
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")

    for language in languages:
        print(f"\t- {language.title()}")

""" este código imprime lo siguiente:
Jen's favorite languages are:
        - Python
        - Ruby

Sarah's favorite language is:
        - C

Edward's favorite languages are:
        - Ruby
        - Go

Phil's favorite languages are:
        - Python
        - Haskell
"""



# DICCIONARIO DENTRO DE DICCIONARIO
users = {
    "aeinstein": {
        "first_name": "albert",
        "last_name": "einstein",
        "location": "princeton"
    },
    "mcurie": {
        "first_name": "marie",
        "last_name": "curie",
        "location": "paris"
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info["location"]

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

""" se imprime lo siguiente:

Username: aeinstein
        Full name: Albert Einstein
        Location: Princeton

Username: mcurie
        Full name: Marie Curie
        Location: Paris
"""



# ACCEDER A LOS VALORES SIN USAR BUCLES
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"]
}

list_of_fav_languages = list(favorite_languages.items())
print(list_of_fav_languages)
""" se imprime lo siguiente:
[
    ('jen', ['python', 'ruby']),
    ('sarah', ['c']),
    ('edward', ['ruby', 'go']),
    ('phil', ['python', 'haskell'])
]
"""

# vemos que es una lista de tuplas -> podemos acceder a los datos de esta forma
print(list_of_fav_languages[0])         # ('jen', ['python', 'ruby']) -> tupla entera
print(list_of_fav_languages[0][0])      # jen -> nombre de la persona
print(list_of_fav_languages[0][1])      # ['python', 'ruby'] -> lenguajes favoritos
print(list_of_fav_languages[0][1][0])   # python -> uno de los lenguajes favoritos