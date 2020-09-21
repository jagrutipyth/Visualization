import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = 'death_valley_2018_simple.csv'
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

        '''Get dates and high,low temperatures from this file.'''
        
          #The reader object continues from where it left off in the
         #CSV file and automatically returns each line following its current position.
         #Because we’ve already read the header row, the loop will begin at the second
         #line where the actual data begins.
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d') # method strptime() is used the string containing
            #  first argument-value , The second argument-Python how date is formatted
            try: #If there is any missing data then except block will be executed
                high = int(row[5])
                low = int(row[6])
            except ValueError: #here for some dates data is missing
                print(f"Missing data for {current_date}")
            else: #if no exception is raised this will be executed.
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
        


# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5) #we make the red and blue plot lines appear lighter with alpha 0.5
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  #this method is usedto fill area between
# two graphs, pass x-values & both Y-values

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # draws date labels diagonally to prevent them from overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()