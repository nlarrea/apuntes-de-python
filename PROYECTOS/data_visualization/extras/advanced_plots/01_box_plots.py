import pandas as pd
import matplotlib.pyplot as plt

from ..introduction.lab_session import get_df_can


# Leer los datos del Excel
df_can = get_df_can()

# Crear un nuevo DataFrame que use los países como índices y
# guarde los valores de las columnas de los años
years = list(map(str, range(1980, 2014)))
df_canada = df_can.pivot_table(index="Country", values=years)

# Creamos un nuevo DataFrame que contenga solo los datos de Japón
df_japan = df_canada.loc[["Japan"], years].transpose()

# Creamos el gráfico
df_japan.plot(kind="box")
plt.title("Box plot of Japanese Immigrants from 1980-2013")
plt.ylabel("Number of Immigrants")
plt.savefig("./extras/advanced_plots/plots/box_plot.png")