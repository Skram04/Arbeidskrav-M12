from math import sqrt

x = 0
v = 0
v0 = 150
g = -9.81 
a = 1 / 2 * -g
b = v0

def f():
    return (v-v0)

def y(): 
    pluss = (150 + sqrt(150**2 * (-4) * 4.905 * (-15.3))) / (2 * 4.905)
    minus = v0 - sqrt(v0**2 * (-4) * 4.905 * (-15.3)) / (2 * 4.905)

print (f(), "funksjon f")
print (y(), "funksjon y")