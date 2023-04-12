# IMPORTAR CLASES

"""
Incluso utilizando las propiedades de la herencia de forma correcta, puede que
en ocasiones las clases acaben ocupando demasiado.
Para evitar esto, Python permite almacenar las clases en módulos e importarlas.
"""



# IMPORTAR UNA ÚNICA CLASE

"""
Vamos a crear un módulo que contenga la clase Car, y vamos a llamarlo 'car.py'.
A continuación, importamos la clase Car de la siguiente manera:
"""

from car import Car

# comprobación de que se ha importado correctamente:
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())        # 2019 Audi A4

my_new_car.odometer_reading = 230
my_new_car.read_odometer()                      # This car has 230 kilometers on it.



# GUARDAR MÚLTIPLES CLASES EN UN MÓDULO

"""
Se pueden guardar varias clases en un único módulo. La recomendación es que se
almacenen en un único módulo aquellas clases que tengan relación entre sí.
En el módulo de car.py, podemos introducir las clases ElectricCar y Battery que
hemos visto en apartados anteriores.
"""

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())          # 2019 Tesla Model S

my_tesla.battery.describe_battery()             # This car has a 75-kWh battery.
my_tesla.battery.get_range()                    # This car can go about 420 kilometers on a full charge.



# IMPORTAR MÚLTIPLES CLASES DE UN MÓDULO

"""
Para importar múltiples clases, se debe realizar lo mismo que se hacía con los
módulos en el apartado '06-modulos':

    from car import Car, ElectricCar
"""



# IMPORTAR UN MÓDULO ENTERO

"""
Para importar un módulo entero, podemos realizar lo siguiente:

    import car

Se ha de tener en cuenta que al importar de esta forma, las instancias de las
clases deben crearse de la siguiente manera:

    my_car = car.Car('aaa', 'bbb', 123)
"""



# IMPORTAR TODAS LAS CLASES DE UN MÓDULO

"""
Para importar todas las clases, se usa la siguiente sintaxis:

    from car import *

Ahora, no sería la notación con punto para poder crear las instancias:

    my_car = Car('aaa', 'bbb', 123)
"""



# UTILIZAR ALIAS

"""
Se pueden usar alias para renombrar lo que se haya importado de la siguiente
manera:
"""

from car import ElectricCar as EC

my_electric_car = EC('tesla', 'roadster', 2020)
print(my_electric_car.get_descriptive_name())       # 2020 Tesla Roadster