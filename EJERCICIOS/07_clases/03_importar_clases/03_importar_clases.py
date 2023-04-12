print("01 - RESTAURANTE IMPORTADO\n")
"""
Utilizando la última clase de Restaurant, guárdala en un nuevo módulo. Importa
aquí dicha clase y crea una instancia, no olvides utilizar algun método de la
clase para comprobar que funciona.
"""

from restaurant import Restaurant

my_restaurant = Restaurant('Batzoki', 'spanish')
my_restaurant.describe_restaurant()         # Batzoki is a spanish cuisine restaurant.



print("\n\n02 - ADMINISTRADOR IMPORTADO\n")
"""
Crea un nuevo módulo y guarda en él las clases Admin, User y Privileges usadas
en ejercicios del apartado anterior. Crea una instancia de Admin y llama al
método 'show_privileges()' de dicha clase.
"""

from user import Admin

admin = Admin('Naia', 'Larrea', 24, 'nlarrea')
admin.privileges.show_privileges()
""" se imprime:
These are the privileges of the admin:
    - can add post
    - can delete post
    - can ban user
"""



# EJERCICIOS USANDO LIBRERÍAS PROPIAS DE PYTHON

print("\n\n03 - DADO\n")
"""
Crea una clase 'Die' con un atributo llamado 'sides', con un valor por defecto
de 6. Crea un método llamado 'roll_die()' que imprima un número aleatorio entre
1 y la cantidad de caras del dado. Crea también dados de 10 y 20 caras, y llama
a los métodos varias veces para comprobar que funcionan.
"""

from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"{randint(1, self.sides)}")


six_sides_die = Die()
six_sides_die.roll_die()        # 1
six_sides_die.roll_die()        # 1
six_sides_die.roll_die()        # 6
six_sides_die.roll_die()        # 3

ten_sides_die = Die(10)
ten_sides_die.roll_die()        # 4
ten_sides_die.roll_die()        # 1
ten_sides_die.roll_die()        # 8
ten_sides_die.roll_die()        # 9

twenty_sides_die = Die(20)
twenty_sides_die.roll_die()     # 6
twenty_sides_die.roll_die()     # 19
twenty_sides_die.roll_die()     # 7
twenty_sides_die.roll_die()     # 5



print("\n\n04 - LOTERÍA\n")
"""
Crea una lista o tupla que contenga una serie de 10 números y 5 letras. Escoge
de forma aleatoria 4 números y/o letras de la lista, e imprime un mensaje que
indique que la papeleta que contenga dicha secuencia, gana.
"""

from random import choices

lottery_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'e', 'i', 'o', 'u']
sequence = ''

for item in choices(lottery_options, k=4):
    sequence += str(item)

print(f"Any ticket matching the '{sequence}' sequence wins the lottery!")
# Any ticket matching the 'e38u' sequence wins the lottery!