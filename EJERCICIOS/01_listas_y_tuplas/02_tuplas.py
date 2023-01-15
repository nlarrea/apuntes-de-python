# 01 - BUFFET
print("\n\n01 - BUFFET\n")
"""
Un buffet ofrece únicamente 5 platos. Piensa en esos 5 platos y almacénalos en
una tupla.

- Usa el bucle for para imprimir cada una de las opciones.
- Intenta modificar alguno de los ítems.
- El restautante ha modificado dos de sus platos. Redefine la variable del menú
e imprime las nuevas opciones.
"""

foods = ("ensalada", "carne", "pescado", "arroz", "pasta")

print("Opciones de comida:")
for food in foods:
    print(food)

foods = ("hamburguesa", "carne", "pizza", "arroz", "pasta")
print("Nuevas opciones:")
for food in foods:
    print(food)
