# ARGUMENTOS POR POSICIÓN

"""
estos son los argumentos más básicos y que hemos visto ya antes en el archivo
sobre cómo declarar funciones

como su nombre indica, al usar ARGUMENTOS POSICIONALES, éstos se deben pasar en
un orden predeterminado, es decir, que si la función tiene definidos 3
parámetros, a la hora de llamar a la función y pasarle los 3 argumentos, éstos
deben seguir el orden en el que se definieron en la función
"""

def print_user_information(username, email, followers):
    print(f"This is the information about '{username}'")
    print(f"\t- email: {email}")
    print(f"\t- followers: {followers}\n")


print_user_information("user123", "user123@example.com", 125)
""" se imprime lo siguiente:
This is the information about 'user123'
    - email: user123@example.com
    - followers: 125
"""

# hay que tener en cuenta el orden en el que se envían los argumentos
print_user_information("user123@example.com", 125, "user123")   # orden erróneo
""" se imprime lo siguiente:
This is the information about 'user123@example.com'
    - email: 125
    - followers: user123
"""

# si se envían menos argumentos que la cantidad de parámetros -> error
# print_user_information("my_username", 450)      # línea comentada para evitar el error
""" python muestra lo siguiente:
TypeError: print_user_information() missing 1 required positional argument: 'followers'

como podemos observar, nos está indicando que falta 1 argumento y, además, dice
que el argumento que falta es el de 'followers'. Esto lo dice porque ese es el
último parámetro de la función y nosotros hemos pasado 2
    1. username = 'my_username'
    2. email = 450      -> lo guardaría aquí aunque nos estuviéramos refiriendo
al parámetro de 'followers'
    3. followers = ?    -> le falta el valor del argumento -> devuelve un error
"""



# ARGUMENTOS CON VALORES POR DEFECTO

"""
se pueden utilizar parámetros con valores por defecto, por lo que si ocurriera
lo mismo que en el último ejemplo (falta de un argumento al realizar la llamada
a la función), no se generaría ningún error

el parámetro con valor por defecto debe ser el último de los definidos en la
función

pueden usarse varios argumentos por defecto, pero se debe tener siempre en
cuenta que al llamar a la función con menos argumentos que parámetros, éstos
comienzan ocupando las posiciones desde el inicio hacia el final. Es decir, que
si mi función tiene 3 parámetros y 2 de ellos tienen valores por defecto(los 2
últimos), 1 argumento será OBLIGATORIO (el primero). Si se envían 2 argumentos,
el tercero tendrá el valor por defecto y los demás el valor de los argumentos
envíados al realizar la llamada
VEÁMOSLO EN UN EJEMPLO
"""

def print_numbers(last_value, start_value=0, name="Default Counter"):
    print(f"This is '{name}'")
    for num in range(start_value, last_value+1):
        print(num)


print_numbers(25)
""" se imprime:
This is 'Default Counter':
0
1
2
...
25
"""

print_numbers(25, 10)
""" se imprime:
This is 'Default Counter':
10
11
12
...
25
"""

print_numbers(25, 10, "My Counter")
""" se imprime:
This is 'My Counter':
10
11
12
...
25
"""



# ARGUMENTOS CON NOMBRE

"""
esta es una forma de asegurarnos de que no enviamos por error un argumento al
parámetro que no queríamos

es una técnica recomendable cuando se utilizan más de dos argumentos en una
misma función
"""

def full_name(first_name, last_name):
    print(f"{first_name} {last_name}")


full_name("Naia", "Larrea")         # por posición -> se imprime: Naia Larrea
# es preferibla hacerlo así cuando hay más argumentos:
full_name(first_name="Naia", last_name="Larrea")    # Naia Larrea
full_name(last_name="Larrea", first_name="Naia")    # Naia Larrea



# DESEMPAQUETADO DE ARGUMENTOS ('UNPACKING')

"""
se utiliza '*' para decir que no conocemos la cantidad de argumentos que se van
a recibir, por tanto, guarda todos ellos en una variable de tipo tupla, después
podremos acceder a sus valores como si se tratara de una tupla normal

por convenio, a este tipo de argumento se le suele llamar 'args'

en este ejemplo, el primer argumento se guarda en 'time_of_day', y los demás,
sin importar cuántos sean, se guardarán en formato de tupla dentro de 'args'
"""

def greeting(time_of_day, *args):
    # print(args) # -> tupla con todos los argumentos que no sean el primero
    print(f"Hi {' '.join(args)}, I hope you're having a good {time_of_day}")


greeting("morning", "Naia")
# Hi Naia, I hope you're having a good monday
greeting("afternoon", "Naia", "Larrea")
# Hi Naia Larrea, I hope you're having a good monday



# KEYWORD ARGUMENTS

"""
este tipo de argumento es una combinación entre los argumentos de desempaquetar
y los de por nombre. Para escribirlo, basta con utilizar '**'

por convenio, a este tipo de argumento se le suele llamar 'kwargs'

lo que ocurre es que se indica el nombre del argumento en la llamada a la
función, y se guarda en el parámetro de la misma como un diccionario, donde el
nombre que se le haya puesto en la llamada, funciona como clave del diccionario
"""

def greet(**kwargs):
    if kwargs:
        print(f"Hi {kwargs['first_name']} {kwargs['last_name']}, have a great day!")
    else:
        print("Hi Guest, have a great day!")


greet(first_name = "Naia", last_name = "Larrea")
# Hi Naia Larrea, have a great day!

greet()
# Hi Guest, have a great day!

"""
tener en cuenta que si no se le pasan los argumentos con nombre 'first_name' y
'last_name', nos devolverá un KeyError, un error indicando el nombre de la
clave que nos falta por enviar a la función
"""



# FUNCIÓN QUE COMBINE TODOS LOS TIPOS DE ARGUMENTOS

def combined_greeting(time_of_day, *args, **kwargs):
    print(f"Hi {' '.join(args)}, I hope you're having a great {time_of_day}")

    if kwargs:
        print("\nYour tasks for the day are:")
        for key, val in kwargs.items():
            print(f"\t- {key} => {val}")


# llamada a la función
combined_greeting(
    "morning",                          # time_of_day -> porque está en primera posición
    "Naia", "Larrea",                   # *args -> coge todos los demás parámetros (que no tengan nombre)
    # estos argumentos tienen nombre, por lo que se recogen en **kwargs como diccionario:
    first = "Empty dishwasher",
    second = "Take pupper outside",
    third = "Math homework"
)

""" esta función imprime:
Hi Naia Larrea, I hope you're having a great morning

Your tasks for the day are:
    - first => Empty dishwasher
    - second => Take pupper outside
    - third => Math homework
"""