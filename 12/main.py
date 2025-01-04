import sys

map = { }

with open(sys.argv[1], "r") as file:
    pos = (0,0)
    for line in file:
        line = line.rstrip("\n")
        for e in line:
            map[pos] = e
            pos = (pos[0] + 1, pos[1])
        pos = (0, pos[1] + 1)

def group(pos):
    plant = map[pos]
    del map[pos]
    plot = [ pos ]
    for prox in [ (pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1) ]:
        if prox in map and map[prox] == plant:
            plot += group(prox)
    return plot

def fence(plot):
    p = 0
    for pos in plot:
        adj = [ (pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1) ]
        int = [ pos for pos in plot if pos in adj ]
        p += 4 - len(int)
    return p

plots = [ ]

while len(map) > 0:
    pos = next(iter(map))
    plots.append(group(pos))

price = 0

for plot in plots:
    price += len(plot) * fence(plot)

print("price:", price)
