# JSON

"""
En varias ocasiones se deseará almacenar cualquier tipo de información de tal
forma que la próxima vez que abran la aplicación en cuestión, se mantenga dicha
información o ajustes que realizaron previamente.

Para esto, existen los archivos con formato JSON. Este formato no es único de
Python, sino que puede ser utilizado en múltiples lenguajes de programación. Lo
que lo hace un formato muy útil y portable.
"""



# ALMACENAR DATOS -> json.dump()

""" json.dump()
Sirve para guardar o almacenar datos.

Toma 2 argumentos -> los datos a guardar y un 'file object'.

Vamos a crear un programa para almacenar una serie de números:
"""

import json     # importamos el módulo necesario

numbers = [5, 12, 7, 10, 9, 17]
filename = "./files/numbers.json"

with open(filename, "w") as f:
    json.dump(numbers, f)

""" 
Si accedemos al directorio indicado, veremos que tenemos un archivo llamado
'numbers.json', donde se encuentra almacenada la lista de números que acabamos
de definir en dicha variable.
"""



# LEER DATOS -> json.load()

""" 
Ahora vamos a leer de vuelta los datos escritos anteriormente en el archivo y a
mostrarlos por pantalla:
"""

with open(filename) as f:
    read_numbers = json.load(f)

print(numbers)      # [5, 12, 7, 10, 9, 17]



# GUARDAR Y LEER DATOS GENERADOS POR EL USUARIO

"""
Utilizar datos con JSON es muy útil cuando se trabaja con entradas de usuario,
puesto que nos permite, de alguna manera, 'recordar' cuál es ese dato o esa
configuración que ha hecho el usuario.'

Vamos con un ejemplo en el que el usuario almacena sus datos, a continuación,
leeremos el archivo para que el programa recuerde cuáles son los datos que ha
introducido el usuario.
"""

user_name = input("Enter your name: ")          # Enter your name: Naia
filename = "./files/user_name.json"

with open(filename, "w") as f:
    json.dump(user_name, f)

""" Ahora, vamos a crear otro caso 'greet user', donde vamos a
acceder a la información que acaba de dar el usuario para saludarlo sin tener
que pedirle de nuevo su nombre.

Veremos que al ejecutar ese código, directamente se saluda al usuario con el
nombre que se haya introducido en este archivo previamente """

"""
Podemos generar un código de tal forma que si existe el usuario, lo salude, y
si el usuario aún no ha sido introducido, pregunte por su nombre. Para esto, se
va a hacer uso de los conocimientos adquiridos en el tema anterior:
"""

filename = "./files/remember_user.json"

try:
    with open(filename) as f:
        user_name = json.load(f)
except FileNotFoundError:
    user_name = input("Enter your name: ")      # Enter your name: Cris
    with open(filename, "w") as f:
        json.dump(user_name, f)
        print("We will remember your name next time!")
else:
    print(f"Welcome back {user_name}!")

""" Si ejecutamos el código una vez (le primera), nos pedirá que introduzcamos
el nombre, pero las próximas veces, nos saludará con el mensaje 'Welcome back'
seguido del nombre introducido """