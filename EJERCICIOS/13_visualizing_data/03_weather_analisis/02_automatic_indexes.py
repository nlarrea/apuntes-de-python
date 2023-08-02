print("02 - ÍNDICES AUTOMÁTICOS\n")
"""
Hasta ahora hemos hardcodeado los ínidices de la temperatura mínima y máxima,
las columnas TMIN y TMAX. Usa la fila de encabezados para determinar los
índices de estos valores para los gráficos de Sitka y Death Valley.
Usa también títulos dinámicos para tus gráficos.
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

sitka_filename = "./data/sitka_weather_2018_simple.csv"
death_valley_filename = "./data/death_valley_2018_simple.csv"

def get_data(filename:str) -> list:
    """ Read and return data from .csv file. """
    
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, header in enumerate(header_row):
            if header == "TMIN":
                tmin_index = index
            elif header == "TMAX":
                tmax_index = index
            elif header == "DATE":
                date_index = index
        
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
            try:
                high = int(row[tmax_index])
                low = int(row[tmin_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    
    return dates, highs, lows


def create_plot(title:str, **kwargs:list):
    """ Plot the given data. """

    # Plot the hight and low temperatures
    plt.style.use("seaborn")
    fig, ax = plt.subplots()
    ax.plot(kwargs["dates"], kwargs["highs"], c='red', alpha=0.5)
    ax.plot(kwargs["dates"], kwargs["lows"], c='blue', alpha=0.5)
    plt.fill_between(kwargs["dates"], kwargs["highs"], kwargs["lows"], facecolor='blue', alpha=0.1)

    # Format plot
    plt.title(title, fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()


if __name__ == "__main__":
    # Get data from files
    s_dates, s_highs, s_lows = get_data(sitka_filename)
    dv_dates, dv_highs, dv_lows = get_data(death_valley_filename)

    # Plot data
    create_plot(
        "Daily high and low temperatures - Sitka 2018",
        dates=s_dates,
        highs=s_highs,
        lows=s_lows    
    )

    create_plot(
        "Daily high and low temperatures - Death Valley 2018",
        dates=dv_dates,
        highs=dv_highs,
        lows=dv_lows
    )