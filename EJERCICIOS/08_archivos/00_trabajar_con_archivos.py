print("01 - APRENDIENDO PYTHON\n")
"""
Crea un archivo de texto desde 0 y añádele algunas líneas resumiendo cosas que
hayas aprendido en este curso sobre Python. Sigue el siguiente formato:

    In Python you can ...

Imprime el contendido en todos los casos:
- Lee el archivo entero
- Lee el archivo línea a línea
- Guarda el contenido en una lista de líneas
"""

file_path = "files/learning_python.txt"

print("- lee el archivo entero:")
with open(file_path) as file:
    content = file.read()

print(content)


print("\n- leer línea a línea:")
with open(file_path) as file:
    for line in file:
        print(line.rstrip())


print("\n- guardar el contenido en una lista de líneas:")
with open(file_path) as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

""" en todos los casos se imprime:
In Python you can create variables
In Python you can use conditionals
In Python you can create dictionaries
In Python you can ask users for input
In Python you can define functions and classes
In Python you can export and import data
"""



print("\n\n02 - APRENDIENDO C\n")
"""
Se puede usar el método 'replace()' para sustituir parte de un string por otro.
Vuelve a leer cada línea del archivo del apartado anterior, y sustituye Python
por el lenguaje 'C'. Imprime cada línea modificada.
"""

with open(file_path) as file:
    for line in file:
        print(line.replace("Python", "C").rstrip())
""" imprime:
In C you can create variables
In C you can use conditionals
In C you can create dictionaries
In C you can ask users for input
In C you can define functions and classes
In C you can export and import data
"""



print("03 - INVITADO\n")
"""
Escribe un programa que pida al usuario que escriba su nombre. Escribe el
nombre introducido en un archivo llamado 'guest.txt'.
"""

user_name = input("Enter your name: ")

file_path = "files/guest.txt"
with open(file_path, "w") as file:
    file.write(f"- {user_name}\n")



print("\n\n04 - LISTA DE INVITADOS\n")
"""
Utiliza un bucle while para pedir el nombre de varios usuarios. Cuando escriban
su nombre, muestra por pantalla un mensaje personalizado y escribe una línea
que recuerde su visita en 'guest_book.txt'.
"""

file_path = "files/guest_book.txt"

while True:
    user_name = input("Enter your name: ")
    if user_name != "" and user_name != "q":
        print(f"Hello {user_name}! Have a nice day!")

        with open(file_path, "a") as file:
            file.write(f"- {user_name}\n")
    else:
        break



print("\n\n05 - ENCUESTA\n")
"""
Crea un bucle while que pregunte al usuario por qué le gusta la programación.
Mientras se escriban respuestas, añádelas a un archivo que contenga todas las
respuestas.
"""

file_path = "files/poll_answers.txt"

while True:
    reason = input("Enter a reason why you like programming: ")
    if reason != "" and reason != "q":
        print(f"- {reason}")

        with open(file_path, "a") as file:
            file.write(f"- {reason}")
    else:
        break