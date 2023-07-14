import csv

filename = "download_data_section/data/sitka_weather_07-2014.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)