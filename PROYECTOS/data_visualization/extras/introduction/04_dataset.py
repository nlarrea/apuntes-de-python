import pandas as pd

# Leer los datos y guardarlos en un DataFrame
df_can = pd.read_excel(
    "./03_extras/data/Canada.xlsx",
    sheet_name="Canada by Citizenship",
    skiprows=range(20),
    skipfooter=2
)

print(df_can)