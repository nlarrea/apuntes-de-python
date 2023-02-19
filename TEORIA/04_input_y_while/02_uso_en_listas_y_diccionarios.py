# USO DE input() Y while EN LISTAS Y DICCIONARIOS

""" FOR O WHILE?
- for -> útil cuando quieres recorrer la lista, pero si lo que quieres es
modificar la lista, Python puede dar problemas

- while -> para modificar una lista a medida que la vas recorriendo, es mejor
usar bucles 'while', son muy usados con listas y diccionarios
"""

# MOVER ÍTEMS DE UNA LISTA A OTRA

unconfirmed_users = ["naia", "cris", "june"]
confirmed_users = []

while unconfirmed_users:
    # se elimina el usuario de la lista, guardando su valor en la variable
    current_user = unconfirmed_users.pop()
    print(f"Verified user: {current_user.title()}")

    # se guarda el usuario recién eliminado en la nueva lista
    confirmed_users.append(current_user)

# mostramos todos los usuarios confirmados
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(f"\t{confirmed_user.title()}")



# ELIMINAR TODOS LOS ELEMENTOS IGUALES DE UNA LISTA

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)         # ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while "cat" in pets:
    pets.remove("cat")

print(pets)         # ['dog', 'dog', 'goldfish', 'rabbit']



# RELLENAR UN DICCIONARIO CON LA ENTRADA DE USUARIO

responses = {}              # empty dictionary

polling_active = True       # a flag to exit the loop

while polling_active:
    # prompt for the person's name and response
    name = input("Enter your name: ")
    response = input("What is your favourite color? ")
    
    # store the response in the dictionary
    responses[name] = response

    # ask if anyone else is going to take the poll
    repeat = input("Would another person respond too? (y/n): ")
    if repeat == "n":
        polling_active = False

# show the results
print("\n--- Poll results ---")
for name, response in responses.items():
    print(f"{name.title()}'s favourite color is {response}.")