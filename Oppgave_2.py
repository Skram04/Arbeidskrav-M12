from math import exp

def f(x):
    return x / (exp(x)+4)

dx = 0.5                                #Man burde senke verdien på denne slik at man ikke den deriverte med store verdier hver gang siden det gir lavere nøyaktighet

def df(x):
    return (f(x + dx) - f(x)) / dx      #Denne linjen regner ut den deriverte til f(x)

x0 = 0

while df(x0) > 0:                       #Øker den deriverte til den blir mindre eller lik null slik at man finner toppunktet
    x0 += dx

print ("Toppunktet er", (x0, f(x0)))