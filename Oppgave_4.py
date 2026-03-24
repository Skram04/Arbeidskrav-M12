from math import sqrt

fart = [73,69,81,83,64,59,70]
dist = 0

a = 0
b = 90
n = 10000

dx = (b - a) / n
print ("delta x er", dx)

for f in fart:
    dist += f * dx

    #dist += f * 0.25        #Et kvarter = 0.25 timer
#dist += (-0.5 * fart[0] + 0.5 * fart[-1]) * 0.25

#print ("f-1", fart[-1])
print ("distanse = ", dist)

"""
for i in range (n):
    s += f(a + i * dx) *dx
s += (-0.5*f(a) + 0.5 f(b) * dx)

print ("Areal er", s)
"""