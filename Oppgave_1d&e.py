v0 = 150    #m/s**2
g = -9.81   #m/s**2
h = 0.001
x = 0

def f(x):
    return v0 * x + 0.5 * g * x**2

while f(x) <= f(x+h):
    x += h

print ("Tiden når kulen er på det høyeste punktet er", x)