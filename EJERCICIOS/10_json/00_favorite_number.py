""" 
Crea un programa que pida a un usuario su número favorito la primera vez que se
ejecute el programa. En las siguientes ocasiones, el código debe mostrar un
mensaje que indique cuál ha sido el número favorito que introdujo el usuario.
"""

import json

def show_favorite_number():
    fav_number = get_stored_number()

    if fav_number:
        print(f"Your favorite number is: {fav_number}!")
    else:
        fav_number = get_new_number()
        print(f"Okay, I'll remember that your favorite number is {fav_number}")


def get_stored_number():
    filename = "./files/favorite_number.json"

    try:
        with open(filename) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_number
    

def get_new_number():
    filename = "./files/favorite_number.json"
    fav_number = input("Enter your favorite number: ")

    with open(filename, "w") as f:
        json.dump(fav_number, f)
    
    return fav_number


show_favorite_number()