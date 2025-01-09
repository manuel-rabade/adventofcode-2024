import sys
import re

machines = [ ]

with open(sys.argv[1], "r") as file:
    for block in file.read().split('\n\n'):
        a, b, c = block.splitlines()
        data = { "a": [ int(i) for i in re.findall(r"X\+(\d+), Y\+(\d+)", a)[0] ],
                 "b": [ int(i) for i in re.findall(r"X\+(\d+), Y\+(\d+)", b)[0] ],
                 "c": [ int(i) for i in re.findall(r"X=(\d+), Y=(\d+)", c)[0] ] }
        machines.append(data)

tokens = 0

for m in machines:
    res = [ ]
    for a in range(100):
        for b in range(100):
            if m["a"][0] * a + m["b"][0] * b == m["c"][0] and m["a"][1] * a + m["b"][1] * b == m["c"][1]:
                res.append(3 * a + b)
    if len(res) > 0:
        tokens += min(res)

print("tokens:", tokens)
