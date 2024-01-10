import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from ..introduction.lab_session import get_df_can


df_can = get_df_can()

# Crear un nuevo DataFrame que use los países como índices y
# guarde los valores de las columnas de los años
years = list(map(str, range(1980, 2014)))

# Obtener los valores totales
df_tot = pd.DataFrame(df_can[years].sum(axis=0))

# Cambiar los datos de los años a tipo float (útil más adelante
# para el gráfico)
df_tot.index = map(float, df_tot.index)

# Resetear el índice del DataFrame
df_tot.reset_index(inplace=True)

# Renombrar las columnas
df_tot.columns = ['year', 'total']

# Crear el gráfico
plt.figure(figsize=(15, 10))    # Aumentar tamaño del gráfico
sns.set(font_scale=1.5)         # Aumentar tamaño de fuente
# sns.set_style("ticks")        # Eliminar el color de fondo
sns.set_style("whitegrid")      # Fondo blanco con grid

ax = sns.regplot(
    data=df_tot,
    x="year",
    y="total",
    # Parámetros customizables:
    color="purple",
    marker=".",
    # Aumentar el tamaño de los markers:
    scatter_kws={"s": 200}
)

ax.set(xlabel="Year", ylabel="Total Immigration")
ax.set_title("Total Immigration to Canada from 1980-2013")

plt.show()