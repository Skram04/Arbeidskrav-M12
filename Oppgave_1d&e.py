v = 0       #m/s   
v0 = 150    #m/s**2
g = -9.81   #m/s**2

def t():                                  #Funksjon som finner tiden til toppunktet
    return v-v0 / g

def s():
    return (v + v0) / 2 * t()             #Funksjon som finner hvor langt opp kula går

print (f"Det øverste punktet er {s():.1f} meter oppover") 
print (f"Tiden til det øverste punktet er {t():.1f} sekunder")   