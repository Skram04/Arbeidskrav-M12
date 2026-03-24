from math import sqrt

x = 0
v = 0
v0 = 150
g = -9.81 
a = 1 / 2 * -g
b = v0

print ("test", v0 + sqrt(v0**2 * -4 * 4.905 * -15.3) / 2 * 4.905)

def f(v,v0):
    return (v-v0)

def y(): 
    pluss = (150 + sqrt(150**2 * (-4) * 4.905 * (-15.3))) / (2 * 4.905)
    minus = v0 - sqrt(v0**2 * (-4) * 4.905 * (-15.3)) / (2 * 4.905)

print (f(0,150), "hei")
print (y(), "heihei")