import pandas as pd
import matplotlib.pyplot as plt

from lab_session import get_df_can


df_can = get_df_can()

years = list(map(str, range(1980, 2014)))
df_canada = df_can.pivot_table(index="Country", values=years)

df_canada.loc["Belgium", years].plot(kind="line")

plt.title("Immigration from Belgium")
plt.ylabel("Number of immigrants")
plt.xlabel("Years")

plt.savefig("./03_extras/00_introduction/plots/line_plot.png")