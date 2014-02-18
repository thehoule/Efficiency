__author__ = 'thehoule'

import math
import matplotlib.pyplot as plt


a = 1
b = 1024
n = 513
sums = 0
test = 0
midpoint = []
trapezoid = []
simpson = []

#Integral function to run cotes and other equations through
def function(var_x):
    integral = 1 + ((math.sin(var_x) * math.cos(((2 * var_x) / 3))) * math.sin((4 * var_x)))
    return integral

#Create a range using step size
def my_range(beginning, end, step):
    while beginning <= end:
        yield beginning
        beginning += step

#Find midpoint formula delta x
def mid_delta_x(size_n):
    delta = (((math.pi * 2) - 0)/size_n)
    return delta

#Find trapezoidal formula delta x
def trap_delta_x(size_n):
    delta = (((math.pi * 2) - 0)/(size_n - 1))
    return delta

#Find simpson formula delta x
def simp_delta_x(size_n):
    delta = (((math.pi * 2) - 0)/(size_n * 2))
    return delta

#Find trapezoidal wi
def trap_wi(size_n, this_n):
    delta = trap_delta_x(size_n)
    if size_n == 1 or size_n == this_n:
        wi = (delta / 2)
        return wi
    else:
        wi = delta
        return wi

#Find simpson wi
def simp_wi(size_n, this_n):
    delta = simp_delta_x(this_n)
    if size_n == 1 or size_n == ((2 * this_n) + 1):
        wi = (delta / 3)
        return wi
    if size_n % 2 == 0:
        wi = ((4 * delta) / 3)
        return wi
    else:
        wi = ((2 * delta) / 3)
        return wi

#Create Midpoint list of sums for each N size
for x in my_range(0, b, 2):
    midpoint_xi = []
    xi_func = 0
    xi = 0
    if x == 0:
        for i in range(1):
            wi = mid_delta_x(1)
            xi_func = 0 + ((1 - .5) * wi)
            xi = function(xi_func)
            sums = (wi * xi)
            midpoint_xi.append(sums)
        sums = 0

    else:
        if x % 2 == 0:
            for c in range(x):
                wi = mid_delta_x(x)
                xi_func = 0 + (((c+1) - .5) * wi)
                xi = function(xi_func)
                sums = (wi * xi)
                midpoint_xi.append(sums)
            sums = 0
            test = 0
            for h in range(len(midpoint_xi)):
                test += midpoint_xi[h]
            midpoint.append(test)



#Create Trapezoidal list of sums for each step size N
for x in my_range(0, b, 2):
    trapezoid_xi = []
    xi_func = 0
    xi = 0
    if x == 0:
        continue
    if x % 2 == 0:
        for c in range(x):
            wi = trap_wi(x+1, c)
            delta = trap_delta_x(x)
            xi_func = 0 + (((c+1) - 1) * delta)
            xi = function(xi_func)
            sums = (wi * xi)
            trapezoid_xi.append(sums)
        sums = 0
        test = 0
        for h in range(len(trapezoid_xi)):
            test += trapezoid_xi[h]
        trapezoid.append(test)



#Create Simpson list of sums for each step size N
for x in my_range(0, b, 2):
    simpson_xi = []
    xi_func = 0
    xi = 0
    max = (x * 2) + 1
    if x == 0:
        for i in range(2 * x + 1):
            wi = simp_wi(1, max)
            delta = simp_delta_x(1)
            xi_func = 0 + ((1 - 1) * delta)
            xi = function(xi_func)
            sums = (wi * xi)
            simpson_xi.append(sums)
        sums = 0
        test = 0
    if x % 2 == 0 and x != 0:
        for c in range((2 * x) + 1):
            wi = simp_wi(c+1, x)
            delta = simp_delta_x(x)
            xi_func = 0 + (((c+1) - 1) * delta)
            xi = function(xi_func)
            sums = (wi * xi)
            simpson_xi.append(sums)
        sums = 0
        test = 0
        for h in range(len(simpson_xi)):
            test += simpson_xi[h]
        simpson.append(test)



plt.plot(midpoint, color='red')
plt.plot(trapezoid, color='blue')
plt.plot(simpson, color='green')
plt.show()

print("This is midpoint: ", midpoint)
print("This is trapezoidal: ", trapezoid)
print("This is Simpson: ", simpson)




