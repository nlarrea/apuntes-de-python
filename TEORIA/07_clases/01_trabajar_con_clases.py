# TRABAJAR CON CLASES Y SUS INSTANCIAS

"""
Cuando se utilizan clases, se termina trabajando principalmente con aquellas
instancias creadas a partir de dicha clase.
En varias ocasiones, se querrán modificar los atributos o métodos para alguna
instancia en particular. Se pueden modificar los atributos de una instancia de
forma directa, o a través de métodos que actualicen los atributos.
"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # ATRIBUTO POR DEFECTO
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    # ATRIBUTO POR DEFECTO
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} km on it.")

    # MODIFICAR EL VALOR DE LOS ATRIBUTOS
    # 2. Modificar el valor a través de un método
    def update_odometer(self, kilometers):
        # self.odometer_reading = kilometers

        # código añadido para ejecutar cada vez que se modifique el valor
        if kilometers >= self.odometer_reading:
            self.odometer_reading = kilometers
        else:
            print("You can't roll back an odometer!")
    
    # 3. Aumentar el valor a través de un método
    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())            # 2019 Audi A4



# ATRIBUTOS POR DEFECTO
"""
Se pueden definir atributos en una clase sin tener que pasar un argumento al
crear la instancia.
Al crear instancias de la clase Car, SIEMPRE van a tener el mismo valor del
atributo 'odometer_reading', ya que éste ni se actualiza, ni se inicializa con
un valor diferente.

Vamos a añadir también el método 'read_odometer()' para leer el valor de la
variable.
"""

my_new_car.read_odometer()          # This car has 0 km on it.



# MODIFICAR EL VALOR DE LOS ATRIBUTOS

"""
Se pueden modificar los valores de los atributos de 3 formas:
    1. Modificar el valor directamente
    2. Modificar el valor a través de un método
    3. Aumentar el valor a través de un método
"""

# 1. Modificar el valor directamente
my_new_car.odometer_reading = 230
my_new_car.read_odometer()          # This car has 230 km on it.


# 2. Modificar el valor a través de un método
# añadimos el método 'update_odometer()' a la clase Car
my_new_car.update_odometer(450)
my_new_car.read_odometer()          # This car has 450 km on it.

# podemos decir a la función que haga algo cuando el valor se modifique
my_new_car.read_odometer()          # # This car has 450 km on it.
my_new_car.update_odometer(180)     # You can't roll back an odometer!
my_new_car.read_odometer()          # # This car has 450 km on it.
# el valor anterior no se ha visto modificado


# 3. Aumentar el valor a través de un método
"""
A veces se preferirá incrementar el valor en cantidades fijas en lugar de dar
un valor totalmente nuevo/diferente al atributo. Por ejemplo, añadir 100 km
cada vez que se llame a un método.

Vamos a verlo creando el método 'increment_odometer()' y creando una nueva
instancia de la clase Car
"""

my_used_car = Car('renault', 'scenic', 1999)
print(my_used_car.get_descriptive_name())       # 1999 Renault Scenic

my_used_car.update_odometer(230_500)
my_used_car.read_odometer()                     # This car has 230500 km on it.

my_used_car.increment_odometer(100)
my_used_car.read_odometer()                     # This car has 230600 km on it.



""" por qué usar métodos?
Como se puede ver en el último caso, al utilizar el método 'update_odometer()',
no se puede modificar el valor del atributo si el nuevo valor es menor que el
que tenía antes.
Si intentamos modificar el valor del atributo de forma directa en vez de llamar
al método, lo modificaríamos a nuestro antojo, lo cual puede no ser correcto.
"""

# esto no debería ser posible y no es una buena práctica:
# my_new_car.odometer_reading = -123
# my_new_car.read_odometer()        # This car has -123 km on it.