import sys

input = []
with open(sys.argv[1], "r") as file:
    for line in file:
        input.append(list(line.rstrip("\n")))

def find_xmas(input):
    return sum([ "".join(l).count("XMAS") + "".join(l).count("SAMX") for l in input ])

res = find_xmas(input)

vertical = [ [ input[y][x] for y in range(len(input)) ] for x in range(len(input)) ]
res += find_xmas(vertical)

s = len(input)
diagonal = [ [ input[x][x] for x in range(s) ], [ input[x][s - x - 1] for x in range(s) ] ]
for i in range(1, s):
    a = []
    b = []
    c = []
    d = []
    for j in range(s - i):
        a.append(input[j][i + j])
        b.append(input[i + j][j])
        c.append(input[j][s - i - j - 1])
        d.append(input[i + j][s - j - 1])
    diagonal.append(a)
    diagonal.append(b)
    diagonal.append(c)
    diagonal.append(d)

res += find_xmas(diagonal)
print("xmas count:", res)
