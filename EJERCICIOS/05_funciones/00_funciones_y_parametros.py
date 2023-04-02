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



print("\n\n06 - NOMBRES DE CIUDADES\n")
"""
Crea una función llamada 'city_country()' que toma el nombre de una ciudad y su
país. La función debe retornar un string como el siguiente:
    'Santiago, Chile'
Llama a la función 3 veces con diferentes valores e imprime el resultado.
"""

def city_country(city, country):
    return f"{city}, {country}"


print(city_country("Murcia", "Spain"))          # Murcia, Spain
print(city_country("London", "England"))        # London, England
print(city_country("Paris", "France"))          # Paris, France



print("\n\n07 - ÁLBUM\n")
"""
Crea una función llamada 'make_album()' que cree un diccionario describiendo un
álbum musical. La función debe recibir un artista y el título del álbum, y debe
retornar un diccionario que contenga esta información. Llama a la función tres
veces para crear tres álbumes diferentes.
Utiliza 'None' para añadir información adicional, como el número de canciones.
Si se añade dicho parámetro, debe añadirse al diccionario. Llama al menos una
vez a la función con este parámetro de más para mostrarlo.
"""

def make_album(artist, title, songs_number = None):
    new_album = {
        "artist": artist,
        "album title": title,
    }

    if songs_number:
        new_album["number of songs"] = songs_number

    return new_album


print(make_album("Asking Alexandria", "The Black"))
# {'artist': 'Asking Alexandria', 'album title': 'The Black'}
print(make_album("Alice Wonder", "Que Se Joda Todo Lo Demás", 8))
# {'artist': 'Alice Wonder', 'album title': 'Que Se Joda Todo Lo Demás', 'number of songs': 8}
print(make_album("Bring Me The Horizon", "That's The Spirit", 11))
# {'artist': 'Bring Me The Horizon', 'album title': "That's The Spirit", 'number of songs': 11}



print("\n\n08 - ÁLBUMES DEL USUARIO")
"""
Comienza desde el programa que has creado en el ejercicio anterior. Escribe un
bucle 'while' que permita al usuario introducir un artista y un título. Una vez
tengas la información, llama a la función make_album()
"""

while True:
    artist = input("\nEnter the artist (enter to exit): ")
    if not artist: break
    
    title = input("Enter the title of the album (enter to exit): ")
    if not title: break

    songs_number = input("Enter the number of songs (enter to quit, -1 to exit): ")
    if songs_number == -1: break

    print(songs_number)
    print(make_album(artist, title, songs_number))

    ans = input("Do you want to make more albums? (y/n): ")
    if ans.lower() == "n": break