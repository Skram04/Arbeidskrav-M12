v0 = 150    #m/s**2
g = -9.81   #m/s**2
h = 0.001
x = 0

def f(x):
    return v0 * x + 0.5 * g * x**2          #Formel som finner strekningen med konstant akselerasjon

while f(x) <= f(x+h):                       #Finner toppunktet til funksjonen
    x += h

print (f"Tiden når kulen er på det høyeste punktet er {x:.2f}") 