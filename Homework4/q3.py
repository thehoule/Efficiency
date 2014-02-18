__author__ = 'thehoule'
import math
import decimal
#copy and paste code below

act = (math.atan(1))
print(act)

#initialize lists to hold results and approximation for pi
act_pi = []
est_pi = []
pi_approx = (0)
for i in range(100000):
    act_pi.append(round(math.atan(1), i+1))
    if (i%2 == 0):
        pi_approx += (1/((i*2) + 1))
    else:
        pi_approx -= (1/((i*2) + 1))
    est_pi.append(pi_approx)
print(pi_approx)