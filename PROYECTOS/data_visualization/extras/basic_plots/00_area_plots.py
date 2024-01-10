import pandas as pd
import matplotlib.pyplot as plt

from ..introduction.lab_session import get_df_can


# Leer los datos del Excel
df_can = get_df_can()

# Crear un nuevo DataFrame que use los países como índices y
# guarde los valores de las columnas de los años
years = list(map(str, range(1980, 2013)))
df_canada = df_can.pivot_table(index="Country", values=years)

# Añadir columna de 'Total' al DataFrame
df_canada["Total"] = df_canada[years].sum(axis=1)

# Ordenar los valores en función a la columna 'Total' de forma descendiente
df_canada.sort_values(["Total"], ascending=False, axis=0, inplace=True)

# Creamos un nuevo DataFrame que contenga sólo los 5 primeros países del
# DataFrame que está ordenado y transponer el DataFrame porque queremos
# tener los años en el eje vertical
df_top5 = df_canada.head()
df_top5 = df_top5[years].transpose()

# Generamos el gráfico
df_top5.plot(kind="area")

plt.title("Immigration trend of top 5 countries")
plt.ylabel("Number of immigrations")
plt.xlabel("Years")

plt.savefig("./extras/basic_plots/plots/area_plot.png")