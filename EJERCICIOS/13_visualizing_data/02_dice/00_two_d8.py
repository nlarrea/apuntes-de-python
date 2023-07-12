print("00 - DOS D8\n")
"""
Crea una simulación que muestre qué ocurre cuando se lanzan dos dados de ocho
lados 1000 veces.
"""

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create two D8
die_1 = Die(8)
die_2 = Die(8)

# make 1000 rolls and store results in a list
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze results
frequencies = []
max_value = die_1.num_sides + die_2.num_sides

for value in range(2, max_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
x_values = list(range(2, max_value + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of Result"}

my_layout = Layout(
    title="Results of rolling two D8s 1000 times",
    xaxis=x_axis_config,
    yaxis=y_axis_config
)

offline.plot({"data": data, "layout": my_layout}, filename="../../EJERCICIOS/13_visualizing_data/02_dice/plots/2_d8.html")