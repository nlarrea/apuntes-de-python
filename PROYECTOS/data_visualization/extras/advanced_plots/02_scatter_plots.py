import pandas as pd
import matplotlib.pyplot as plt

from ..introduction.lab_session import get_df_can

# Leer los datos del Excel
df_can = get_df_can()

# Crear un nuevo DataFrame que use los países como índices y
# guarde los valores de las columnas de los años
years = list(map(str, range(1980, 2014)))
df_canada = df_can.pivot_table(index="Country", values=years)

# Crear un nuevo DataFrame que tenga las columnas 'Year' (con
# los valores de los años 1980-2013), y 'Total' (que sea el
# total de personas en cada año)
df_total = pd.DataFrame(
    data={
        "Year": years,
        # Añadimos la columna 'Total' al nuevo DataFrame
        "Total": df_canada[years].sum(axis=0).transpose()
    },
)

# Creamos el gráfico
df_total.plot(
    kind="scatter",
    x="Year",
    y="Total"
)

plt.title("Total Immigrants population to Canada from 1980-2013")
plt.xlabel("Year")
plt.ylabel("Number of Immigrants")

plt.savefig("./extras/advanced_plots/plots/scatter_plot.png")