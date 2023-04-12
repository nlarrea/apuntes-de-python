# INSTANCIAS COMO ATRIBUTOS

"""
En ocasiones acabamos detallando tanto una clase que ésta acaba ocupando mucho,
pudiendo reducir su tamaño si algunos de sus atributos y métodos formaran parte
de otra clase.
Esto puede hacerse creando dicha clase y haciendo que ésta sea un atributo de
la clase en la que estábamos trabajando.

Continuando con las clases generadas en el apartado anterior (herencia.py), se
ve que podemos alargar mucho la clase de ElectricCar si definimos la batería de
éstas instancias. Para evitar que esta clase siga creciendo tanto, lo que sí
podemos hacer es crear una nueva clase 'Battery' y trasladar estos atributos y
métodos a la misma.
"""

# CLASE ORIGINAL
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


# CLASE BATTERY -> descripción de las baterías de las instancias de ElectricCar
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    # método que antes estaba en la clase ElectricCar
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    # métodos nuevos que describen mejor la batería de los ElectricCar
    def get_range(self):
        if self.battery_size == 75:
            range = 420
        elif self.battery_size == 100:
            range = 500
        
        print(f"This car can go about {range} kilometers on a full charge.")


# CLASE HIJA
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()        # instancia de Battery como atributo
    
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


# creación de instancia de la clase ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())   # 2019 Tesla Model S
my_tesla.battery.describe_battery()      # This car has a 75-kWh battery.

my_tesla.battery.get_range()
# This car can go about 420 kilometers on a full charge.