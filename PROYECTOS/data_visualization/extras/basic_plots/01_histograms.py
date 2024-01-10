import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from ..introduction.lab_session import get_df_can


# Leer los datos del Excel
df_can = get_df_can()

# Crear un nuevo DataFrame que use los países como índices y
# guarde los valores de las columnas de los años
years = list(map(str, range(1980, 2014)))
df_canada = df_can.pivot_table(index="Country", values=years)

# Calcular el ancho de las barras del histograma para que coincida
# con las marcas de los valores
count, bin_edges = np.histogram(df_canada["2013"])

df_canada["2013"].plot(kind="hist", xticks=bin_edges)

plt.title("Histogram of Immigration from 195 countries in 2013")
plt.ylabel("Number of Countries")
plt.xlabel("Number of Immigrants")

plt.savefig("./extras/basic_plots/plots/histogram.png")