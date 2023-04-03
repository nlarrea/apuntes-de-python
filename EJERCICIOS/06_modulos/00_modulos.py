print("01 - IMPRIMIR MODELOS\n")
"""
Importe las funciones del archivo 'printing_modules.py' y úselas.
"""

# importing all the functions
from printing_models import *

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# calling functions -> we can use them w/o the dot
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)



print("\n\n02 - FUNCIONES MATEMÁTICAS\n")
"""
Importa las funciones necesarias del archivo 'math_functions.py' para realizar
los siguientes cálculos e imprimir su resultado formateado:
    8 + 10
    23 - 4
    5 * 6
"""

from math_functions import sum_values, subtrack_values, multiply_values

sum_values(8, 10)               # 8 + 10 = 18
subtrack_values(23, 4)          # 23 - 4 = 19
multiply_values(5, 6)           # 5 * 6 = 30