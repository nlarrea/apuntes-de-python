print("01 - NÚMERO SERVIDO\n")
"""
Partiendo de este código:

    class Restaurant:
        def __init__(self, restaurant_name:str, cuisine_type:str):
            self.name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"{self.name} is a {self.cuisine_type} cuisine restaurant.")

        def open_restaurant(self):
            print(f"The {self.name} restaurant is opened!")

Añade un atributo llamado 'number_served' con un valor inicial por defecto
igual a 0. Crea una instancia llamada 'restaurant'. Imprime el número de
clientes a los que ha servido el restaurante, modifica su valor e imprimelo de
nuevo.
Añade un método llamado 'set_number_served()' que te permita modificar el valor
al que tu desees. Llama al método e imprime el valor a continuación.
Añade un método llamado 'increment_number_served()' que te permita incrementar
el número de clientes servidos. Llama al método e imprime el valor de nuevo.
"""

class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} cuisine restaurant.")

    def open_restaurant(self):
        print(f"The {self.name} restaurant is opened!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant('Aldapeko', 'spanish')

print(restaurant.number_served)             # 0
restaurant.number_served = 10
print(restaurant.number_served)             # 10

restaurant.set_number_served(23)
print(restaurant.number_served)             # 23

restaurant.increment_number_served(15) 
print(restaurant.number_served)             # 38



print("\n\n02 - INTENTOS DE INICIO DE SESIÓN\n")
"""
Partiendo del siguiente código:

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

Añade un atributo llamado 'login_attempts' a la clase User. Escribe un método
llamado 'increment_login_attempts()' que incremente en 1 el valor del atributo
'login_attempts'. Escribe otro método llamado 'reset_login_attempts()' que haga
que el valor de 'login_attempts' vuelva a ser 0.
Crea una instancia de User y llama al método 'increment_login_attempts()' unas
pocas veces. Imprime el valor de 'login_attempts' para comprobar que se ha
modificado su valor, entonces llama a 'reset_login_attempts()' e imprime de
nuevo el valor.
"""

class User:
    def __init__(self, first:str, last:str, age:int, username:str):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Age: {self.age}\n")

    def greet_user(self):
        print(f"Hi {self.username}! Have a nice day!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


my_user = User('Naia', 'Larrea', 24, 'nlarrea')

print(my_user.login_attempts)           # 0
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print(my_user.login_attempts)           # 3

my_user.reset_login_attempts()
print(my_user.login_attempts)           # 0