from math import exp

def f(x):
    return x / (exp(x)+4)

dx = 0.5

def df(x):
    return (f(x + dx) - f(x)) / dx

x0 = 0

while df(x0) > 0:
    x0 += dx

print ("Toppunktet er", (x0, f(x0)))