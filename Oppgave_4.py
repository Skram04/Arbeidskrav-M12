fart = [73,69,81,83,64,59,70]
dist = 0

for f in fart:
    dist += f * 0.25        #Et kvarter = 0.25 timer
dist += (-0.5 * fart[0] + 0.5 * fart[-1]) * 0.25

print (dist)