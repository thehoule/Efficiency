__author__ = 'thehoule'

#Parameters
Ts = 19
Tc = 84
r = 0.025
h = [30, 15, 10, 5, 1, 0.5, 0.25]

Temp = []
BackTemp = []
ModTemp = []

Temp.append(Tc)
BackTemp.append(Tc)
ModTemp.append(Tc)

#Forward Euler Equation
for x in h:
    for z in range(0, 300):
        if(z != 0) and (((x * 10) % z) == 0):
            Temp.append(round(Temp[-1] + z * (-r*(Temp[-1] - Ts)), 2))

#Backward Euler Equation
for i in h:
    for c in range(0, 30):
        if (c != 0) and (((i * 10) % c) == 0):
            BackTemp.append(round((BackTemp[-1] + (r * c * Ts)) / (1 + (r * c)), 2))

#Modiified Euler Equation
for f in h:
    for d in range(0, 30):
        if (d != 0) and (((f * 10) % d) == 0):
            ModTemp.append(round((((1 - ((r * d) / 2)) * ModTemp[-1]) + (r * d * Ts)) / (1 + ((r * d) / 2)), 2))


Temp.sort(reverse=True)
BackTemp.sort(reverse=True)
ModTemp.sort(reverse=True)

print("Results of the various equations using the step sizes in seconds : ", h)
print("Forward Euler result = ", Temp)
print("Backward Euler result = ", BackTemp)
print("Modified Euler result = ", ModTemp)

