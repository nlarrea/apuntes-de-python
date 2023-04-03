# MÓDULOS

"""
Usar módulos es una forma muy útil de mantener el código principal limpio y más
legible, además de permitir compartir funciones con otros programadores sin la
necesidad de compartir el código al que no quieras que otros tengan acceso.

Pero primero: QUÉ ES UN MÓDULO?
Un módulo es un archivo (.py) que contiene el código que deseas importar a tu
programa.
"""

# IMPORTAR UN MÓDULO ENTERO

"""
para importar un módulo entero vamos a seguir esta sintaxis:

    import module.name

después, para usar alguna de sus funciones:

    module_name.function_name()

    
Vamos a crear un archivo llamado 'pizza.py' para explicar esto, y vamos a crear
la función 'make_pizza()' en él.
"""

import pizza

pizza.make_pizza(16, "pepperoni")
""" imprime:
Making a 16-inch pizza with the following toppings:
 - pepperoni
"""

pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")
""" imprime:
Making a 12-inch pizza with the following toppings:
 - mushrooms
 - green peppers
 - extra cheese
"""



# IMPORTAR EL MÓDULO ENTERO SIN LA NOTACIÓN CON PUNTO

"""
Si se van a importar todas las funciones, se puede usar la siguiente sintaxis
para importarlas todas y hacerlas accesibles SIN la necesidad de usar el nombre
del módulo seguido de un punto para acceder a éstas. Esta es la sintaxis:

    from module_name import *

con el '*' indicamos que queremos importarlo todo
"""

from pizza import *

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# se obtiene el mismo resultado que el visto en el ejemplo anterior



# IMPORTAR FUNCIONES ESPECÍFICAS

"""
se pueden importar solo las funciones deseadas desde un módulo siguiendo la
siguiente sintaxis:

    from module_name import function_name       # para importar 1 función

o bien, para importar varias funciones:

    from module_name import function_0, function_1, function_2

La ventaja más evidente de esta sintaxis es la de poder importar solo algunas
funciones envez de todas. Además, no será necesario usar la notación del punto
cuando se utilicen dichas funciones
"""

# estas líneas dan como resultado lo mismo que hemos visto antes:

from pizza import make_pizza

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")



# USAR UN ALIAS EN LAS FUNCIONES

"""
En ocasiones, la función que se desea importar puede generar conflictos con
alguna función del programa, o puede que tenga un nombre muy largo y querramos
hacerlo más corto.

En estos casos, se puede utilizar un alias para la función siguiendo la
siguiente sintaxis:

    from module_name import function_name as new_name
"""

from pizza import make_pizza as mp

mp(16, "pepperoni")
mp(12, "mushrooms", "green peppers", "extra cheese")

# se obtienen los mismos resultados que en los casos anteriores



# USAR ALIAS EN EL MÓDULO

"""
Principalmente se usa para acortar el nombre del módulo a la hora de llamarlo
haciendo uso de la notación con punto. Esta es su sintaxis:

    import module_name as mn
"""

import pizza as p

p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# de nuevo, se obtiene el mismo resultado que el ya visto anteriormente