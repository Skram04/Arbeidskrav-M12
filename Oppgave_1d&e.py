def t(v,v0,g):                                  #Funksjon som finner tiden til toppunktet
    return v-v0 / g

def s(v,v0,g):
    return (v + v0) / 2 * t(v,v0,g)             #Funksjon som finner hvor langt opp kula går

print ("Tid = ", t(0, 150, -9.81))
print ("Strekning = ", s(0, 150, -9.81))        