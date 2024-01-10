import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from ..introduction.lab_session import get_df_can


df_can = get_df_can()

# Crear un nuevo DataFrame con los siguientes 3 países
df_dsn = df_can.loc[["Denmark", "Norway", "Sweden"], :]

# Obtener el total y las proporciones en función al total
total_values = df_dsn["Total"].sum()
category_proportions = df_dsn["Total"] / total_values

# Paso 1: Imprimir las proporciones

pd.DataFrame({"Category Proportion": category_proportions})

# Paso 2: Definir el tamaño

width = 40
height = 10

total_num_tiles = width * height

print(f"Total number of tiles is {total_num_tiles}.")

# Paso 3: Calcular el número de bloques por cada categoría

tiles_per_category = (category_proportions * total_num_tiles).round().astype(int)

pd.DataFrame({"Number of tiles": tiles_per_category})

# Paso 4: Crear una matriz que represente el gráfico

waffle_chart = np.zeros((height, width), dtype=np.uint)

# Definir índices para recorrer en el chart
category_index = 0
tile_index = 0

# Rellenar el gráfico
for col in range(width):
    for row in range(height):
        tile_index += 1

        if tile_index > sum(tiles_per_category[0:category_index]):
            category_index += 1
        
        waffle_chart[row, col] = category_index

print("Waffle chart populated!")

# Paso 5: Mapear el gráfico a algo visual

fig = plt.figure()

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()
plt.show()

# Paso 6: 'Hacer bonito' el gráfico

# instantiate a new figure object
fig = plt.figure()

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()

# get the axis
ax = plt.gca()

# set minor ticks
ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
    
# add gridlines based on minor ticks
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

plt.xticks([])
plt.yticks([])
plt.show()