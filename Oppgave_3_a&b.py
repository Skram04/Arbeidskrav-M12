N0 = 100

def N(t):
    return N0 * ((1/2)**(t/5700))                      #Funksjon som finner antall gram t år
                                                    #Halveringstiden 5700 viser at det gjelder Karbon C-14
for i in range(10):
    år = i * 1000
    print (N(år), "Gram etter", år, "år")