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