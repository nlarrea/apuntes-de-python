# 01 - NOMBRES
print("01 - NOMBRES\n")
"""
Almacena los nombres de algunos amigos tuyos en una lista llamada names.
Imprime el nombre de cada persona accediendo uno a uno a cada elemento.
"""

names = ["Cristina", "June", "Clara"]

print(names[0])
print(names[1])
print(names[2])

print("\n\n")



# 02 - AGRADECIMIENTOS
print("02 - AGRADECIMIENTOS\n")
"""
Usando la lista del apartado anterior, imprime un mensaje para cada una de
las personas de la lista, mostrando su nombre.
"""

print(f"{names[0]}, I miss you so much!")
print(f"{names[1]} is my sister")
print(f"{names[2]}, I can't wait to see you again!")

print("\n\n")



# 03 - TU LISTA PERSONALIZADA
print("03 - TU LISTA PERSONALIZADA")
"""
Piensa en tu medio de transporte favorito, como una moto o un coche, y haz una lista
en la que guardes varios ejemplos. Utiliza tu lista para imprimir una serie de
afirmaciones sobre estos artículos, como "Me gustaría tener una moto Honda".
"""

my_list = ["train", "car", "plane"]

print(f"I use the {my_list[0]} almost every day")
print(f"I would like to buy a new {my_list[1]}")
print(f"I take a {my_list[2]} once every two months!")

print("\n\n")



# 04 - LISTA DE INVITADOS
print("04 - LISTA DE INVITADOS\n")
"""
Si pudieras invitar a cualquiera a una cena, a quiénes invitarías?
Crea una lista que contenga al menos 3 personas con las que te gustaría ir a
cenar. Después usa esa lista para imprimir un mensaje a cada persona,
invitándoles a la cena.
"""

guest_list = ["Cristina", "June", "Sheila"]

for person in guest_list:
    print(f"{person}, you're invited to a dinner party tonight!")

print("\n\n")



# 05 - CAMBIANDO LA LISTA DE INVITADOS
print("05 - CAMBIANDO LA LISTA DE INVITADOS\n")
"""
Uno de los invitados no puede asistir a la cena, así que debes modificar la lista
para enviársela a los nuevos invitados. Deberás pensar a quién invitar esta vez.

- Comienza el programa desde el apartado anterior. Crea un print() que muestre el
nombre del invitado que no puede venir.
- Modifica tu lista sustituyendo el nombre del invitado que no puede por el nombre
de la nueva persona a la que invitas.
- Imprime un segundo juego de mensajes de invitación, uno para cada persona que
sique en la lista.
"""

not_coming = guest_list[2]
print(f"{not_coming} is not coming")

guest_list[2] = "Clara"

for person in guest_list:
    print(f"{person}, you're invited to a dinner party tonight!")

print("\n\n")



# 06 - MÁS INVITADOS
print("06 - MÁS INVITADOS\n")
"""
Has encontrado un lugar donde poder invitar a más personas a la cena. Piensa en otros
tres invitados.

- Comience con su programa desde el ejercicio anterior. Añade una llamada a print()
al final de tu programa informando a la gente de que has encontrado un lugar mejor.
- Use insert() para añadir un nuevo invitado al principio de su lista.
- Utilice insert() para añadir un nuevo invitado a la mitad de la lista.
- Utilice append() para añadir un nuevo invitado al final de la lista.
- Imprima un nuevo conjunto de mensajes de invitación, uno por cada persona de su lista.
"""

print("I've found a bigger place to celebrate the dinner party. More people will be invited!")

guest_list.insert(0, "Thom")
guest_list.insert(2, "Piedad")
guest_list.append("Vero")

for person in guest_list:
    print(f"{person}, you're invited to a dinner party tonight!")

print("\n\n")



# 07 - REDUCCIÓN DE LA LISTA DE INVITADOS
print("07 - REDUCCIÓN DE LA LISTA DE INVITADOS\n")
"""
Acabas de descubrir que el nuevo lugar para la celebración de la cena no está disponible, y
solo tienes espacio para dos invitados.

- Comienza tu programa desde el apartado anterior. Crea un print() que indique que solo
puedes invitar a dos personas.
- Utilice pop() para eliminar invirados de la lista de uno en uno hasta que solo queden 2
nombres en la lista. Cada vez que elimine un numbre de su lista, imprima un mensaje a esa
persona diciéndole que lamenta no poder invitarla.
- Imprime un mensaje para las personas que siguen invitadas haciéndoles saber que están invitadas
- Usa del() para eliminar los últimos dos nombres de la lista e imprime la lista para comprobar
que está vacía.
"""

print("I am sorry to inform you that I can only invite two people to dinner tonight...")

# podría hacerse con bucles, condiciones, etc. Pero en la teoría aún no se han visto las
# condiciones, por lo que se va a realizar "a mano" de la siguiente manera:
print(f"{guest_list.pop()}, I'm sorry, I won't be able to finally invite you to dinner tonight...")
print(f"{guest_list.pop()}, I'm sorry, I won't be able to finally invite you to dinner tonight...")
print(f"{guest_list.pop()}, I'm sorry, I won't be able to finally invite you to dinner tonight...")
print(f"{guest_list.pop()}, I'm sorry, I won't be able to finally invite you to dinner tonight...")

for person in guest_list:
    print(f"Hi {person}! You're still invited to dinner tonight!")

del(guest_list[0])
del(guest_list[0])
print(guest_list)       # []

print("\n\n")



# 08 - MOSTRANDO LA PALABRA
print("08 - MOSTRANDO LA PALABRA\n")
"""
Piensa en al menos 5 lugares del mundo que te gustara visitar.

- Guarda las ubicaciones en una lista. Asegúrese de que la lista no esté en orden alfabético.
- Imprime la lista en su orden original.
- Utilice sorted() para imprimir su lista en orden alfabético sin modificar el orden de
la lista original.
- Muestre que su lista sigue en su orden original imprimiéndola.
- Utilice sorted() para imprimir su lista en orden alfabético inverso sin modificar el
orden de la lista original.
- Muestre que su lista sigue en su orden original imprimiéndola.
- Usa reverse() para cambiar el orden de tu lista. Imprímela para mostrar la diferencia.
- Usa reverse() otra vez para que la lista vuelva a ser la original. Imprímela.
- Usa sort() para ordenar la lista alfabéticamente. Imprímela para demostrar que ha sido
modificada.
- Usa sort() para ordenar la lista en orden alfabético inverso. Imprímela para demostrar
que ha sido modificada.
"""

places = ["Murcia", "Madrid", "New Zealand", "Iceland", "Belgium"]

print(places)               # ['Murcia', 'Madrid', 'New Zealand', 'Iceland', 'Belgium']

print(sorted(places))       # ['Belgium', 'Iceland', 'Madrid', 'Murcia', 'New Zealand']

print(places)               # ['Murcia', 'Madrid', 'New Zealand', 'Iceland', 'Belgium']

print(sorted(places, reverse=True))     # ['New Zealand', 'Murcia', 'Madrid', 'Iceland', 'Belgium']

print(places)               # ['Murcia', 'Madrid', 'New Zealand', 'Iceland', 'Belgium']

places.reverse()
print(places)               # ['Belgium', 'Iceland', 'New Zealand', 'Madrid', 'Murcia']

places.reverse()
print(places)               # ['Murcia', 'Madrid', 'New Zealand', 'Iceland', 'Belgium']

places.sort()
print(places)               # ['Belgium', 'Iceland', 'Madrid', 'Murcia', 'New Zealand']

places.sort(reverse=True)
print(places)               # ['New Zealand', 'Murcia', 'Madrid', 'Iceland', 'Belgium']

print("\n\n")



# 09 - INVITADOS A LA CENA
print("09 - INVITADOS A LA CENA\n")
"""
Recupera la lista del ejercicio 06 e imprime la cantidad de invitados de la lista.
"""

guest_list = ["Thom", "Cristina", "Piedad", "June", "Clara", "Vero"]

print(len(guest_list))

print("\n\n")