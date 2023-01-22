"""
Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase.
Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.
"""

peso = float(input("Introduce tu peso (kg): "))
altura = float(input("Introduce tu altura en metros (decimales con '.'): "))

imc = round(peso / pow(altura, 2), 2)

print(f"Tu IMC es: {imc}")