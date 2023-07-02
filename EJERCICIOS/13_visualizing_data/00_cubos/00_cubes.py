print("00 - CUBOS")
"""
Un cubo es un número elevado a la tercera potencia. Crea un gráfico que muestre
los valores cúbicos de los primeros cinco números. Después, muestra el cubo de
los primeros 5000 números.
"""

import matplotlib.pyplot as plt

# dibujando datos de los primeros 5 números
# x_values = [1, 2, 3, 4, 5]
# y_values = [x**3 for x in x_values]

# dibujando datos de los primeros 5000 números
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# chart title and labels
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# size of tick labels
ax.tick_params(axis="both", which="major", labelsize=14)

# range
# dibujando datos de los primeros 5 números
# ax.axis([0, 6, 0, 150])

# dibujando datos de los primeros 5 números
ax.axis([0, 6000, 0, 150_000_000_000])

plt.show()