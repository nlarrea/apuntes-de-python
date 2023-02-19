print("01 - ALQUILER DE COCHES\n")
"""
Escribe un programa que poda al usuario qué tipo de coche les gustaría alquilar
e imprime un mensaje como 'Let me see if I can find you a Subaru.'
"""

car_type = input("Enter the car you want: ")

print(f"Let me see if I can find you a {car_type}.")



print("\n\n02 - MESA EN UN RESTAURANTE\n")
"""
Pide al usuario cuántas personas van a asistir a la cena de grupo. Si la
respuesta es más de 8, escribe un mensaje que diga que deberán esperar para una
mesa. De lo contrario, imprime que disponen de una ya.
"""

people_number = input("Enter how may people are having the dinner: ")
people_number = int(people_number)

if people_number > 8:
    print("You will have to wait until the table is ready.")
else:
    print("Your table is ready for dinner.")



print("\n\n03 - MÚLTIPLO DE 10\n")
"""
pide un número al usuario y escribe si ese número es múltiplo de 10 o no
"""

number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is a multiple of 10!")
else:
    print(f"The number {number} is not a multiple of 10...")