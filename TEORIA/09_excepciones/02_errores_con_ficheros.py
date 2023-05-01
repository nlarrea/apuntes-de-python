# ERRORES CON FICHEROS

"""
Algo muy posible a la hora de trabajar con ficheros es que se pretenda usar un
fichero que no se encuentra en la ruta especificada y que se obtenga un error.
Para poder continuar trabajando a pesar de no encontrar dicho archivo, se puede
usar una sentencia try-except.
"""

""" comentado para que no de errores
file_path = "alice.txt"     # no es correcto -> debería ser: ./files/alice.txt

with open(file_path, encoding="utf-8") as f:
    contents = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
"""

"""
El programa anterior da errores porque no está bien especificado el directorio
en el que se encuentra el archivo. ¿Cómo podríamos arreglarlo?
"""

try:
    file_path = "alice.txt"

    with open(file_path, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_path} does not exist.")
# Sorry, the file alice.txt does not exist.



# ANALIZAR ARCHIVOS

file_path = "./files/alice.txt"     # correct path

try:
    with open(file_path, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_path} does not exist.")
else:
    # count the number of words in the file
    words = contents.split()
    word_number = len(words)
    print(f"The file {file_path} has about {word_number} words.")
    # The file ./files/alice.txt has about 29590 words.



# TRABAJAR CON MÚLTIPLES ARCHIVOS

def count_words(file):
    """ count the aproximate number of words in a file """
    try:
        with open(file, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file} does not exist.")
    else:
        words = contents.split()
        word_number = len(words)
        print(f"The file {file} has about {word_number} words!")


filenames = ["alice.txt", "dracula.txt", "bcd.txt", "romeo&juliet.txt"]

for filename in filenames:
    count_words(f"./files/{filename}")
    """ prints:
    The file ./files/alice.txt has about 29590 words!
    The file ./files/dracula.txt has about 164459 words!
    Sorry, the file ./files/bcd.txt does not exist.
    The file ./files/romeo&juliet.txt has about 29002 words!
    """



# ERRORES SILENCIOSOS

"""
En ocasiones quizá no queramos indicar ni dejar constancia de algún error, tal
vez porque el usuario ni siquiera debe preocuparse por ello.
Para esto, existe la palabra reservada 'pass', la cual permite 'pasar' a un
bloque de código sin dar ningún tipo de error.
Repitiendo el último apartado, si cambiáramos el código para que no se mostrara
ningún mensaje de error si no se encontrara el archivo, habría que hacer lo
siguiente:
"""

def count_words_silent_errors(file):
    """ count the aproximate number of words in a file """
    try:
        with open(f"./files/{file}", encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass        # 'failing silently'
    else:
        words = contents.split()
        word_number = len(words)
        print(f"The file {file} has about {word_number} words!")


filenames = ["alice.txt", "dracula.txt", "bcd.txt", "romeo&juliet.txt"]

for filename in filenames:
    count_words_silent_errors(filename)
    """ prints:
    The file alice.txt has about 29590 words!
    The file dracula.txt has about 164459 words!
    The file romeo&juliet.txt has about 29002 words!
    """