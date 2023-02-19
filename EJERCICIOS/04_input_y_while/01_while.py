print("01 - INGREDIENTES DE LA PIZZA\n")
"""
Crea un programa que pida 'toppings' de la pizza al usuario hasta que éste
escriba 'quit'. Por cada topping añadido, muestra un mensaje que indique que se
ha añadido a la pizza.
"""

while True:
    topping = input("Enter a topping (write 'quit' to exit): ")

    if topping == "quit":
        break
    else:
        print(f"{topping} added to your pizza!")



print("\n\n02 - ENTRADA DE CINE\n")
"""
La entrada del cine tiene un precio diferente en base a la edad del usuario:
- Si una persona tiene menos de 3 años, la entrada es gratuita.
- Si la persona tiene entre 3 y 12, la entrada cuesta 10 euros.
- Si la persona tiene más de 12, la entrada cuesta 15 euros.
Crea un bucle con el que preguntes la edad a la gente e imprime el coste de la
entrada de cada persona
"""

prompt = "Enter your age (write 'quit' to exit): "

while True:
    age = input(prompt)

    if age == "quit":
        break
    elif not age.isnumeric():
        print("You must enter an INTEGER NUMBER or 'quit'!")
        continue
    elif int(age) < 3:
        cost = 0
    elif int(age) >= 3 and int(age) <= 12:
        cost = 10
    elif int(age) > 12:
        cost = 15
    
    print(f"Your ticket costs {cost} euros.")