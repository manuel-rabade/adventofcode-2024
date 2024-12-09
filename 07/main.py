import sys

equations = []

with open(sys.argv[1], "r") as file:
    for line in file:
        line = line.rstrip("\n")
        res, tmp = line.split(":")
        params = [ int(t) for t in tmp.split() ]
        equations.append([ int(res), params ])

def eval(a, p):
    b = p.pop(0)
    x = a + b
    y = a * b
    if len(p) > 0:
        i = eval(x, p.copy())
        j = eval(y, p.copy())
        return i + j
    else:
        return [ x, y ]

total = 0
for e in equations:
    r = e[0]
    p = e[1]
    a = p.pop(0)
    e = eval(a, p.copy())
    if r in e:
        total += r

print("total:", total)
