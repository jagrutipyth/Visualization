import matplotlib.pyplot as plt

print(plt.style.available) # to see built style available

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('fivethirtyeight') # using built in styles
fig, ax = plt.subplots() #. This function can generate one or more plots in the same figure. The variable fig represents the
                         # entire figure or collection of plots that
                         #are generated. The variable ax represents a single plot in the figure
ax.scatter(2, 4, s=200) #here you can first declare x_list and y_list then pass them here
ax.plot(input_values,squares,linewidth = 3,color = 'pink')
ax.set_title("Square numbers",fontsize = 24)
ax.set_xlabel("value",fontsize = 14)
ax.set_ylabel("Sqaure of value",fontsize = 14)
ax.tick_params(axis='both',labelsize=14)

plt.show()
