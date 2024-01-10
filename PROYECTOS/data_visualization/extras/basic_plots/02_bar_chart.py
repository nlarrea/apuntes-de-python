import pandas as pd
import matplotlib.pyplot as plt

from ..introduction.lab_session import get_df_can


# Leer los datos del Excel
df_can = get_df_can()

# Crear un nuevo DataFrame que use los países como índices y
# guarde los valores de las columnas de los años
years = list(map(str, range(1980, 2014)))
df_canada = df_can.pivot_table(index="Country", values=years)

# Creamos el nuevo DataFrame que contenga los datos de Iceland
df_iceland = df_canada.loc["Iceland", years]

# Creamos el gráfico de barras
df_iceland.plot(kind="bar")

plt.title("Icelandic immigrants to Canada from 1980 to 2013")
plt.ylabel("Number of immigrants")
plt.xlabel("Year")

plt.savefig("./extras/basic_plots/plots/bar_chart.png")