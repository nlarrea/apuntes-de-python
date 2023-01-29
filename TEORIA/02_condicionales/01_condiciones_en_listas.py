# COMPROBAR SI UN VALOR ESTÁ EN UNA LISTA -> in
"""
para comprobar si un elemento está o no en una lista, se podría pensar que es
necesario utilizar un bucle para recorrer toda la lista. Sin embargo, existe
la palabra clave 'in' que devuelve True o False indicando si el valor deseado
está o no en la lista
"""

banned_users = ["hack123", "cyanide", "devilHP"]
user = "hack123"

if user in banned_users:
    print(f"{user}, you are BANNED!")   # hack123, you are BANNED!

print(user in banned_users)             # True
print("nlarrea" in banned_users)        # False



# COMPROBAR SI UN VALOR NO ESTÁ EN UNA LISTA -> not in

available_toppings = ["mushrooms", "onions", "pepperoni"]
requested_topping = "pineapple"

if requested_topping not in available_toppings:
    print(f"Sorry, the {requested_topping} is not available.")  # Sorry, the pineapple is not available.



# COMPROBAR QUE UNA LISTA NO ESTÉ VACÍA
"""
no se puede asumir siempre que una lista tiene contenido, por ello, habrá que
comprobar que no esté vacía. Para ello, usaremos una simple sentencia 'if',
Python devolverá True si la lista tiene al menos un elemento y un False si no
tiene ninguno
"""
requested_toppings = []                             # lista vacía

if requested_toppings:                              # False -> no se ejecuta
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:                                               # se ejecuta este bloque
    print("Are you sure you want a plain pizza?")   # Are you sure you want a plain pizza?



# TRATAR CON ÍTEMS CONCRETOS
"""
esta vez sí será necesario utilizar bucles para recorrer la lista completa y
realizar las tareas correspondientes con los valores deseados. Para ello, se
puede utilizar el bucle 'for'
"""

cars = ["audi", "bmw", "renault", "toyota"]

print("Estos son los coches de la lista:")
for car in cars:
    if car == "bmw":
        print(f"\t{car.upper()}")
    else:
        print(f"\t{car.title()}")

""" se imprime:
Estos son los coches de la lista:
    Audi
    BMW
    Renault
    Toyota
"""



# UTILIZAR VARIAS LISTAS
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "extra cheese"]
requested_toppings = ["mushrooms", "pineapple", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

""" se imprime lo siguiente:
Adding mushrooms.
Sorry, we don't have pineapple.
Adding extra cheese.

Finished making your pizza!
"""