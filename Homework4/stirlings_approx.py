__author__ = 'thehoule'

import math
import matplotlib.pyplot as py

def approximate():
    computed_factorial = []
    stirling_factorial = []
    absolute_error = []
    relative_error = []
    steps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Compute actual factorial to be calculated
    # into absolute and relative errors.
    for x in range(len(steps)):
        computed_factorial.append(math.factorial(steps[x]))

    # Compute Sterling's factorial to be calculated
    # into absolute and relative errors.
    for x in range(len(steps)):
        stirling_factorial.append(math.sqrt(2 * (math.pi * (steps[x]))) * (((steps[x]) / math.e) ** (steps[x])))

    # Calculate Absolute and Relative error from
    # Actual computed factorial and Stirling's Approximation
    for x in range(10):
        calculated_absolute_error = math.fabs(computed_factorial[x] - stirling_factorial[x])
        calculated_relative_error = calculated_absolute_error / computed_factorial[x]
        absolute_error.append(calculated_absolute_error)
        relative_error.append(calculated_relative_error)

    print("Calculated absolute error: ", absolute_error)
    print("Calculated relative error: ", relative_error)


    py.xlabel("Steps")
    py.ylabel("Error Value")
    py.yscale('log')
    py.plot(steps, absolute_error, 'g^-')
    py.plot(steps, relative_error, 'bo-')
    py.show()