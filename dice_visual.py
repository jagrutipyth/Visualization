from plotly.graph_objects import Bar, Layout
from plotly import offline
from random import randint
from die import Die

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)  # To analyze the rolls, we create the empty
    # list frequencies to store the number of times each value is rolled. We loop
    # through the possible values (1 through 6 in this case) at , count how many
    # times each number appears in results

    frequencies.append(frequency)

# print(frequencies)

# Visualize the results.
x_values = list(range(2, max_result + 1))  # Xaxis
data = [Bar(x=x_values, y=frequencies)]  # The Plotly class Bar()  needs a list of x-values, and a list of
# y-values.

x_axis_config = {'title': 'Result', 'dtick': 1}  # Now that we have more bars on the histogram, Plotly’s default
# settings will only label some of the bars. The 'dtick': 1 setting tells Plotly to label every tick mark

y_axis_config = {'title': 'Frequency of Result'}  # title of y axis

my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)  # The Layout() class returns an object that
# specifies the layout and configuration of the graph as a whole

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')  # This function needs a dictionary containing
# the data and layout objects
