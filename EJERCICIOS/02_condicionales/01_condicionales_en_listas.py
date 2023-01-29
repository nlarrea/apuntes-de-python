print("\n\n01 - FRUTA FAVORITA\n")
"""
Haz una lista que contenga tus frutas favoritas y escribe una serie de sentencias
'if' independientes que comprueben ciertas frutas de tu lista:

- Escribe al menos 5 sentencias donde si la fruta está en la lista, se muestre
un mensaje como "¡Pues sí que te gustan los plátanos!"
"""

favorite_fruits = ["strawberries", "grapes", "melons"]

if "bananas" in favorite_fruits:
    print("You really like bananas!")
if "melons" in favorite_fruits:
    print("You really like melons!")        # sí se imprime
if "strawberries" in favorite_fruits:
    print("You really like strawberries!")  # sí se imprime
if "grapes" in favorite_fruits:
    print("You really like grapes!")        # sí se imprime
if "apples" in favorite_fruits:
    print("You really like apples!")



print("\n\n02 - HOLA ADMIN\n")
"""
Crea una lista con el nombre de 5 usuarios, incluyendo el nombre 'admin'.
Imagina que vas a crear un programa que salude a cada usuario tras iniciar la
sesión. Recorre la lista e imprime un saludo a cada usuario:

- Si el usuario es 'admin', imprime un saludo especial.
- Si no es el administrador, imprime un saludo genérico.
"""

users = ["nlarrea", "nloust", "admin", "jajunait", "user123"]

for user in users:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again!")



print("\n\n03 - SIN USUARIOS")
"""
Partiendo del ejercicio anterior, crea una sentencia 'if' para asegurarte de
la lista 'users' no está vacía antes de usarla.

- Si la lista está vacía, imprime un mensaje indicando que faltan usuarios.
- Elimina todos los nombres de usuario y asegúrate de que se imprime el mensaje.
"""

users.clear()

if users:                                   # users vacía -> no ejecuta el 'if'
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again!")
else:
    print("We need to find some users!")    # se imprime este mensaje



print("\n\n04 - COMPROBAR NOMBRES DE USUARIOS\n")
"""
Haz lo siguiente para crear un programa que se asegure de que en una web no hay
nombres de usuario repetidos:

- Crea una lista con 5 nombres de usuaios llamada 'current_users'.
- Crea otra lista de 5 usuarios llamada 'new_users'. Asegúrate de que alguno de
los usuarios aparezca en las dos listas.
- Recorre la lista de 'new_users' para ver si algún usuario nuevo está ya
registrado.
    - Si no lo está, imprime un mensaje de que el nombre está disponible.
    - Si está, imprime un mensaje diciendo que necesitará introducir otro nombre
    de usuario.
"""

current_users = ["nlarrea", "nloust", "naia98", "jajunait", "user123"]
new_users = ["junee", "user123", "fullJS", "user321", "other_user"]

for user in new_users:
    if user in current_users:
        print("Sorry, you will have to enter a new username.")
    else:
        print(f"The username {user} is available!")



print("\n\n05 - NÚMEROS ORDINALES\n")
"""
En inglés, todos los números ordinales acaban en 'th', excepto el 1, 2 y 3, que
terminan en 'st', 'nd' y 'rd' respectivamente.

- Guarda los números del 1 al 9 en una lista.
- Recorre la lista.
- Usa una sentencia 'if-elif-else' para imprimir de forma adecuada los números
ordinales, cada uno en una línea.
"""

numbers = [*range(1, 10)]   # crea una lista con los números del 1 al 9

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")