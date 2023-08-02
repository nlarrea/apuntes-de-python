print("01 - COMPARACIÓN SITKA & DEATH VALLEY\n")
"""
Las temperaturas de Sitka y Death Valley son distintas, pero para realizar una
buena comparación, necesitamos que la escala del eje y sea igual en ambos.
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

sitka_filename = "./data/sitka_weather_2018_simple.csv"
death_valley_filename = "./data/death_valley_2018_simple.csv"

def get_data (filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, high and low temperatures from this file
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            try:
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    
    return dates, highs, lows


# Get data from files
sitka_dates, sitka_highs, sitka_lows = get_data(sitka_filename)
dv_dates, dv_highs, dv_lows = get_data(death_valley_filename)

# Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
# Plot Sitka's data
ax.plot(sitka_dates, sitka_highs, c='red', alpha=0.5)
ax.plot(sitka_dates, sitka_lows, c='blue', alpha=0.5)
# Plot Death Valley's data
ax.plot(dv_dates, dv_highs, c='orange', alpha=0.5)
ax.plot(dv_dates, dv_lows, c='purple', alpha=0.5)
# Same y-axis limits for both plots
ax.set_ylim([0, 120])
# Fill between lines
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.1)
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor='purple', alpha=0.1)

# Format plot
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)   

plt.show()