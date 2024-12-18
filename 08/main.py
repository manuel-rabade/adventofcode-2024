import sys

size = { "x": 0, "y": 0 }
antennas = { }

with open(sys.argv[1], "r") as file:
    y = 0
    for line in file:
        line = line.rstrip("\n")
        for x in range(0, len(line)):
            if line[x] == ".":
                continue
            antennas[line[x]] = antennas.get(line[x], [])
            antennas[line[x]].append((x, y))
        size["x"] = len(line)
        y += 1
    size["y"] = y

antinodes = []

def get_antinodes(a, b, size):
    res = []
    d_x = a[0] - b[0]
    d_y = a[1] - b[1]
    c = (a[0] + d_x, a[1] + d_y)
    d = (b[0] - d_x, b[1] - d_y)
    if c[0] >= 0 and c[0] < size["x"] and c[1] >= 0 and c[1] < size["y"]:
        res.append(c)
    if d[0] >= 0 and d[0] < size["x"] and d[1] >= 0 and d[1] < size["y"]:
        res.append(d)
    return res

for freq in antennas.keys():
    pos = antennas[freq]
    for i in range(0, len(pos)):
        for j in range(i + 1, len(pos)):
            for e in get_antinodes(pos[i], pos[j], size):
                if e not in antinodes:
                    antinodes.append(e)

print("antinodes:", len(antinodes))
