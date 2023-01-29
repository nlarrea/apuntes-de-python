# CONDICIONES SIMPLES
# SENTENDIAS 'if'

""" RECORDATORIO DE OPERADORES
para utilizar condicionales es imprescindible que sepamos cómo utilizar los
operadores COMPARATIVOS y LÓGICOS que vimos en apartados anteriores:
    igualdad              ==
    desigualdad           !=
    mayor que             >
    menor que             <
    mayor o igual que     >=
    menor o igual que     <=

    and
    or
    not
"""

""" SINTAXIS
si queremos realizar una acción cuando ocurra algo específico, ese ALGO será la
condición que se ha de cumplir en nuestra sentencia 'if':

if condition:
    some_code

"""

if 4 > 3:
    print("4 is more than 3")           # se imprime porque 4 es mayor que 3

if "Hello" == "hello":
    print("They are equals!")           # NO se imprime porque Python es case-sensitive


# se pueden utilizar variables dentro de las condiciones
age = 24

if age >= 18:
    print("You are an adult")           # se imprime porque 24 es mayor o igual que 18

""" VARIABLES DE TIPO BOOL
tener en cuenta que si alguna variable es un dato de tipo boolean (True o False)
no es necesario escribir ninguna comparación y basta con escribir el nombre de
la variable

no hacer:
    if boolean_variable == True:
        some_code

sí hacer:
    if boolean_variable:
        some_code
"""


# se puede dar que un único 'if' tenga más de una condición a tener en cuenta

""" OR
en este primer ejemplo, se utiliza el operador lógico OR, lo que significa que
si una de las dos condiciones se cumple, se ejecuta el código de dentro de la
sentencia 'if'
"""

have_studied_hard = True
exam_difficulty = "high"

if have_studied_hard or exam_difficulty == "low":
    print("You will pass the exam!")            # se imprime porque la primera condición se cumple

""" AND
en este caso, todas las condiciones de la sentencia 'if' deberán cumplirse para
que se ejecute el código dentro del mismo
"""

door = "closed"
took_keys = False

if not took_keys and door == "closed":
    print("You will not be able to get in")
    # se imprime porque no has cogido llaves y la puerta está cerrada

""" NOT
puede utilizarse tal y como está, o introducir entre paréntesis la variable de tipo
bool para que se lea mejor el código:

if not(boolean_variable):
    some_code
"""



# SENTENCIA 'else'
"""
en ocasiones se desea realizar una acción si se cumple una condición, y otra acción
distinta en todos los demás casos. Para estas situaciones está el 'else', que
se ejecutará siempre que la condición del 'if' al que acompaña no se cumpla

tener en cuenta que siempre que en una condición haya un 'else', debe tener un
'if' delante, pero que los 'else' son opcionales, no tienen por qué ser usados

SINTAXIS:
if condition:
    some_code
else:
    other_code
"""

have_studied_hard = False
exam_difficulty = "high"

if have_studied_hard or exam_difficulty == "low":
    print("You will pass the exam!")
else:
    print("You should study more...")       # se imprime
    # se ejecuta este código porque ninguna de las condiciones del 'if' se cumplen



# CONDICIONES MÚLTIPLES
# SENTENCIAS 'elif'
"""
habrá ocasiones en las que no sólo se desee ejecutar un código bajo una condición
y otro código si ésta no se cumple, sino que se podrían querer realizar otras
comprobaciones adicionales. Para eso existen las sentencias 'elif'
"""

sex = "female"

if sex == "female":
    print("You are a woman")
elif sex == "male":
    print("You are a man")
else:
    print("You are neither a man nor a woman")

"""
se pueden escribir tantas sentencias 'elif' como se deseen, pero éstas deben estas
precedidas por una única sentencia 'if'
"""



# DIFERENCIA ENTRE USAR VARIOS 'elif' O VARIOS 'if'
"""
si se utiliza un 'if' y varias sentencias 'elif', de todas las condiciones solo
se tendrá en cuenta aquella que sea verdadera primero. Si se tienen dos o más
condiciones verdaderas, la situada más arriba en el código será la que se
ejecute

si se utilizan varios 'if', da igual la posición en la que estén las condiciones,
si se cumplen, se ejecutan tantas como sean verdaderas
"""

""" VARIAS SENTENCIAS 'elif'
en este primer ejemplo, a pesar de 'age' ser menor que 18 y también de 26, la
primera condición en cumplirse es la que se ejecuta, y las demás son ignoradas
"""

age = 12

if age < 4:
    cost = 0
elif age < 18:  # sí se cumple
    cost = 15   # sí se ejecuta
elif age < 26:  # sí se cumple, pero se ignora
    cost = 20   # no se ejecuta
else:
    cost = 30

print(f"Your admission cost is {cost}€")    # Your admission cost is 15€


""" VARIAS SENTENCIAS 'if'
en este caso, si dos o más condiciones se cumplen, todas ellas serán ejecutadas
independientemente de en qué posición u orden se encuentren
"""

use_numbers = True
use_symbols = False
use_capital = True

if use_numbers:
    print("The password has numbers")           # The password has numbers
if use_symbols:
    print("The password has symbols")           # NO se imprime porque la condición no se cumple
if use_capital:
    print("The password has capital letters")   # The password has capital letters



# OMITIR LA SENTENCIA 'else'
"""
cuando se desea comprobar que cierta variable está entre cierto rango de valores,
es más conveniente crear ina condición 'elif' adicional que cubra los valores no
definidos por las sentencias anteriores, antes que dejar a una sentencia 'else'
encargarse de los mismos

esto se debe a que no se desea admitir CUALQUIER tipo de valor, sino que se busca
que esté dentro de un valor concreto, para ello es mejor omitir el 'else' y usar
otro 'elif'. Posteriormente, podría usarse un 'else' para recoger CUALQUIER otro
tipo de valor y realizar una acción con ello (evidentemente, esto es opcional)
"""

age = 12

if age < 4:
    cost = 0
elif age < 18:
    cost = 15
elif age < 65:
    cost = 30
elif age >= 65:
    cost = 20

"""
si la variable 'age' tuviera un valor de tipo String (por ejemplo) no entraría
en ninguna de las sentencias, y ese dato no sería tratado como si 'cost = 20',
algo que sí ocurriría si la última sentencia fuera 'else'
"""
