print("01 - PRUEBAS CONDICIONALES\n")
"""
Escribe una serie de pruebas condicionales. Imprime una frase describiendo cada
prueba y su predicción para el resultado. Con 3 pruebas basta.
"""

fav_number = 11

print("Is your favorite number 11? I predict true.")
print(fav_number == 11)

print("Is your favorite number 7? I predict true.")
print(fav_number == 7)

print("Is your favorite number 5? I predict true.")
print(fav_number == 5)



print("\n\n02 - COLORES DE ALIENS 1\n")
"""
Imagina que estás jugando a los marcianitos. Se ha disparado a un alien y deben
mostrarse los puntos obtenidos. El color del alien puede ser 'green', 'yellow',
o 'red'.
Crea un programa en el que se asigne el color verde al alien y se muestre que
se han obtenido 5 puntos si el alien era de color verde.
"""

color_alien = "green"

if color_alien == "green":
    print("5 points!")



print("\n\n03 - COLORES DE ALIENS 2\n")
"""
Partiendo del ejercicio anterior, escribe una sentencia 'if-else':

- Si el color del alien es verde, imprime que se han conseguido 5 puntos.
- Si el color del alien no es verde, imprime que se han conseguido 10 puntos.
"""

color_alien = "yellow"

if color_alien == "green":
    print("5 points!")
else:
    print("10 points!")



print("\n\n04 - COLORES DE ALIENS 3\n")
"""
Partiendo del ejercicio anterior, escribe una sentencia 'if-elif-else':

- Si el color del alien es verde, imprime que se han conseguido 5 puntos.
- Si el color del alien es amarillo, imprime que se han conseguido 10 puntos.
- Si el color del alien es rojo, imprime que se han conseguido 15 puntos.
"""

color_alien = "red"

if color_alien == "green":
    points = 5
elif color_alien == "yellow":
    points = 10
elif color_alien == "red":      # es más seguro usar otro elif que un else
    points = 15

print(f"{points} points!")



print("\n\n05 - ETAPAS VITALES\n")
"""
Escribe un programa con sentencias 'if-elif-else' para determinar la etapa vital
de una persona. Atribuye un valor a la variable 'age' y:

- Si la persona tiene menos de 2 años, imprime un mensaje que diga que esta en
el rango de 'baby'.
- Si la persona tiene al menos 2 años y es menor de 13, imprime un mensaje que
diga que es 'kid'.
- Si la persona tiene al menos 13 años y es menor de 20, imprime que esta en el
rango de 'teenager'.
- Si la persona tiene al menos 20 años y es menor de 65, imprime que esa persona
es 'adult'.
- Si la persona tiene al menos 65 años, imprime que es 'elder'.
"""

age = 24

if age < 2:
    stage = "baby"
elif age >= 2 and age < 13:
    stage = "kid"
elif age >= 13 and age < 20:
    stage = "teenager"
elif age >= 20 and age < 65:
    stage = "adult"
elif age >= 65:
    stage = "elder"

print(f"This person is a/an {stage}")