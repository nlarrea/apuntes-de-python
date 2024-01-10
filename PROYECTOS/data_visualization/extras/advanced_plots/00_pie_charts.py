import pandas as pd
import matplotlib.pyplot as plt

from ..introduction.lab_session import get_df_can


# Leer los datos del Excel
df_can = get_df_can()

# Agrupar los datos por continentes, usando la columna Continent y sumar
# la cantidad de datos
df_continents = df_can.groupby("Continent", axis=0).sum()

# Guarde los valores de las columnas de los años y
# añadir columna de 'Total' al DataFrame
years = list(map(str, range(1980, 2014)))
df_continents["Total"] = df_continents[years].sum(axis=1)

# Creamos el gráfico
df_continents["Total"].plot(kind="pie")
plt.title("Immigration to Canada by Continent [1980-2013]")
plt.savefig("./extras/advanced_plots/plots/pie_chart.png")