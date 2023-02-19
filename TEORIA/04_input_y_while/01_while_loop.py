# BUCLE WHILE

# se repite mientras se cumpla una determinada condición

index = 1
while index <= 5:
    print(index)
    index += 1
    """ se imprime:
    1
    2
    3
    4
    5
    """

# el bucle se repite mientras el valor de 'index' siga siendo menor o igual a 5



# PERMITIR AL USUARIO DETENER EL BUCLE

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != "quit":
    message = input(prompt)
    
    if message != "quit":
        print(message)
    
    """ se imprime:
    Tell me something and I will repeat it back to you:
    Enter 'quit' to end the program. Hi
    Hi

    Tell me something and I will repeat it back to you:
    Enter 'quit' to end the program. Hello
    Hello
    
    Tell me something and I will repeat it back to you:
    Enter 'quit' to end the program. 234
    234

    Tell me something and I will repeat it back to you:
    Enter 'quit' to end the program. quit
    """



""" FLAGS
cuando el salir de un bucle depende de varias condiciones, lo mejor es utilizar
'flags' -> crear una variable que indique si el programa debe continuar o no
"""

# repitiendo el ejemplo anterior:

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)
    
    if message == "quit":
        active = False
    else:
        print(message)

# el programa funciona igual que antes, pero ahora usando 'active' como flag



# BREAK

"""
cuando se quiere salir inmediátamente del bucle sin que se ejecute nada más en
su interior, se utiliza la keyword 'break'
"""

prompt = "\nEnter the name of a city you've visited."
prompt += "\n(enter 'quit' when finished): "

while True:
    city = input(prompt)

    if city == 'quit':
        break           # sale directamente del bucle
    else:
        print(f"{city} is an awesome city!")



# CONTINUE

"""
se usa 'continue' cuando queremos volver al comienzo del bucle manteniendo la
condición como estaba en el caso de los bucles 'while', o avanzando al siguiente
en los bucles 'for'
"""

current = 0

while current < 10:
    # actualizar variable
    # si estuviera al final, crearíamos un bucle infinito!
    current += 1        

    if current % 2 == 0:
        continue

    print(current)      # si se cumple el 'if', esto no se ejecuta

    """ se imprime:
    1
    3
    5
    7
    9
    """