"""
Crea un programa que pida el nombre de usuario la primera vez que se ejecute.
Las siguientes veces, preguntará si es correcto que ese nombre de usuario es
quien ha ejecutado el programa. Si la respuesta del usuario indica que no, se
volverá a tomar la información del nombre de usuario.
"""

import json

def get_stored_username():
    filename = "./files/username.json"

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    filename = "./files/username.json"
    username = input("Enter your username: ")

    with open(filename, "w") as f:
        json.dump(username, f)
    
    return username


def ask_correct_username(username):
    while True:
        answer = input(f"Is '{username}' your username? (y/n): ")

        if answer.lower() == "y": return True
        elif answer.lower() == "n": return False
        else: print(f"Sorry, {answer} is not a valid answer.\n")


def greet_user():
    username = get_stored_username()

    if username:
        is_correct_username = ask_correct_username(username)
        if is_correct_username:
            print(f"Welcome back, {username}!")

    if not username or not is_correct_username:
        username = get_new_username()
        print(f"Hello, {username}! I'll remember you when you come back!")


greet_user()