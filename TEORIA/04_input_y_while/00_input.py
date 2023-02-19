# ENTRADA DE USUARIO

"""
para introducir datos de usuario, Python cuenta con la función input()

lo que hace esta función es pausar el programa y esperar a que el usuario
introduzca algún valor

si guardamos el dato introducido en una variable, éste será guardado como tipo
de dato string, es decir, texto
"""

message = input("Tell me something and I will repeat it to you: ")
print(message)



# PARÁMETRO DE LA FUNCIÓN

"""
input() toma un parámetro -> un mensaje a mostrar => prompt

debemos asegurarnos siempre de que ese mensaje sea lo más claro posible
"""

name = input("Enter your name: ")
print(f"Hello {name}\n")



# mensaje de más de una línea en el prompt

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello {name}\n")


# otra forma de hacer lo mismo:

prompt = """
If you tell us who you are, we can personalize the messages you see.
What is your first name?
"""

# usamos .lstrip() para que quite el \n que se genera antes del prompt
name = input(prompt.lstrip())
print(f"Hello {name}\n")



# RECOGER DATOS NUMÉRICOS -> int()

age = input("Enter your age: ")
print(type(age))    # string

age = int(age)      # contertimos el str a tipo int
print(type(age))    # int

# ahora podemos usar la variable 'age' para cualquier cosa que requiera números
print(age >= 18)    # como age es tipo int, ya no daría error



# SABER SI UN NÚMERO INTRODUCIDO ES PAR O IMPAR -> %

number = input("Enter a number, I'll tell you if it is even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")
