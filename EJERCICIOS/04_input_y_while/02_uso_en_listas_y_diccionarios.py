print("01 - BOCATERÍA\n")
"""
Crea una lista llamada 'sandwich_orders' y llénala con el nombre de sandwiches.
Crea una lista vacía llamada 'finished_sandwiches'.
Usa un bucle para recorrer la lista de sandwiches solicitados e imprime un
mensaje para cada uno (por ejemplo: 'I made your tuna sandwich'). A medida que
se prepare el sandwich, muévelo a la lista de sandwiches finalizados.
Cuando todos se hayan hecho, imprime un mensaje listando todos los que se hayan
hecho.
"""

sandwich_orders = ["tuna", "eme", "egg mayo", "corned beed", "cheese and onion"]
finished_sandwiches = []

# si queremos que el primero de la lista sea el primero en mostrarse
# sandwich_orders.reverse()

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order} sandwich.")

    finished_sandwiches.append(sandwich_order)

print("\nThis is the list of the finished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(f"\t- {finished_sandwich}")



print("\n\n02 - NO QUEDA PASTRAMI\n")
"""
Usando la lista de 'sandwich_orders' del ejercicio anterior, introduce en ella
el sandwich 'pastrami' 3 veces. Muestra un mensaje indicando que la bocatería
se ha quedado sin pastrami y usa un bucle 'while' para eliminar todos los
sandwiches de este tipo de la lista 'sandwich_orders'.
Asegúrate de que no entran sandwiches de este tipo en la lista
'finished_sandwiches'
"""

sandwich_orders = ["tuna", "pastrami", "eme", "pastrami", "pastrami", "egg mayo", "corned beed", "cheese and onion"]
finished_sandwiches = []

print("Deli has run out of pastrami!\n")

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()

    if sandwich_order != "pastrami":
        finished_sandwiches.append(sandwich_order)

print("This is the list of the finished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(f"\t- {finished_sandwich}")

# con .pop() ya se eliminan todos los sandwiches de la lista, así que no hace
# falta usar otro bucle para quitar los de tipo pastrami



print("\n\n03 - VACACIONES DE ENSUEÑO\n")
"""
Escribe un programa que pregunte al usuario sobre las vacaciones de sus sueños.
Crea una encuesta que pregunte cosas como 'If you would visit one place in the
world, where would you go?'
Incluye un bloque de código que imprima los resultados de la encuesta.
"""

dream_vacations = {}

while True:
    name = input("\nEnter your name: ")
    response = input("If you would visit one place in the world, where would you go? ")

    dream_vacations[name] = response

    repeat = input("Will anyone else take the poll? (y/n) ")
    if repeat == "n":
        break

print("--- Poll results ---")
for name, response in dream_vacations.items():
    print(f"\t- {name.title()} wants to go to {response.title()}")