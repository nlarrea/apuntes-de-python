print("01 - RESTAURANTE\n")
"""
Crea una clase llamada 'Restaurant'. El método __init__() debe recibir 2 atri-
butos: 'restaurant_name' y 'cuisine_type'. Crea un método llamado 'describe_
restaurant()' que imprima la información del restaurante, y otro método que
se llame 'open_restaurant()' que imprima un mensaje diciendo que el restaurante
está abierto.

Imprime los dos atributos de forma individual, y después llama a los métodos.
"""

class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} cuisine restaurant.")
    
    def open_restaurant(self):
        print(f"The {self.name} restaurant is opened!")


my_restaurant = Restaurant('Batzoki', 'spanish')

print(my_restaurant.name)               # Batzoki
print(my_restaurant.cuisine_type)       # spanish

my_restaurant.describe_restaurant()     # Batzoki is a spanish cuisine restaurant.
my_restaurant.open_restaurant()         # The Batzoki restaurant is opened!



print("\n\n02 - TRES RESTAURANTES\n")
"""
Partiendo del ejercicio anterior, crea tres instancias diferentes de la clase
que has creado, y llama al método 'describe_restaurant()' con cada uno de los
restaurantes creados.
"""


first_restaurant = Restaurant('Irish Tabern', 'irish')
second_restaurant = Restaurant('Rugby Taberna', 'spanish')
third_restaurant = Restaurant('aaa', 'bbb')

first_restaurant.describe_restaurant()      # Irish Tabern is a irish cuisine restaurant.
second_restaurant.describe_restaurant()     # Rugby Taberna is a spanish cuisine restaurant.
third_restaurant.describe_restaurant()      # aaa is a bbb cuisine restaurant.



print("\n\n03 - USUARIOS\n")
"""
Crea una clase llamada 'User'. Crea 2 atributos llamados 'first_name' y 'last_
name', y añade atributos típicos de un usuario. Crea un método que se llame
'describe_user()' que imprima un resumen de la información del usuario. Crea
otro método llamado 'greet_user()' que imprima un saludo personalizado.
Crea un par de instancias y llama a ambos métodos.
"""

class User:
    def __init__(self, first:str, last:str, age:int, username:str):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.username = username

    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Age: {self.age}\n")

    def greet_user(self):
        print(f"Hi {self.username}! Have a nice day!\n")
    

user_one = User('Naia', 'Larrea', 24, 'nlarrea')
user_two = User('Marcus', 'Fenix', 33, 'delta')

user_one.describe_user()
user_one.greet_user()
""" imprime:
Full name: Naia Larrea
Username: nlarrea
Age: 24

Hi nlarrea! Have a nice day!
"""


user_two.describe_user()
user_two.greet_user()
""" imprime:
Full name: Marcus Fenix
Username: delta
Age: 33

Hi delta! Have a nice day!
"""