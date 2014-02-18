__author__ = 'thehoule'

import decimal
import math
import time
import matplotlib.pyplot as py

def compute():
    factorial_steps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1000, 10000, 20000]
    computed_factorial_results = []
    factorial_time_results = []

    # Compute lager integer factorial for all elements
    # inside factorial steps list
    for x in range(len(factorial_steps)):
        start = time.time()
        large_integer_factorial = math.factorial(factorial_steps[x])
        runtime = time.time()
        computed_factorial_results.append(decimal.Decimal(large_integer_factorial).normalize())
        time_difference = runtime - start
        factorial_time_results.append(time_difference)


    highest_factorial_one_minute = 1
    highest_factorial_computed = 1

    start = time.time()
    while time.time() - start < 60:
        highest_factorial_one_minute += 1
        highest_factorial_computed = highest_factorial_one_minute * highest_factorial_computed

    runtime = time.time()
    computational_time = runtime - start

    print("Largest computed n! in one minute: ", highest_factorial_one_minute)
    print("Computation time during largest factorial computation: ", computational_time)
    print("Computed factorial results: ", computed_factorial_results)


    py.xlabel("Computed Factorial of N size")
    py.ylabel("Computational Time")
    py.plot(factorial_steps, factorial_time_results, 'g^-')
    py.show()


    py.xlabel("Computed Factorial of N size")
    py.ylabel("Log10 Results")
    py.xscale('log')
    py.plot(factorial_steps, factorial_time_results, 'bo-')
    py.show()

compute()