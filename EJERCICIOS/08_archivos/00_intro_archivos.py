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