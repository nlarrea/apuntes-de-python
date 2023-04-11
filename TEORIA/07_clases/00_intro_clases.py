# INTRODUCCIÓN A LAS CLASES

""" INTRODUCCIÓN
La Programación Orientada a Objetos es una de las formas más efectivas de
escribir software. Se crean clases, las cuales pueden entenderse como una
especie de 'plantillas', y a partir de éstas se crean objetos.

Las clases tienen los conceptos generales, que son aplicables a varios objetos,
después cada uno de los objetos que se haya creado a partir de dicha clase
tendrá sus propias características.

Crear un objeto a partir de una clase se denomina 'instanciar', por lo que el
objeto en cuestión, es una 'instancia' de la clase.
"""



# CREAR UNA CLASE

"""
Se crea una clase utilizando la palabra reservada 'class'

Las buenas prácticas de Python dicen que el nombre de la clase debe comenzar
con la primera letra en mayúscula.
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        # simulate a dog sitting in response to a command
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        # simulate a dog rolling over in response to a command
        print(f"{self.name} rolled over!")



""" __init__()
Este es un método especial que Python ejecuta automáticamente cada vez que se
crea una nueva instancia de la clase a la que pertenece.

El parámetro 'self' dentro de este método es obligatorio, y debe aparecer en la
primera posición dentro del paréntesis de argumentos al definir __init__().
Debe incluirse en la definición porque cada vez que se cree una nueva instancia
de esta clase, la llamada usa 'self' de forma automática, que es una referencia
a la propia instancia.

En el ejemplo se pasan también los parámetros 'name' y 'age', por lo que cada
vez que creemos una instancia de esta clase, debemos añadir estos dos valores.

Éstas dos se definen con un 'self' delante dentro del método, esto significa
que cada instancia tendrá su propio 'name' y 'age'.
"""

""" MÉTODOS
La clase que hemos creado tiene 2 métodos que hemos creado: 'sit' y 'roll_over'

Estos dos métodos, en este ejemplo, solo sirven como simulación, así que se les
pasa únicamente el valor de 'self' para que tengan acceso a los atributos
propios de cada una de las instancias
"""



# CREAR INSTANCIAS DE UNA CLASE

my_dog = Dog('Lagun', 4)        # nueva instancia de Dog
your_dog = Dog('Atom', 6)       # otra instancia de Dog



# ACCESO A LOS ATRIBUTOS Y MÉTODOS

"""
Hemos dicho que las instancias son, en definitiva, objetos, por lo que se puede
acceder a los valores (atributos y métodos) usando un punto
"""

print(f"My dog's name is {my_dog.name}")
# My dog's name is Lagun

print(f"Your dog's name is {your_dog.name} and it's {your_dog.age} years old")
# Your dog's name is Atom and it's 6 years old


my_dog.sit()                    # Lagun is now sitting
your_dog.roll_over()            # Atom rolled over!