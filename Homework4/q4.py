__author__ = 'thehoule'
import math

#code for question 4

#initialize the numbers
x = math.sqrt(2)
pi_approx = 2 + math.sqrt(2)
y = 2 ** (.25)
abs_error = []
ten_pow_nth = []
pi_list = []
steps = []
#now iterate through to approximate pi
for i in range(1000):
    x = .5*(math.sqrt(x) + (1/math.sqrt(x)))
    pi_approx = pi_approx *((x+1)/(y+1))
    y = (y*math.sqrt(x) + 1/math.sqrt(x))/(y+1)
    pi_list.append(pi_approx)
    steps.append(i+1)
    abs_err = math.pi - pi_approx
    abs_error.append(math.fabs(abs_err))
    ten_pow_nth.append(10**(-2*(i+2)))

print(pi_approx)
print(math.pi)
print()
print(abs_error)
print(ten_pow_nth)