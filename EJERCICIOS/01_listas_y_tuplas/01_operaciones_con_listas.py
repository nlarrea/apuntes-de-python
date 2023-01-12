# 01 - PIZZAS
print("01 - PIZZAS\n")
"""
Piensa al menos 3 tipos de pizza que te gusten y guarda sus nombres en una lista.

- Modifica tu bucle for para imprimir una sentencia usando el nombre de cada pizza.
Por ejemplo, imprime: 'I like pepperoni pizza'.
- Al final del programa, escribe 'I really love pizza!' para que se muestre una
sola vez después de acabar el bucle.
"""

pizzas = ["pepperoni", "cheese", "BBQ chicken"]

for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I really love pizza!")



# 02 - CONTANDO HASTA 20
print("\n\n02 - CONTANDO HASTA 20\n")
"""
Usa un bucle para imprimir los números del 1 al 20, ambos incluidos.
"""

for number in range(1, 21):
    print(number)



# 03 - CIÉN
print("\n\n03 - CIÉN\n")
"""
Crea una lista que contenga los números del 1 al 100 e imprime la lista usando un bucle.
"""

hundred_numbers = [value for value in range(1, 101)]

for number in hundred_numbers:
    print(number)



# 04 - SUMAR 100
print("\n\n04 - SUMAR 100\n")
"""
Crea una lista con los números del 1 al 100. Utiliza las funciones min(), max() y sum().
"""

hundred_numbers = [value for value in range(1, 101)]

print(min(hundred_numbers))
print(max(hundred_numbers))
print(sum(hundred_numbers))



# 05 - NÚMEROS IMPARES
print("\n\n05 - NÚMEROS IMPARES\n")
"""
Usa el tercer argumento de range() para crear una lista con todos los números impares del
1 al 20. Usa un bucle for para imprimirlos.
"""

odd_numbers = [value for value in range(1, 20, 2)]

for number in odd_numbers:
    print(number)



# 06 - TRESES
print("\n\n06 - TRESES\n")
"""
Crea una lista con los múltiplos de 3 desde el 3 al 30. Usa un bucle for para imprimirlos.
"""

threes = [value for value in range(3, 30, 3)]

for number in threes:
    print(number)



# 07 - CUBOS
print("\n\n07 - CUBOS\n")
"""
Un número elevado a la tercera potencia es un cubo. Crea una lista con los primeros 10
cubos e impríme los valores con un bucle for.
"""

cubes = [value**3 for value in range(1, 11)]

for number in cubes:
    print(number)



# 08 - MIS PIZZAS, TUS PIZZAS
print("\n\n08 - MIS PIZZAS, TUS PIZZAS\n")
"""
Con la lista de pizzas creada en el primer ejercicio, crea una copia llamada "friend_pizzas".

- Añade una pizza nueva a tu lista.
- Añade una pizza diferente a la lista de tu amigo.
- Demuestra que tienes dos listas diferentes. Escribe "My favorite pizzas are:", muestra tu
lista con un bucle for y, después, escribe otro mensaje "My friend's favorite pizzas are:"
y muestra las contenidas en la otra lista.
"""

my_pizzas = ["pepperoni", "cheese", "BBQ chicken"]
friend_pizzas = my_pizzas.copy()    # es lo mismo que hacer: fiend_pizzas = my_pizzas[:]

my_pizzas.append("meat")
friend_pizzas.append("veggie")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"\t{pizza}")

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t{pizza}")