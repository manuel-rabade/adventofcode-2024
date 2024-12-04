import sys
import re

with open(sys.argv[1], "r") as file:
    mem = file.read()

res = sum([ int(x)*int(y) for x,y in re.findall(r"mul\((\d+),(\d+)\)", mem) ])
print(res)

code = re.findall(r"(mul|do|don't)\((|\d+,\d+)\)", mem)

res = 0
mul_enabled = True
for i in code:
    if i[0] == "do":
        mul_enabled = True
    elif i[0] == "don't":
        mul_enabled = False
    elif i[0] == "mul" and mul_enabled:
        a, b = i[1].split(",")
        res += int(a) * int(b)
print(res)
