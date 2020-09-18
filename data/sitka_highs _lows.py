import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = 'sitka_weather_2018_simple.csv'
with open(filename,'r') as reader:
    reader = csv.reader(reader) #he csv module contains a next() function, which returns the next line
# in the file when passed the reader object. In the preceding listing, we call
# next() only once so we get the first line of the file, which contains the file
# headers

    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []

    #print(header_row)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates and high temperatures from this file.

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    print(highs)


# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5) #we make the red and blue plot lines appear lighter with alpha 0.5
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  #this method is usedto fill area between
# two graphs, pass x-values & both Y-values

# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # draws date labels diagonally to prevent them from overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()