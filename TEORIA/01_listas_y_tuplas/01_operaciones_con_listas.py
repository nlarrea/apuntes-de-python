# OPERACIONES CON LISTAS

# DESESTRUCTURAR LISTAS -> guardar sus elementos en variables

my_list = ["Naia", "nlarrea", 24, 1.63]

# forma rápida y útil de guardar los datos de una lista en variables
name, username, age, height = my_list

print(name)         # Naia
print(username)     # nlarrea
print(age)          # 24
print(height)       # 1.63



# RECORRER LISTAS -> bucle "for"

""" INTRODUCCIÓN A BUCLES FOR
se pueden recorrer las listas pasando por todos los elementos usando bucles "for"

esto es algo muy útil cuando se necesita realizar una acción o comprobación en todos
los elementos de una lista

una buena práctica para estos bucles es crearlos de la siguiente manera:
    for item in list_of_items:
    for dog in dogs:
es decir, una especie de "for sigular in plural:"
"""

for item in my_list:
    print(item)
    """ se imprime lo siguiente:
    Naia
    nlarrea
    24
    1.63

    ese bloque se ejecuta tantas veces como elementos tenga la lista, e imprime un
    elemento de la lista
    """

# otro ejemplo
names = ["naia", "cristina", "june", "clara"]       # nombres en minúscula

for name in names:
    print(f"'{name.title()}' está escrito con la primera letra en mayúscula.")
    """ se imprime lo siguiente:
    'Naia' está escrito con la primera letra en mayúscula.
    'Cristina' está escrito con la primera letra en mayúscula.
    'June' está escrito con la primera letra en mayúscula.
    'Clara' está escrito con la primera letra en mayúscula.
    """



# USAR RANGOS -> range()

for value in range(1, 5):
    print(value)
    """ se imprime lo siguiente:
    1
    2
    3
    4
    """
    # range(inicio, final, paso) -> el inicio está incluido pero el valor final no

# se puede usar range() para crear listas
numbers = list(range(1,6))
print(numbers)          # [1, 2, 3, 4, 5]

even_numbers = list(range(2, 11, 2))
print(even_numbers)     # [2, 4, 6, 8, 10]

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)          # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



# ESTADÍSTICA BÁSICA CON LISTAS NUMÉRICAS

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits))      # 0
print(max(digits))      # 9
print(sum(digits))      # 45



# LIST COMPREHENSION

# este método es posible para crear cualquier lista a partir de un bucle for
squares = [value**2 for value in range(1, 11)]
print(squares)          # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# otra forma de crear listas rápidas (con el mismo tipo de elemento)
new_list = [5] * 4
print(new_list)         # [5, 5, 5, 5]

new_list = [None] * 3
print(new_list)         # [None, None, None]
# este método es útil cuando queremos crear la estructura de la lista sin dar valores



# BUCLES A TRAVÉS DE SECCIONES DE LISTAS

video_games = ["Gears of War", "Halo", "Skyrim", "Bioshock", "Dragon Quest"]

for game in video_games[:3]:
    print(game)
    """ se imprime lo siguiente:
    Gears of War
    Halo
    Skyrim
    """