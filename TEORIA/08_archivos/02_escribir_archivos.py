# ESCRIBIR ARCHIVOS

""" FORMAS DE ABRIR UN ARCHIVO
'r' -> por defecto si no lo especificamos = read mode

'w' -> para escribir un archivo desde 0 (se borra el contenido anterior). Si no
existía un archivo con ese nobre, lo crea = writing mode

'a' -> para escribir un archivo desde el último punto de éste, o desde cero si
no existía un archivo con ese nombre = append mode

"""

# ESCRIBIR EN UN ARCHIVO VACÍO -> "w" (writing mode)

"""
Para escribir en un archivo vacío, primero hay que abir el archivo como se ha
hecho hasta ahora con 'open()', pero esta vez, añadiendo un segundo argumento
al usar esta función: 'w'.

'w' indica que queremos abrir el archivo en modo escritura

Si no existe el archivo en el que queremos escribir, Python lo creará, pero si
ya existe el archivo, BORRARÁ SU CONTENIDO y añadirá aquel que escribamos
"""

with open("files/write_message.txt", "w") as file:
    file.write("Hello World!")

"""
Este código no tiene salida en la terminal, sin embargo, si accedemos a la ruta
especificada, veremos que se ha creado el archivo y se ha escrito en él 'Hello
Wolrd!'
"""



# ESCRIBIR MÚLTIPLES LÍNEAS

with open("files/write_message.txt", "w") as file:
    file.write("First line.")
    file.write("Second line.")
""" escribe en el archivo:
First line.Second line.

* Si queremos que escriba en diferentes líneas, debemos añadir manualmente el
'\n' al final del texto:
"""

with open("files/write_message.txt", "w") as file:
    file.write("First line.\n")
    file.write("Second line.\n")
""" escribe en el archivo:
First line.
Second line.

"""



# CONTINUAR ESCRIBIENDO / AÑADIR CONTENIDO -> "a" (append mode)

"""
Si no queremos eliminar el contenido de un archivo y queremos seguir añadiendo
más datos, debemos usar 'a' como segundo argumento de la función 'open()'
"""

with open("files/write_message.txt", "a") as file:
    file.write("This is a new line!\n")
""" si abrimos el archivo, veremos:
First line.
Second line.
This is a new line!

"""