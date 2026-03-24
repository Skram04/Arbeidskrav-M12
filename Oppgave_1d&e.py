v = 0
v0 = 150
g = -9.81

def f():
    return v-v0 / g

def y():
    return (v + v0) / 2 * f()

print ("Tid = ", f())
print ("Strekning = ", y())