print("01 - PERSONAS\n")
"""
Comienza con el diccionario creado en el primer ejercicio del apartado anterior.
Crea dos personas nuevas y guarda los 3 diccionarios en una lista llamada
'people'. Recorre toda la lista imprimiendo todo lo que sepas acerca de las
personas de la lista.
"""

person_0 = {
    "name": "haizea",
    "surname": "albarracín",
    "age": 5,
    "city": "murcia"
}

person_1 = {
    "name": "clara",
    "surname": "garcía",
    "age": 21,
    "city": "madrid"
}

person_2 = {
    "name": "cristina",
    "surname": "larrea",
    "age": 28,
    "city": "bilbao"
}

people = [person_0, person_1, person_2]

for person in people:
    full_name = f"{person['name'].title()} {person['surname'].title()}"
    print(f"{full_name} is {person['age']} years old and lives in {person['city'].title()}")



print("\n\n02 - MASCOTAS\n")
"""
Crea unos diccionarios que representen a una mascota. En cada diccionario debes
incluir el tipo de mascota que es y el nombre del dueño. Guarda los diccionarios
en una lista llamada 'pets' y recorre la lista para imprimir todo lo que sepas
de cada una de las mascotas.
"""

pet_0 = {
    "name": "buckbeak",
    "type": "hippogriff",
    "owner": "rubeus hagrid"
}

pet_1 = {
    "name": "fawkes",
    "type": "phoenix",
    "owner": "albus dumbledore"
}

pet_2 = {
    "name": "norris",
    "type": "cat",
    "owner": "argus filch"
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"The pet name is {pet['name'].title()}, it is a/an {pet['type']} and its owner is {pet['owner'].title()}")



print("\n\n03 - LUGARES FAVORITOS\n")
"""
Crea un diccionario llamado 'favorite_places'. Piensa en tres nombres para usar
como claves y guarda de uno a tres lugares favoritos para cada persona.
Recorre el diccionario e imprime el nombre de cada persona y su lugar favorito.
"""

favorite_places = {
    "naia": ["murcia", "bilbao", "madrid"],
    "cris": ["murcia", "segovia"],
    "june": ["galdakao", "noja"]
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f"\t- {place.title()}")



print("\n\n04 - NÚMEROS FAVORITOS\n")
"""
Usa un diccionario para almacenar los números favoritos de las personas. Usa 5
nombres y utilízalos como claves del diccionario. Piensa cuáles son todos los
números favoritos de cada una de esas personas, puede ser solo un número o más.
Imprime cada nombre y sus números favoritos.
"""

favorite_numbers = {
    "naia": [11, 5, 7],
    "cristina": [5, 9],
    "irene": [10, 15],
    "javi": [23]
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorites numbers are:")
    for number in numbers:
        print(f"\t- {number}")



print("\n\n06 - CIUDADES\n")
"""
Crea un diccionario llamado 'cities'. Usa el nombre de 3 ciodades como clave.
Crea un diccionario con información sobre cada una de las ciudades, añadiendo
el país en el que se encuentran, la población aproximada, y algún dato acerca
de la misma.
Imprime el nombre de la ciudad y toda la información sobre ella.
"""

cities = {
    "murcia": {
        "country": "spain",
        "population": 447182,
        "fact": "You can go into a bar and eat a 'bicycle', which is the name of a typical local snak"
    },
    "bilbao": {
        "country": "spain",
        "population": 345821,
        "fact": """The most famous museum in Bilbao is the Guggenheim Museum, which has a giant dog
        made of flowers in front and a giant iron spider in the back area."""
    },
    "matamata": {
        "country": "new zealand",
        "population": 31800,
        "fact": "The Hobbiton film set is located in this place, which you can visit!"
    }
}

for city, city_info in cities.items():
    print(f"\n{city.title()}:")
    for info_title, info_value in city_info.items():
        if info_title == "country":
            info_value = info_value.title()
        print(f"- {info_title.capitalize()} -> {info_value}")