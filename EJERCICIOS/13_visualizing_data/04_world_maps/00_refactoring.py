print("00 - REFACTORIZAR\n")
"""
El bucle que toma los datos de 'all_eq_dicts' usa una variable por cada dato
que se va a guardar. Esto se hizo así para que fuera más legible, sin embargo,
no es necesario.
Refactoriza el código de 'eq_world_map.py' para no tener que guardar estos
datos en esas variables.
"""

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
filename = "./data/eq_data_30_day_m1.json"

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geomtery"]["coordinates"][1])
    hover_texts.append(eq_dict["properties"]["title"])

# Map the earthquakes
data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": hover_texts,
    "marker": {
        "size": [5 * mag for mag in mags],
        "color": mags,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Magnitude"}
    }
}]
my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="download_data_section/data/generated/global_earthquakes.html")