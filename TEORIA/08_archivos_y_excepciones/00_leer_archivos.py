# LEER ARCHIVOS

"""
Trabajar con archivos es una habilidad importante para manejar grandes
cantidades de datos.
En este apartado vamos a ver cómo abrir archivos, cómo leer esa información, y
cómo evitar los posibles errores que conlleve intentar leer dicha información.
"""



# LEER UN ARCHIVO ENTERO

"""
Vamos a crear un archivo con la información de una persona: person_data.txt
Este archivo contiene las siguientes líneas:

    Naia
    Larrea
    nlarrea
    24

Para poder leer archivos, primero deben ser accesibles -> deben abrirse

Para abrir un archivo se utiliza 'open()', sin embargo, los archivos abiertos
deben cerrarse siempre para evitar problemas, por lo que se necesita utilizar
'close()' al terminar de usar dicho archivo. Pero, ¿cuándo deja de usarse un
archivo? ¿cómo sabemos cuándo podemos cerrar el archivo?

Para hacerlo todo más fácil, Python incluye la opción de usar 'with' antes del
'open()', que hace que se cierre siempre el archivo y de forma automática cada
vez que éste no se use más
"""

# abrir archivo
with open('person_data.txt') as file:
    # leer todo el contenido del archivo y almacenarlo en 'contents'
    contents = file.read()

print(contents.rstrip())
""" imprime:
Naia
Larrea
nlarrea
24
"""



# PATH (ruta) DE LOS ARCHIVOS

"""
No siempre se va a trabajar con un archivo que se encuentre en el mismo lugar o
directorio que el archivo Python que deba acceder a él. Por ello, se pueden
especificar las direcciones o rutas (path) de los archivos.

Creamos el directorio 'files' e insertamos dentro un bloc de notas que contiene
algunos decimales del número pi:

    3.1415926535
      8979323846
      2643383279

En este caso vamos a TRABAJAR CON UNA RUTA RELATIVA, es decir, se indica solo
la ruta a seguir desde el directorio en el que se encuentra el archivo Python
que debe abrir el archivo, en este caso:

    path (relative) = ./files/pi_digits.txt

'./' no es obligatorio en este caso, pero sirve para representar el directorio
actual

Si se quieren escribir las rutas con '\' en lugar de '/', se deben usar dos
barras (ejemplo):

    C:\\path\\to\\file.txt
"""

with open('files/pi_digits.txt') as file:
    contents = file.read()

print(contents)
""" imprime:
3.1415926535
  8979323846
  2643383279
"""

""" TRABAJAR CON RUTAS ABSOLUTAS
Las rutas absolutas son más largas que las relativas, por lo que suele ser una
buena práctica almacenarlas en una variable para mantener el código más limpio
"""

file_path = "C:/Users/larre/Desktop/apuntes-de-python/TEORIA/08_archivos_y_excepciones/files/pi_digits.txt"

with open(file_path) as file:
   contents = file.read()

print(contents)
""" imprime:
3.1415926535
  8979323846
  2643383279
"""



# LEER UN ARCHIVO LÍNEA A LÍNEA

"""
En ocasiones se desea leer el contenido de un archivo línea a línea debido a
que es más cómodo para trabajar. Para ello, se debe abrir primero el archivo,
al igual que lo visto hasta ahora, y a continuación, hacer lo siguiente:
"""

with open('person_data.txt') as file_obj:
    for line in file_obj:
        print(line)
""" imprime:
Naia

Larrea

nlarrea

24
"""

""" ELIMINAR LOS ESPACIOS EN BLANCO
Como se puede observar, se añaden espacios en blanco al imprimir cada una de
las líneas, para evitar dichos saltos, se puede usar el método '.rstrip()'
"""

with open('person_data.txt') as file:
    for line in file:
        print(line.rstrip())
""" imprime:
Naia
Larrea
nlarrea
24
"""



# CREAR UNA LISTA CON LAS LÍNEAS DE UN ARCHIVO

"""
Si queremos acceder a las líneas del archivo desde fuera de la sentencia 'with'
debemos guardarlas en una lista. Para ello, se puede hacer uso del método
'.readlines()', el cual crea esa lista
"""

with open('person_data.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())
""" imprime:
Naia
Larrea
nlarrea
24
"""