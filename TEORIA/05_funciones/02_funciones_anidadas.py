# FUNCIONES ANIDADAS = una función dentro de otra

def greeting(first_name, last_name):
    def full_name():
        return f"{first_name} {last_name}"
    
    print(f"Hello {full_name()}!")


greeting("Naia", "Larrea")          # Hello Naia Larrea!

"""
la función 'full_name()' se encuentra dentro de la función 'greeting()', por lo
que tiene acceso directo a las variables de la función en la que se encuentra y
no necesita que éstas sean pasadas como parámetros al llamar a la función
"""


""" CUÁNDO USAR ESTE TIPO DE FUNCIONES?
si creas un programa con una función que va a tener que ser llamada en algún
otro momento a lo largo del programa, es mejor no usar funciones anidadas

si solo vas a usar esa función para que sea llamada desde una única función,
entonces sí debería ser una función anidada (como en el ejemplo)
"""