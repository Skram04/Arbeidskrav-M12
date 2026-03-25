#Mengde igjen av Rn-219 etter 0, 10 og 20 sekunder

N0 = 2

def N(t):
    return N0 * ((1/2)**(t/4))

for i in range(3):
    sekunder = i * 10
    print (round(N(sekunder), 3), "gram etter", sekunder, "sekunder")