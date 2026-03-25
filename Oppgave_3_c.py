#Mengde igjen av Rn-219 etter 0, 10 og 20 sekunder

N0 = 2

def N(t):
    return N0 * ((1/2)**(t/4))                      #Funksjon som regner ut mengden som er igjen etter t tid har gått

for i in range(3):                                  #Setter antall perioder den skal kjøre funksjonen
    sekunder = i * 10
    print (round(N(sekunder), 3), "gram etter", sekunder, "sekunder") 