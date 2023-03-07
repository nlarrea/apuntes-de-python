print("01 - MENSAJES\n")
"""
Crea una función llamada 'display_message()' que imprima un mensaje contándole
a todo el mundo que estás aprendiendo a programar Python. Asegúrate de que el
mensaje se imprime correctamente.
"""

def display_message(msg):
    print(msg)


message = "Hello World! I am learning Python!"
display_message(message)
# prints: Hello World! I am learning Python!

display_message("Hi! I love Python")
# prints: Hi! I love Python



print("\n\n02 - LIBRO FAVORITO\n")
"""
Escribe una función llamada 'favorite_book()' que obtenga un parámetro 'title'.
La función debe imprimir un mensaje como 'One of my favorite books is Alice in
Wonderland'. Llama a la función para asegurarte de que el mensaje se imprime
correctamente.
"""

def favorite_book(title):
    print(f"One of my favorite books is {title}")


favorite_book("Python Crash Course")
# prints: One of my favorite books is Python Crash Course

favorite_book("Harry Potter and the Prisoner of Azkaban")
# prints: One of my favorite books is Harry Potter and the Prisoner of Azkaban



print("\n\n03 - CAMISETA\n")
"""
Crea una función llamada 'make_shirt()' que acepte la talla y el mensaje que
debe imprimirse en la camiseta. La función debe imprimir un mensaje que resuma
la talla y el mensaje de la camiseta.
- Llama a la función usando argumentos por posición.
- Llama a la función usando argumentos con nombre.
"""

def make_shirt(size, message):
    print(f"Size: {size}\nMessage: {message}\n")


# argumentos por posición
make_shirt("M", "I came, I saw & I forgot what I was doing")
""" prints:
Size: M
Message: I came, I saw & I forgot what I was doing
"""

# argumentos por nombre
make_shirt(message="I came, I saw & I forgot what I was doing", size="S")
""" prints:
Size: S
Message: I came, I saw & I forgot what I was doing
"""



print("\n\n04 - CAMISETAS GRANDES")
"""
Modifica la función 'make_shirt()' para que las camisetas sean grandes por
defecto con un mensaje que diga 'I love Python'. Haz una camiseta grande y una
mediana con el mensaje predeterminado, y una de cualquier talla con un mensaje
diferente.
"""

def make_shirt2(size="L", message="I love Python"):
    print(f"Size: {size}\nMessage: {message}\n")


# camiseta grande con mensaje por defecto
make_shirt2()
""" prints:
Size: L
Message: I love Python
"""

# camiseta mediana con mensaje predeterminado
make_shirt2("M")
""" prints:
Size: M
Message: I love Python
"""

# camiseta de cualquier talla con mensaje diferente
make_shirt2(message="Hello World!")
""" prints:
Size: L
Message: Hello World!
"""



print("\n\n05 - CIUDADES\n")
"""
Crea una función llamada 'describe_city()' que reciba el nombre de una ciudad y
el país al que pertenece. La función debe mostrar un mensaje como 'Reykjavik is
in Iceland'. Dale al parámetro del país un nombre por defecto. Llama a la
función 3 veces, al menos en una de ellas no debe usar el nombre del país por
defecto.
"""

def describe_city(city, country="spain"):
    print(f"{city.title()} is in {country.title()}")


describe_city("murcia")                 # Murcia is in Spain
describe_city("bilbao")                 # Bilbao is in Spain
describe_city("paris", "france")        # Paris is in France