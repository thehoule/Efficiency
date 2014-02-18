__author__ = 'thehoule'

import math
import matplotlib.pyplot as py

def calculation():
    approximation_size = 200000
    approximated_pi_value = 0
    step_size = []
    actual_computed_pi_value = []
    estimated_calculated_pi_value = []
    for x in range(approximation_size):
        step_size.append(x + 1)
        actual_computed_pi_value.append(round(math.atan(1), (x + 1)))
        if x % 2 == 0:
            approximated_pi_value += (1 / ((x * 2) + 1))
        else:
            approximated_pi_value -= (1 / ((x * 2) + 1))
        estimated_calculated_pi_value.append(approximated_pi_value)
    #print("Actual computed pi value: ", actual_computed_pi_value)
    #print("Calculated approximated pi value: ", estimated_calculated_pi_value)

    py.xlabel("Iterations")
    py.ylabel("Calculated Value")
    py.xscale('log')
    py.plot(step_size, estimated_calculated_pi_value, 'g^-')
    py.plot(step_size, actual_computed_pi_value, 'bo-')
    py.show()

calculation()