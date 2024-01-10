import pandas as pd

def get_df_can(print_data: bool = False) -> pd.DataFrame:
    # Leer los datos y guardarlos en un DataFrame
    df_can = pd.read_excel(
        "./extras/data/Canada.xlsx",
        sheet_name="Canada by Citizenship",
        skiprows=range(20),
        skipfooter=2
    )

    # Limpiar el dataset para eliminar columnas innecesarias
    df_can.drop(["AREA", "REG", "DEV", "Type", "Coverage"], axis=1, inplace=True)
    # -> Otra forma de hacerlo si hubiera muchísimas más columnas
    # que quisiéramos eliminar:
    # wanted_columns = [*years, "Total"]
    # df_continents = df_continents[wanted_columns]

    # Cambiamos el nombre a las columnas para que tengan más sentido
    df_can.rename(
        columns={
            "OdName": "Country",
            "AreaName": "Continent",
            "RegName": "Region"
        },
        inplace=True
    )

    # Para que todo sea más accesible, cambiamos los tipos de datos
    # de todas las columnas al tipo string
    df_can.columns = list(map(str, df_can.columns))

    # Asignamos la columna 'Country' como índice
    df_can.set_index("Country", inplace=True)

    # Los años con los que estaremos trabajando - útil tenerlos a
    # mano para trabajar con ellos más tarde
    years = list(map(str, range(1980, 2014)))
    # Añadir la columna de 'Total'
    df_can["Total"] = df_can[years].sum(axis=1)

    if print_data:
        print(df_can)
        print("data dimensions:", df_can.shape)

    return df_can