N0 = 2

def N(t):
    return N0 * ((1/2)**(t/4))

for i in range(3):
    sekunder = i * 10
    print (N(sekunder), "Gram etter", sekunder, "sekunder")