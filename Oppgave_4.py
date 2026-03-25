fart = [73,69,81,83,64,59,70]
dist = 0

for f in fart:
    print ("f er = ", f)
    print ("fart index er = ", fart.index(f))
    dist += (fart[fart.index(f)]) * 0.25
    print("distanse er = ", dist)
dist += (-1/2 * fart[0] - 1/2 * fart[-1] ) * 0.25               #Fjerner halvparten av første og siste punkt

print ("distanse = ", dist)