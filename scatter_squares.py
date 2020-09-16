import matplotlib.pyplot as plt

x_values = range(1,1000)
y_values = [x**2 for x in x_values]
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
ax.scatter(x_values, y_values, s=10)


# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
plt.show()
#plt.savefig('squares_plot.png', bbox_inches='tight') #saves file in same directory , if you dont want to omit whit
# spaces omit 2nd arg