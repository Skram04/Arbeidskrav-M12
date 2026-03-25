def f(v,v0,g):
    return v-v0 / g

def y(v,v0,g):
    return (v + v0) / 2 * f(v,v0,g)

print ("Tid = ", f(0, 150, -9.81))
print ("Strekning = ", y(0, 150, -9.81))