import csv

filename = "download_data_section/data/sitka_weather_07-2014.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)