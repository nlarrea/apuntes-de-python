import json

# Explore the structure of the data
filename = "download_data_section/data/eq_data_1_day_m1.json"

with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = "download_data_section/data/generated/readable_eq_data.json"
with open(readable_file, "w") as f:
    json.dump(all_eq_data, f, indent=4)