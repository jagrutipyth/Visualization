from plotly.graph_objects import Bar, Layout
from plotly import offline
from random import randint
from die import Die

die = Die()

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)  # To analyze the rolls, we create the empty
    # list frequencies to store the number of times each value is rolled. We loop
    # through the possible values (1 through 6 in this case) at , count how many
    # times each number appears in results

    frequencies.append(frequency)

# print(frequencies)

# Visualize the results.
x_values = list(range(1, die.num_sides + 1))  # Xaxis
data = [Bar(x=x_values, y=frequencies)]  # The Plotly class Bar()  needs a list of x-values, and a list of
# y-values.

x_axis_config = {'title': 'Result'}  # title of x axis
y_axis_config = {'title': 'Frequency of Result'}  # title of y axis

my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)  # The Layout() class returns an object that
# specifies the layout and configuration of the graph as a whole

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')  #This function needs a dictionary containing
# the data and layout objects
