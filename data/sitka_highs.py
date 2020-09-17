import csv
import matplotlib.pyplot as plt
filename = 'sitka_weather_07-2018_simple.csv'
with open(filename,'r') as reader:
    reader = csv.reader(reader) #he csv module contains a next() function, which returns the next line
# in the file when passed the reader object. In the preceding listing, we call
# next() only once so we get the first line of the file, which contains the file
# headers

    header_row = next(reader)

    #print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

# Get high temperatures from this file.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
    print(highs)


# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot.
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()