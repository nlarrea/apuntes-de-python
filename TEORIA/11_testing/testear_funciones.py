# TESTEAR FUNCIONES

def get_formated_name(first, last, middle=""):
    """ Generate a neatly formated full name """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


# comprobamos que la función devuelve el nombre completo de forma correcta
""" comentado para que no se ejecute al lanzar el test
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nEnter your first name: ")
    if first == "q": break

    last = input("Enter your last name: ")
    if last == "q": break

    formatted_name = get_formated_name(first, last)
    print(f"\nFormatted name: {formatted_name}")
"""