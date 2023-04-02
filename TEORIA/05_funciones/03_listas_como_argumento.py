# MODIFICACIÓN DE LAS LISTAS DENTRO DE LAS FUNCIONES

"""
Al trabajar con listas, es importante saber que si se pasa una lista a una
función como parámetro y ésta es modificada dentro de dicha función, la modifi-
cación es permanente, lo que significa que la lista original también se ve
afectada por el cambio realizado.
"""

def print_models(unprinted_designs, completed_models):
    # simulación de impresión de modelos
    while unprinted_designs:
        # elimina de una lista y lo asigna a variable
        current_design = unprinted_designs.pop()
        # imprime la variable
        print(f"Printing model: {current_design}")
        # la añade a otra lista
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")

    for completed_model in completed_models:
        print(f"\t- {completed_model}")


# creación de listas inicial
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# llamadas a las funciones
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

""" se imprime:
Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
    - dodecahedron
    - robot pendant
    - phone case    
"""

# ahora, el valor de las listas se ha visto modificado:
print(unprinted_designs)    # []
print(completed_models)     # ['dodecahedron', 'robot pendant', 'phone case']



# PASAR LISTAS A LAS FUNCIONES SIN MODIFICAR LA ORIGINAL

"""
Si en este ejemplo hubiéramos querido guardar el valor original de la lista de
elementos impresos, deberíamos haber pasado a la función una copia de la lista.
Los elementos dentro de la función se habrían movido de una lista a otra igual-
mente, sin embargo, la lista original fuera de la función permanecería intacta.

Para pasar copias de listas, es tan sencillo como usar la notación de 'slice':
    function_name(list_name[:])
"""

# manteniendo las funciones del ejemplo anterior:

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

""" se imprime lo mismo que antes:
Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
    - dodecahedron
    - robot pendant
    - phone case
"""

# la lista de 'unprinted_designs' no se ha visto alterada:
print(unprinted_designs)    # ['phone case', 'robot pendant', 'dodecahedron']
print(completed_models)     # ['dodecahedron', 'robot pendant', 'phone case']