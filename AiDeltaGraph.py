"""
AiDeltaGraph.py
Rob Standifer
CS3030
This program reads the data from AiAlpha.py into a list
and plots the data using matpolotlib

"""

import matplotlib.pyplot as plt


# Initialize data list

delta_data = []
float_delta_data = []


with open('AiDelta1000RandomTimes.txt', 'r') as file:
    for line in file:

        # Remove linebreaks

        currentItem = line[:-1]

        # Add item to list

        delta_data.append(currentItem)


# Close test data file

file.close()

# Cast list of strings to list of floats

for item in delta_data:
    
    float_item = float(item)
    
    float_delta_data.append(float_item)


# Graph the test data
plt.plot(float_delta_data, 'or', label = 'delta')
plt.xlabel('AI Trial Runs')
plt.ylabel('Seconds')
plt.legend()
plt.show()
