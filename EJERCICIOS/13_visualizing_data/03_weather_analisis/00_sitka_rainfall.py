print("00 - LLUVIA EN SITKA\n")
"""
Sitka está en una selva templada, así que recibe una cantidad de lluvia enorme.
En el archivo 'sitka_weather_2018_simple.csv' hay un encabezado llamado 'PRCP'
que representa la cantidad de lluvia al día.
Haz una visualización de esta columna.
"""

import csv
import matplotlib.pyplot as plt

filename = "./data/sitka_weather_2018_simple.csv"

# Read file and save data in 'rainfalls' list
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # See what index we need to get data
    # for index, header in enumerate(header_row):
    #     print(index, header)
    # Now we know that PRCP -> at index 3

    rainfalls = []
    for row in reader:
        try:
            rainfall = float(row[3])
        except ValueError:
            print(f"Missing data.")
        else:
            rainfalls.append(rainfall)

# Plot the rainfalls
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(rainfalls, c="blue")

# Format plot
plt.title("Daily rainfalls", fontsize=24)
plt.xlabel("", fontsize=16)
plt.ylabel("Rainfalls", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()