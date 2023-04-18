# TRABAJAR CON EL CONTENIDO DE LOS ARCHIVOS

"""
Hasta ahora hemos visto cómo leer y almacenar el contenido de un archivo. Ahora
vamos a ver cómo trabajar con el contenido de dichos archivos. Podemos hacer lo
que queramos con dicho contenido.

Hay que tener en cuenta que al leer desde archivos, Python interpreta todo como
si fueran cadenas de texto. Esto significa que si leemos algún dato numérico y
queremos que se trate como tal, deberemos realizar el 'cambio de tipo string al
tipo numérico que queramos'.

Vamos con unos ejemplos.
"""

file_path = "files/pi_digits.txt"

with open(file_path) as file:
    lines = file.readlines()

pi_str = ""
for line in lines:
    pi_str += line.strip()      # .strip() -> para eliminar espacios

print(pi_str)                   # 3.141592653589793238462643383279
print(len(pi_str))              # 36



# estas líneas de código funcionan también con archivos de gran contenido
file_path = "files/pi_million_digits.txt"

with open(file_path) as file:
    lines = file.readlines()

pi_str = ""
for line in lines:
    pi_str += line.strip()

print(f"{pi_str[:52]}...")      # mostrar solo 52 dígitos
print(len(pi_str))              # 1000002



# DATO CURIOSO: ¿está tu fecha de nacimeinto en los decimales de pi?

bday = input("Enter your birthday (ddmmyy): ")

if bday in pi_str:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi...")