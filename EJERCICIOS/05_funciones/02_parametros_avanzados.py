print("01 - SANDWICHES\n")
"""
Escribe una función que acepte una lista de ítems que una persona quiera añadir
en su sandwich. La función debe tener un parámetro que recoja tantos ítems como
la llamada a dicha función envíe, y debe imprimir un resumen del sandwich que
se va a preparar.
Llama a la función 3 veces, usando diferente cantidad de ítems.
"""

def make_sandwich(*args):
    print("The ordered sandwich contains the next items:")
    for arg in args:
        print(f"\t- {arg}")
    
    print()


make_sandwich("tomato", "lettuce", "boiled egg")
""" prints:
The ordered sandwich contains the included items:
    - tomato
    - lettuce
    - boiled egg
"""

make_sandwich("ham", "cheese slice")
""" print:
The ordered sandwich contains the included items:
    - ham
    - cheese slice
"""

make_sandwich("french omelet", "cheese", "ham")
""" print:
The ordered sandwich contains the included items:
    - french omelet
    - cheese
    - ham
"""



print("\n\n02 - PERFIL DE USUARIO\n")
"""
Crea un perfil de ti mismo llamando a la función 'build_profile()', usando tu
nombre, apellido y otros tres pares clave-valor que te describan.
"""

def build_profile(first_name, last_name, **kwargs):
    user_info = {}
    
    user_info["firts_name"] = first_name
    user_info["last_name"] = last_name
    
    for key, val in kwargs.items():
        user_info[key] = val
    
    return user_info


user = build_profile("Naia", "Larrea",
              age = 24,
              is_developer = True)
print(user)

""" another way of doing the same thing:

def build_profile(first, last, user_info):
    user_info['first'] = first
    user_info['last'] = last

    return user_info

difference -> this way doesn't have the name and surname in the first and
second position of the dictionary, which is not bad, but personally I rather
see them at the beginning of the object
"""



print("\n\n03 - COCHES\n")
"""
Crea una función que guarde información sobre un coche en un diccionario. La
función siempre debe recibir el fabricante y el modelo. Después, debe aceptar
una cantidad arbitraria de claves. Crea el diccionario llamándolo con al menos
dos pares clave-valor nuevos.
"""

def make_car(manufacturer, model, **kwargs):
    car = {}

    car["manufacturer"] = manufacturer
    car["model"] = model

    for key, val in kwargs.items():
        car[key] = val
    
    return car


car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
# {'manufacturer': 'subaru', 'model': 'outback', 'color': 'blue', 'tow_package': True}

car = make_car("renault", "kadjar", color="dark blue")
print(car)
# {'manufacturer': 'renault', 'model': 'kadjar', 'color': 'dark blue'}