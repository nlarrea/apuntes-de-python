print("01 - CIUDAD, PAÍS\n")
"""
Escribe una función que acepte 2 parámetros: una ciudad y el nombre del país.
La función debe devolver un string con el formato 'Ciudad, País'. Crea un
archivo llamado 'test_cities.py', importa la librería 'unittest' y crea un
método llamado 'test_city_country()' para comprobar que la función devuelve los
datos deseados.
"""

# comentado para que no haya conflicto con el siguiente ejercicio
#
# def get_formated_str(city, country):
#     city_country = f"{city}, {country}"
#     return city_country.title()

# test result:
#
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK



print("\n\n02 - POPULATION\n")
"""
Modifica la función, de tal forma que la función requiera un tercer parámetro,
'population'. La función debe retornar un string con el formato siguiente:
    'City, Country - population XXXX'
Vuelve a arrancar el test para comprobar que da error. Modifica la función de
nuevo para asegurarte de que el parámetro 'population' es optativo. Crea un
test llamado 'test_city_country_population()' que verifique que puedes llamar a
la función con los 2 y/o 3 parámetros.
"""

# 'rompemos' la función para que no funcione:

# comentado para que no haya conflicto con el siguiente paso del ejercico
#
# def get_formated_str(city, country, population):
#     city_country = f"{city}, {country} - population {population}"
#     return city_country.title()

# test result:
#
# E
# ======================================================================
# ERROR: test_city_country (__main__.CitiesTestCase)
# Do entries like 'Santiago, Chile' work?
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\larre\Documents\NAIA\OpenBootcamp\4-Python\open-python\EJERCICIOS\11_testing\test_cities.py", line 10, in test_city_country
#     formatted_str = get_formated_str("santiago", "chile")
# TypeError: get_formated_str() missing 1 required positional argument: 'population'
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
#
# FAILED (errors=1)


# ahora arreglamos la función para que funcione con 2 y 3 parámetros:

def get_formated_str(city, country, population=None):
    if population:
        city_country = f"{city.title()}, {country.title()} - population {population}"
    else:
        city_country = f"{city}, {country}".title()
    return city_country

# test result:
#
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK