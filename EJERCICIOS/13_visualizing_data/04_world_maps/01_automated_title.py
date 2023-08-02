print("01 - TÍTULO AUTOMÁTICO\n")
"""
En el código escrito a lo largo del curso, hemos usado un título que está
hardcodeado en la variabel 'my_layout'. Cambia este título para que sea uno
dinámico dependiendo del archivo que se abra.
"""

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
filename = "./data/eq_data_30_day_m1.json"

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]
file_title = all_eq_data["metadata"]["title"]

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
my_layout = Layout(title=file_title)

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="./data/generated/global_earthquakes.html")