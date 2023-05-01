# REFACTORIZACIÓN

"""
Este apartado no tiene nada que ver con los archivos JSON, sin embargo, es una
parte importante, así que vamos a verla aquí y a utilizar ejemplos vistos con
archivos JSON para trabajarlo.

Hay ocasiones en las que el código funciona perfectamente, pero podría tener
una estructura mejor. Llegados a este punto, vamos a repetir el último ejemplo
del apartado anterior, dividiendo el código en funciones que lo hagan más
sostenible.
"""

import json

def say_hi_to_user():
    """ Greet user by name """
    filename = "./files/username.json"

    try:
        with open(filename) as f:
            user_name = json.load(f)
    except FileNotFoundError:
        user_name = input("Enter your name: ")
        with open(filename, "w") as f:
            json.dump(user_name, f)
        print(f"{user_name}, we will remember your name for the next time!")
    else:
        print(f"Welcome back, {user_name}!")

    
# say_hi_to_user()      # comentarlo para que no se ejecute



"""
El código mostrado funciona, pero la función utilizada hace más que simplemente
saludar al usuario.
Vamos a REFACTORIZAR el código dividiéndolo en funciones más simples que tengan
un único proposito:
"""

def get_stored_username():
    """ Get stored user name if available. """
    filename = "./files/username.json"

    try:
        with open(filename) as f:
            user_name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user_name
    

def get_new_username():
    """ Prompt for a new user name. """
    user_name = input("Enter your name: ")
    filename = "./files/username.json"

    with open(filename, "w") as f:
        json.dump(user_name, f)
    
    return user_name


def greet_user():
    """ Greet the user by name """
    user_name = get_stored_username()

    if user_name:
        print(f"Welcome back, {user_name}!")
    else:
        user_name = get_new_username()
        print(f"{user_name}, we will remember you when you come back!")


greet_user()