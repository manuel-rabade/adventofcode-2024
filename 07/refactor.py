import sys

equations = []

with open(sys.argv[1], "r") as file:
    for line in file:
        line = line.rstrip("\n")
        res, tmp = line.split(":")
        params = [ int(t) for t in tmp.split() ]
        equations.append([ int(res), params ])

def eval(a, p, r):
    b = p.pop(0)
    x = a + b
    y = a * b
    z = int(str(a) + str(b))
    if len(p) > 0:
        t = []
        if x <= r:
            t += eval(x, p.copy(), r)
        if y <= r:
            t += eval(y, p.copy(), r)
        if z <= r:
            t += eval(z, p.copy(), r)
        return t
    else:
        return [ x, y, z ]

total = 0
for e in equations:
    r = e[0]
    p = e[1]
    a = p.pop(0)
    e = eval(a, p.copy(), r)
    if r in e:
        total += r

print("total:", total)
