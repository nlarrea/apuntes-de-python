print("01 - CARRITO DE HELADO\n")
"""
Un carrito o puesto de helados puede tratarse como una especide de restaurante.
Partiendo de la clase Restaurant utilizada en ejercicios de otros apartados,
crea una nueva clase llamada 'IceCreamStand' que herede de esa clase Rstaurant
y añade un atributo llamado 'flavors' que guarde una lista de sabores de
helados. Escribe un método que muestre los sabores. Crea una instancia de
IceCreamStand y llama a dicho método.
"""

class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} cuisine restaurant.")
    
    def open_restaurant(self):
        print(f"The {self.name} restaurant is opened!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry', 'lemon', 'pistachio']
    
    def get_flavors(self):
        print("These are the available flavors:")

        for flavor in self.flavors:
            print(f"\t- {flavor}")


ice_cream_stand = IceCreamStand('Regma', 'ice cream stand')
ice_cream_stand.get_flavors()
""" se imprime:
These are the available flavors:
    - chocolate
    - vanilla
    - strawberry
    - lemon
"""



print("\n\n02 - ADMINISTRADOR\n")
"""
Un administrador es un tipo especial de usuario. Crea una clase llamada 'Admin'
que herede de la clase User utilizada en ejercicios anteriores. Añádele un
atributo llamado 'privileges' que almacene un listado de strings como 'can add
post', 'can delete post', 'can ban user', etc. Crea un método llamado 'show_
privileges()' que muestre el contenido de dicha lista. Crea una instancia de
Admin y llama al método.
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

""" comentado para que no interfiera en el apartado siguiente
class Admin(User):
    def __init__(self, first: str, last: str, age: int, username: str):
        super().__init__(first, last, age, username)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"These are the privileges of {self.username}:")

        for privilege in self.privileges:
            print(f"\t- {privilege}")


admin = Admin('Naia', 'Larrea', 24, 'nlarrea')
admin.show_privileges()
"""
""" se imprime:
These are the privileges of nlarrea:
    - can add post
    - can delete post
    - can ban user
"""



print("\n\n03 - PRIVILEGIOS\n")
"""
Crea una clase 'Privileges'. La clase debe tener un atributo, 'privileges' que
almacene la lista de strings del ejercicio anterior. Mueve el método 'show_
privileges()' a esta clase. Usa esta clase como atributo en la clase Admin del
apartado anterior. Crea una nueva instancia de Admin y llama a este método.
"""

class Admin(User):
    def __init__(self, first: str, last: str, age: int, username: str):
        super().__init__(first, last, age, username)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"These are the privileges of the admin:")

        for privilege in self.privileges:
            print(f"\t- {privilege}")


admin = Admin('Naia', 'Larrea', 24, 'nlarrea')
admin.privileges.show_privileges()
""" se imprime:
These are the privileges of the admin:
    - can add post
    - can delete post
    - can ban user
"""



print("\n\n04 - MEJORA DE BATERÍA\n")
"""
Añade un método a la clase Battery llamado 'upgrade_battery()'. Este método
debe comprobar el tamaño de la batería y poner su capacidad a 100 si no lo está
ya. Crea un coche eléctrico con la batería por defecto, llama al método 'get_
range()', y llama de nuevo a este método tras modificar la capacidad de la
batería.
Este es el código desde el cual debes partir:

    class Car:
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0

        def get_descriptive_name(self):
            long_name = f"{self.year} {self.make} {self.model}"
            return long_name.title()

        def read_odometer(self):
            print(f"This car has {self.odometer_reading} kilometers on it.")

        def update_odometer(self, kilometers):
            if kilometers >= self.odometer_reading:
                self.odometer_reading = kilometers
            else:
                print("You can't roll back an odometer!")

        def increment_odometer(self, kilometers):
            self.odometer_reading += kilometers

        def fill_gas_tank(self):
            print("Filling the gas tank...")


    class Battery:
        def __init__(self, battery_size=75):
            self.battery_size = battery_size

        def describe_battery(self):
            print(f"This car has a {self.battery_size}-kWh battery.")

        def get_range(self):
            if self.battery_size == 75:
                range = 420
            elif self.battery_size == 100:
                range = 500

            print(f"This car can go about {range} kilometers on a full charge.")


    class ElectricCar(Car):
        def __init__(self, make, model, year):
            super().__init__(make, model, year)
            self.battery = Battery()

        def fill_gas_tank(self):
            print("This car doesn't need a gas tank!")
"""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kilometers on it.")

    def update_odometer(self, kilometers):
        if kilometers >= self.odometer_reading:
            self.odometer_reading = kilometers
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers

    def fill_gas_tank(self):
        print("Filling the gas tank...")


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 420
        elif self.battery_size == 100:
            range = 500
        
        print(f"This car can go about {range} kilometers on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


my_electric_car = ElectricCar('tesla', 'model s', 2019)

my_electric_car.battery.get_range()         # This car can go about 420 kilometers on a full charge.
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()         # This car can go about 500 kilometers on a full charge.