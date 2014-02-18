__author__ = 'thehoule'

import math
import matplotlib.pyplot as py

def calculate():
    x_value = math.sqrt(2)
    pi_approximation = 2 + math.sqrt(2)
    y_value = 2 ** .25

    absolute_pi_error = []
    n = []
    n_error = []
    pi = []
    number_steps = []
    for c in range(20):
        x_value = .5 * (math.sqrt(x_value) + (1 / math.sqrt(x_value)))
        pi_approximation = pi_approximation * ((x_value + 1) / (y_value + 1))
        y_value = (y_value * math.sqrt(x_value) + 1 / math.sqrt(x_value)) / (y_value+1)
        pi.append(pi_approximation)
        number_steps.append(c + 1)
        error = math.pi - pi_approximation
        absolute_pi_error.append(math.fabs(error))
        n_error.append(10 ** (-1 * (2 ** (c + 2))))
        n.append(10 ** (-2 * (c + 2)))

    print("Calculated pi approximation: ", pi_approximation)
    print("Actual value of pi: ", math.pi, "\n")
    print("Computed absolute error of pi: ", absolute_pi_error)
    print("The nth term: ", n)


    py.plot(number_steps, n, 'g-')
    py.plot(number_steps, n_error, 'b-')
    py.plot(number_steps, absolute_pi_error, 'r-')
    py.xlabel("Number of Iterations")
    py.ylabel("Calculated Value")
    py.yscale('log')
    py.show()

calculate()