# HERENCIA (inheritance)

"""
En ocasiones se crean clases que tienen muchas cosas en común con otras. En
estos casos, una de las clases incluso podría ser creada a partir de otra, es
decir, podría crearse una clase que heredara propiedades de la otra.
La clase 'original' se dice que es la clase 'padre' o 'madre', mientras que la
otra es la clase 'hija'.
La clase hija puede heredar alguno o todos los atributos y métodos de la clase
original, sin embargo, también pueden ser modificados para ser diferentes.
"""



# EL MÉTODO __init__() PARA CLASES HIJAS

"""
Cuando se crea una clase hija, a veces se quiere llamar al método __init__() de
la clase padre.
Vamos con el siguiente ejemplo:
"""

# clase original / padre / madre:
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

    # ANULAR MÉTODO EN LA CLASE HIJA
    def fill_gas_tank(self):
        print("Filling the gas tank...")


# clase hija / heredera
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # llama al método __init__() de la clase original
        super().__init__(make, model, year)
        # ATRIBUTO PROPIO DE LA CLASE HIJA
        self.battery_size = 75
    
    # MÉTODO PROPIO DE LA CLASE HIJA
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    # ANULAR MÉTODO DE LA CLASE ORIGINAL
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
    

# creamos una instancia de la clase hija
my_tesla = ElectricCar('tesla', 'model s', 2019)

# obtiene todos los argumentos y métodos por defecto
print(my_tesla.get_descriptive_name())          # 2019 Tesla Model S

"""
Hasta este punto, las instancias de la clase ElectricCar trabajan DE LA MISMA
FORMA que una instancia cualquiera de la clase Car. Es decir, es como si ambas
clases fueran IGUALES
"""



# DEFINIR ATRIBUTOS Y MÉTODOS PARA LA CLASE HIJA

"""
Se le pueden añadir atributos y métodos propios a la clase hija. Éstos no serán
añadidos a la clase original.

Añadimos el atributo 'battery_size' y el método 'describe_battery()' a la clase
hija.
"""

# comprobamos que el atributo y método propios funcionan instancias ElectricCar
my_tesla.describe_battery()             # This car has a 75-kWh battery.



# ANULAR MÉTODOS DE LA CLASE ORIGINAL

"""
Se pueden anular métodos de la clase original que no queramos mantener en las
clases hijas. Para ello, se crea un método con el mismo nombre que el método a
anular de la clase original.

Creamos un método en la clase Car llamado 'fill_gas_tank()'. Este método no
sirve de nada en la clase ElectriCar, por lo que en esta segunda clase vamos a
anular el método.
"""

# instancia de la clase Car (clase original)
my_car = Car('renault', 'scenic', 1999)

# comparación del mismo método en instancias de ambas clases
my_car.fill_gas_tank()                  # Filling the gas tank...
my_tesla.fill_gas_tank()                # This car doesn't need a gas tank!