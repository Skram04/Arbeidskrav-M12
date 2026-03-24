import math as m

x = 0
v = 0
v0 = 150
g = -9.81 
a = 1 / 2 * -g
b = v0

print ("test", v0 + m.sqrt(v0**2 * -4 * 4.905 * -15.3) / 2 * 4.905)

def f(x):
    return (v-v0) / g

def y(x): 
    pluss = (150 + m.sqrt(150**2 * (-4) * 4.905 * (-15.3))) / (2 * 4.905)
    print ("pluss", pluss)
    minus = v0 - m.sqrt(v0**2 * (-4) * 4.905 * (-15.3)) / (2 * 4.905)
    print ("minus", minus)
    if pluss > 0:
        return pluss
    else:
        return minus




print (f(x))
print (y(x))