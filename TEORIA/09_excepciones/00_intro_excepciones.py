# INTRODUCCIÓN A LAS EXCEPCIONES

"""
En ocasiones se trabaja con datos o variables que han de cumplir ciertos
requisitos para que el programa funcione correctamente y no se detenga debido a
un error.

Para poder manejar dichos errores, existen las llamadas 'excepciones', objetos
que Python proporciona para evitar que el programa se detenga en caso de que
ocurra algún error y poder realizar algo específico en estos casos.

Comencemos con un ejemplo sencillo -> ZeroDivisionError: error que ocurre al
tratar de dividir cualquier número entre 0.
"""

""" COMENTADO PARA EVITAR ERRORES:
En este ejemplo, se le pide al usuario que introduzca dos números y divide el
primero por el segundo. ¿Qué pasaría si el segundo número fuera un 0?
¡Tendríamos un error y el programa quedaría detenido!

number_one = input('Enter a number: ')
number_two = input('Enter another number: ')

answer = int(number_one) / int(number_two)
"""



# TRY-EXCEPT -> cómo manejar errores

"""
La mejor forma de evitar que el programa se detenga debido a un error, es la de
utilizar bloques try-except.

TRY: aquí irá la parte del código que pueda dar algún error (cualquier entrada
de usuario, por ejemplo)

EXCEPT: si ha habido algún error al tratar de ejecutar el código contenido en
el bloque TRY, el programa 'avanza' automáticamente hasta este bloque y ejecuta
su contenido
"""

try:
    number_one = 5
    number_two = 0
    ans = number_one / number_two
    print(f"La respuesta de la división es: {ans}")
except ZeroDivisionError:
    print("No puedes dividir entre 0!")

print("Ahora se sigue ejecutando el programa")

""" lo que vemos por consola:
    No puedes dividir entre 0!
    Ahora se sigue ejecutando el programa

Como se produce un error en el bloque TRY, saltamos directamente al bloque de
EXCEPT, sin que termine de ejecutarse el bloque TRY.

Después el programa continúa como si nada ejecutando las siguientes líneas que
haya después del try-except
"""



# TRY-EXCEPT-ELSE

"""
Al bloque try-except se le puede añadir un bloque 'else' al final. Éste solo se
ejecutará en aquellas ocasiones en las que no se haya producido ningún error.
"""

try:
    number_one = 10
    number_two = 2
    ans = number_one / number_two
    print(f"El resultado de la división es: {ans}")
except ZeroDivisionError:
    print("No puedes dividir entre 0!")
else:
    print("Enhorabuena, no se han producido errores")

print("Aquí continúa el programa")

""" lo que se imprime en la consola:
    El resultado de la división es: 5.0
    Enhorabuena, no se han producido errores
    Aquí continúa el programa

Como no se han producido errores, se ejecuta también el código contenido en el
bloque ELSE.

Veamos qué ocurriría si se hubiera intentado dividir entre 0 esta vez:
"""

try:
    number_one = 10
    number_two = 0
    ans = number_one / number_two
    print(f"El resultado de la división es: {ans}")
except ZeroDivisionError:
    print("No puedes dividir entre 0!")
else:
    print("Enhorabuena, no se han producido errores")

print("Aquí continúa el programa")

""" se imprimiría lo siguiente:
    No puedes dividir entre 0!
    Aquí continúa el programa

Como se puede observar, no se termina de ejecutar el bloque TRY, se salta al
bloque EXCEPT y no se ejecuta el bloque ELSE
"""



# TRY-EXCEPT-FINALLY

"""
FINALLY: a diferencia del bloque ELSE, el bloque FINALLY se ejecuta SIEMPRE,
haya habido errores o no, después de terminar de ejecutarse el bloque TRY o el
bloque EXCEPT.
"""

try:
    number_one = 10
    number_two = 5
    ans = number_one / number_two
    print(f"El resultado de la división es: {ans}")
except ZeroDivisionError:
    print("No puedes dividir entre 0!")
else:
    print("Esto se imprime si no hay errores")
finally:
    print("Esto se muestra siempre")

print("Aquí continúa el programa")

""" se imprime:
    El resultado de la división es: 2.0
    Esto se imprime si no hay errores
    Esto se muestra siempre
    Aquí continúa el programa
"""

try:
    number_one = 10
    number_two = 0
    ans = number_one / number_two
    print(f"El resultado de la división es: {ans}")
except ZeroDivisionError:
    print("No puedes dividir entre 0!")
else:
    print("Esto se imprime si no hay errores")
finally:
    print("Esto se muestra siempre")

print("Aquí continúa el programa")

""" se imprime:
    No puedes dividir entre 0!
    Esto se muestra siempre
    Aquí continúa el programa
"""



# ELSE Y FINALLY

"""
Si se escribe un bloque TRY, el bloque EXCEPT es obligatorio, sin embargo, los
bloques ELSE y FINALLY son optativos, puede haber uno de ellos (cualquiera),
los dos, o ninguno.
"""