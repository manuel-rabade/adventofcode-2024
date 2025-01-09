import sys
import re

machines = [ ]

with open(sys.argv[1], "r") as file:
    for block in file.read().split('\n\n'):
        a, b, c = block.splitlines()
        data = { "a": [ int(i) for i in re.findall(r"X\+(\d+), Y\+(\d+)", a)[0] ],
                 "b": [ int(i) for i in re.findall(r"X\+(\d+), Y\+(\d+)", b)[0] ],
                 "c": [ 10000000000000 + int(i) for i in re.findall(r"X=(\d+), Y=(\d+)", c)[0] ] }
        machines.append(data)

tokens = 0

for m in machines:
    res = [ ]
    a = (m["c"][0] * m["b"][1] - m["c"][1] * m["b"][0]) // (m["b"][1] * m["a"][0] - m["b"][0] * m["a"][1])
    b = (m["c"][0] * m["a"][1] - m["c"][1] * m["a"][0]) // (m["a"][1] * m["b"][0] - m["b"][1] * m["a"][0])
    if m["a"][0] * a + m["b"][0] * b == m["c"][0] and m["a"][1] * a + m["b"][1] * b == m["c"][1]:
        tokens += 3 * a + b

print("tokens:", tokens)
