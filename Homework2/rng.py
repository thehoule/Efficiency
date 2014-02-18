__author__ = 'thehoule'
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import random


#Setup variables
divisor = 86753098421
prospect_value = 183755194209
start = 374829731
sizes = [100, 1000, 10000, 100000, 1000000]
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
lists = [one_hundred, one_thousand, ten_thousand, one_hundred_thousand, one_million]
random_values = [rand_one_hundred, rand_one_thousand, rand_ten_thousand, rand_one_hundred_thousand, rand_one_million]

# generate random number through computation
for x in range(len(sizes)):
    for i in range(0, sizes[x]):
        start = (start + prospect_value) % divisor
        lists[x].append(round(start*.00000000001, 2))

#Create histograms of each random number size result
for a in range(len(sizes)):
    #Set labels and values
    labels, values = zip(*Counter(lists[a]).items())
    #Arrange labels
    indexes = np.arange(len(labels))
    width = .5
    #Subplot the figure and data
    fig, ax1 = plt.subplots()
    ax1.bar(indexes, values, width)
    #Format table to prevent overlapping
    fig.autofmt_xdate()
    plt.show()

# generate python random number for library random number generator
for z in range(len(sizes)):
    for c in range(0, sizes[z]):
        random_values[z].append(round(random.random(), 2))

#Create graphs of python random numbers
for t in range(len(sizes)):
    #Set labels and values
    labels, values = zip(*Counter(random_values[t]).items())
    #Arrange labels
    indexes = np.arange(len(labels))
    width = .5
    #Subplot the figure and data
    fig, ax1 = plt.subplots()
    ax1.bar(indexes, values, width)
    #Format table to prevent overlapping
    fig.autofmt_xdate()
    plt.show()