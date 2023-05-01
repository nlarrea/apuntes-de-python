print("01 - SUMATORIO\n")
"""
Un problema muy común al trabajar con datos numéricos ocurre cuando un usuario
introduce un dato de tipo texto en lugar de uno numérico. Al tratar de pasar el
dato a tipo 'int' se nos devuelve un ValueError.
Crea un programa que pida dos números al usuario, realiza la suma e imprime el
resultado. Maneja el ValueError para que se muestre un mensaje si el usuario no
introduce los tipos de datos correctos.
"""

try:
    number_one = int(input("Enter number: "))
    number_two = int(input("Enter another number: "))
except ValueError:
    print("You should enter two numbers!")
else:
    print(f"{number_one} + {number_two} = {number_one + number_two}")



print("\n\n02 - CALCULADORA DE SUMAS\n")
"""
Copia tu código anterior e insértalo en un bucle 'while' para que el usuario
pueda introducir números incluso cuando cometa el error de meter un dato con
formato de texto en vez de numérico.
"""

while True:
    try:
        num_one = int(input("Enter a number: "))
        num_two = int(input("Enter a second number: "))
    except ValueError:
        print("You should enter an integer number!")
    else:
        print(f"{num_one} + {num_two} = {num_one + num_two}")
        break



print("\n\n03 - GATOS Y PERROS\n")
"""
Crea dos archivos: 'cats.txt' y 'dogs.txt'. Introduce al menos 3 nombres tanto
de gatos como de perros. Crea un programa que trate de leer los nombres de los
archivos y los imprima por consola. Crea un bloque try-except para manejar el
posible error de FileNotFoundError.
"""

filenames = ["cats.txt", "dogs.txt"]

def read_content(file):
    """ read de content of a file """
    try:
        with open(f"./files/{file}") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Sorry, couldn't find the '{file}' file...")
    else:
        print(f"These are the names from the '{file}' file:")
        for line in lines:
            print(f"\t- {line.strip()}")


for filename in filenames:
    read_content(filename)



print("\n\n04 - GATOS Y PERROS SILENCIADO\n")
"""
Modifica el bloque 'except' del ejercicio anterior para que no se muestre al
usuario ningún mensaje si los archivos no se encuentran.
"""

filenames = ["cats.txt", "dogs.txt"]

def read_content_silent(file):
    """ read de content of a file """
    try:
        with open(f"./files/{file}") as f:
            lines = f.readlines()
    except FileNotFoundError:
        pass
    else:
        print(f"These are the names from the '{file}' file:")
        for line in lines:
            print(f"\t- {line.strip()}")


for filename in filenames:
    read_content_silent(filename)