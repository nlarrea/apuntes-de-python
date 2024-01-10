import pandas as pd
import matplotlib.pyplot as plt

india_china_df = pd.DataFrame(
    data={
        "India": [8880, 8670, 8147, 7338, 5704],
        "China": [5123, 6682, 3308, 1863, 1527]
    },
    index=[1980, 1981, 1982, 1983, 1984],
)

# Gráfico de línea
# india_china_df.plot(kind="line")
# plt.savefig("./03_extras/00_introduction/plots/pandas_line_graph.png")

# Histograma
india_china_df["India"].plot(kind="hist")
plt.savefig("./03_extras/00_introduction/plots/pandas_histogram.png")