# FUNCIONES

""" PARA QUÉ SIRVEN
- tenemos un input
- la función realiza lo que tenga que hacer
- obtenemos un output

este proceso puede ser llamado después desde cualquier parte del programa, lo
que evita que tengamos código repetido varias veces

SINTAXIS -> función que recibe argumentos (inputs) y devuelve datos (outputs):

def function_name(inputs):
    return output

recibir y devolver datos es algo opcional, pero es lo más común

por convenio, en Python se dejan dos líneas en blanco después de la definición
de una función hasta la siguiente línea de código
"""

# FUNCIÓN SIN RECIBIR NI DEVOLVER DATOS

# definición de la función
def greeting():
    print("Hello world!")


# llamada a la función -> OBLIGATORIO para que se ejecute
greeting()              # Hello World!


# otro ejemplo
def print_hundred():
    for num in range(1, 101):
        print(num)


print_hundred()         # imprime los números del 1 al 100 (incluidos)



# FUNCIÓN QUE RECIBE DATOS PERO NO DEVUELVE NINGUNO
def greet_user(name):
    print(f"Hello {name.title()}!")


greet_user("Naia")      # Hello Naia!


# otro ejemplo
def auth(email, password):
    if email == "youremail@example.com" and password == "123456":
        print("You are authorized!")
    else:
        print("Sorry! You are not authorized...")


auth("youremail@example.com", "123456")         # You are authorized
auth("youremail@example.com", "123456789")      # Sorry! You are not authorized...
auth("notcorrect@email.com", "sfsefsfd")        # Sorry! You are not authorized...



# FUNCIÓN QUE RECIBE Y DEVUELVE DATOS
def return_full_name(first, last):
    return f"{first} {last}"                    # devuelve el nombre completo


def greet_somebody(name):
    print(f"Hi {name}!")                        # imprime el saludo


full_name = return_full_name("Naia", "Larrea")  # full_name = "Naia Larrea"
greet_somebody(full_name)                       # Hi Naia Larrea!



# FUNCIONES ANIDADAS ('NESTED FUNCTIONS')
""" CUÁNDO USAR NESTED FUNCTIONS?
si creas un programa con una función que va a tener que ser llamada en algún
otro momento a lo largo del programa, es mejor no usar nested functions

si solo vas a usar esa función para que sea llamada desde una única función,
entonces sí debería ser una nested function (como en el ejemplo)

SIGUIENDO EL EJEMPLO ANTERIOR, probablemente solo queramos usar la función que
devuelva el nombre completo para el saludo a esa persona, por ello, podemos
meter esa función dentro de la otra y llamarla desde ahí

la función 'hija', la que está dentro, puede acceder a las variables de la
función en la que se encuentra
"""

# definición de la función 'madre'
def nested_greeting(first, last):
    # definición de la función 'hija'
    def nested_full_name():
        return f"{first} {last}"
    
    # imprime el saludo llamando a la función hija para obtener el 'full name'
    print(f"Hi {nested_full_name()}!")


nested_greeting("Naia", "Larrea")      # Hi Naia Larrea!