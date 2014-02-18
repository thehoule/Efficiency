__author__ = 'thehoule'

from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import random
import math


#Setup variables
divisor = 86753098421
prospect_value = 183755194209
start = 374829731
double_int = 475291345
sizes = [100, 1000, 10000, 100000, 1000000]
single_sum = 0
double_sum = 0

one_hundred = []
one_thousand = []
ten_thousand = []
one_hundred_thousand = []
one_million = []

rand_one_hundred = []
rand_one_thousand = []
rand_ten_thousand = []
rand_one_hundred_thousand = []
rand_one_million = []

integral_one_hundred = []
integral_one_thousand = []
integral_ten_thousand = []
integral_one_hundred_thousand = []
integral_one_million = []

double_one_hundred = []
double_one_thousand = []
double_ten_thousand = []
double_one_hundred_thousand = []
double_one_million = []

python_integral_one_hundred = []
python_integral_one_thousand = []
python_integral_ten_thousand = []
python_integral_one_hundred_thousand = []
python_integral_one_million = []

python_double_one_hundred = []
python_double_one_thousand = []
python_double_ten_thousand = []
python_double_one_hundred_thousand = []
python_double_one_million = []

lists = [one_hundred, one_thousand, ten_thousand, one_hundred_thousand, one_million]
random_values = [rand_one_hundred, rand_one_thousand, rand_ten_thousand, rand_one_hundred_thousand, rand_one_million]

single_integral_my_random = [integral_one_hundred, integral_one_thousand, integral_ten_thousand, integral_one_hundred_thousand, integral_one_million]
double_integral_my_random = [double_one_hundred, double_one_thousand, double_ten_thousand, double_one_hundred_thousand, double_one_million]

single_integral_python_random = [python_integral_one_hundred, python_integral_one_thousand, python_integral_ten_thousand, python_integral_one_hundred_thousand, python_integral_one_million]
double_integral_python_random = [python_double_one_hundred, python_double_one_thousand, python_double_ten_thousand, python_double_one_hundred_thousand, python_double_one_million]


#Single Integral
def single_integral(my_rand, pos):
    global single_sum
    carlo = ((math.log(math.pow(my_rand, 2))) * (math.log(math.pow((1 - my_rand), 2))))
    single_sum = single_sum + carlo
    integral = round(float(1 / pos) * single_sum)
    #print(integral)
    return integral

#Double Integral
def double_integral(x, y, pos):
    global double_sum
    double_carlo = (x * math.exp(y))
    double_sum = double_sum + double_carlo
    integral = round(float(1 / pos) * double_sum)
    return integral

# generate random number through computation and call single integration
for x in range(len(sizes)):
    for i in range(0, sizes[x]+1):
        start = (start + prospect_value) % divisor
        my_new_rand = round(start * .00000000001, 2)
        if i == 0 or my_new_rand == 0:
            continue
        else:
            single_integral_my_random[x].append(round((single_integral(my_new_rand, i)), 2))

# generate random number through computation and call double integration
for s in range(len(sizes)):
    for g in range(0, sizes[s]+1):
        start = (start + prospect_value) % divisor
        my_new_rand = round(start * .00000000001, 2)
        my_new_rand2 = round(start * .00000000001, 2)
        if g == 0 or my_new_rand == 0 or my_new_rand2 == 0:
            continue
        else:
            double_integral_my_random[s].append(round((double_integral(my_new_rand, my_new_rand2, g)), 2))

# generate python random number for library random number generator and call single integration
for z in range(len(sizes)):
    for c in range(0, sizes[z]+1):
        temp = round(random.random(), 2)
        if c == 0.00 or temp == 0.00:
            continue
        else:
            single_integral_python_random[z].append(round((single_integral(temp + .001, c)), 2))

# generate python random number for library random number generator and call double integration
for d in range(len(sizes)):
    for f in range(0, sizes[d]+1):
        temp1 = round(random.random(), 2)
        temp2 = round(random.random(), 2)
        if f == 0.00 or temp1 == 0.00 or temp2 == 0.00:
            continue
        else:
            double_integral_python_random[d].append(round((double_integral(temp1 + .001, temp2 + .001, f)), 2))

# print(len(single_integral_my_random[0]))
# print(single_integral_my_random[0])

#Create histograms of each my random single integral
for a in range(len(sizes)):
    #Set labels and values
    labels, values = zip(*Counter(single_integral_my_random[a]).items())
    #Arrange labels
    indexes = np.arange(len(labels))
    width = .5
    #Subplot the figure and data
    fig, ax1 = plt.subplots()
    ax1.bar(indexes, values, width)
    #Format table to prevent overlapping
    fig.autofmt_xdate()
    plt.show()

#Create histograms of each my random double integral
for b in range(len(sizes)):
    #Set labels and values
    labels, values = zip(*Counter(double_integral_my_random[b]).items())
    #Arrange labels
    indexes = np.arange(len(labels))
    width = .5
    #Subplot the figure and data
    fig, ax1 = plt.subplots()
    ax1.bar(indexes, values, width)
    #Format table to prevent overlapping
    fig.autofmt_xdate()
    plt.show()

#Create histograms of each python random single integral
for e in range(len(sizes)):
    #Set labels and values
    labels, values = zip(*Counter(single_integral_python_random[e]).items())
    #Arrange labels
    indexes = np.arange(len(labels))
    width = .5
    #Subplot the figure and data
    fig, ax1 = plt.subplots()
    ax1.bar(indexes, values, width)
    #Format table to prevent overlapping
    fig.autofmt_xdate()
    plt.show()

#Create histograms of each python random double integral
for h in range(len(sizes)):
    #Set labels and values
    labels, values = zip(*Counter(double_integral_python_random[h]).items())
    #Arrange labels
    indexes = np.arange(len(labels))
    width = .5
    #Subplot the figure and data
    fig, ax1 = plt.subplots()
    ax1.bar(indexes, values, width)
    #Format table to prevent overlapping
    fig.autofmt_xdate()
    plt.show()





# #Create graphs of python random numbers
# for t in range(len(sizes)):
#     #Set labels and values
#     labels, values = zip(*Counter(random_values[t]).items())
#     #Arrange labels
#     indexes = np.arange(len(labels))
#     width = .5
#     #Subplot the figure and data
#     fig, ax1 = plt.subplots()
#     ax1.bar(indexes, values, width)
#     #Format table to prevent overlapping
#     fig.autofmt_xdate()
#     plt.show()