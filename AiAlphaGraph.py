"""
AiAlphaGraph.py
Rob Standifer
CS3030
This program reads the data from AiAlpha.py into a list
and plots the data using matpolotlib

"""

import matplotlib.pyplot as plt


# Initialize data list

alpha_data = []
float_alpha_data = []


# Read ai alpha test data from txt file

with open('AiAlpha.txt', 'r') as file:
    for line in file:

        # Remove linebreaks

        currentItem = line[:-1]

        # Add item to list

        alpha_data.append(currentItem)


# Close test data file

file.close()

# Cast list of strings to list of floats

for item in alpha_data:
    
    float_item = float(item)
    
    float_alpha_data.append(float_item)


# Graph the test data

plt.plot(float_alpha_data, 'oy', label = 'alpha')
plt.xlabel('AI Trial Runs')
plt.ylabel('Seconds')
plt.legend()
plt.show()

