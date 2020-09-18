import csv
import matplotlib.pyplot as plt
from datetime import datetime
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

    # Get dates and high temperatures from this file.

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
    print(highs)


# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # draws date labels diagonally to prevent them from overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()