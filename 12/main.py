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

def segments(plot):
    sides = [ ]
    for pos in plot:
        adj = [ (pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1) ]
        sides += [ pos for pos in adj if pos not in plot ]
    #print("sides:", sides)

    count = 0
    while len(sides) > 0:
        pos = sides.pop()
        #print("-" * 100)
        #print("pos:", pos)
        count +=1
        # horizontal
        if (pos[0] + 1, pos[1]) in sides or (pos[0] - 1, pos[1]) in sides:
            # horizontal positive
            adj = (pos[0] + 1, pos[1])
            while adj in sides:
                #print("remove horizontal positive:", adj)
                sides.remove(adj)
                adj = (adj[0] + 1, adj[1])
            # horizontal negative
            adj = (pos[0] - 1, pos[1])
            while adj in sides:
                #print("remove horizontal negative:", adj)
                sides.remove(adj)
                adj = (adj[0] - 1, adj[1])
        # vertical
        elif (pos[0], pos[1] + 1) in sides or (pos[0], pos[1] - 1) in sides:
            # vertical negative
            adj = (pos[0], pos[1] - 1)
            while adj in sides:
                #print("remove vertical negative:", adj)
                sides.remove(adj)
                adj = (adj[0], adj[1] - 1)
            # vertical positive
            adj = (pos[0], pos[1] + 1)
            while adj in sides:
                #print("remove vertical positive:", adj)
                sides.remove(adj)
                adj = (adj[0], adj[1] + 1)
        #print("sides:", sides)
    return count

plots = [ ]

while len(map) > 0:
    pos = next(iter(map))
    plots.append(group(pos))

price = 0
price_discount = 0

for plot in plots:
    price += len(plot) * fence(plot)
    price_discount += len(plot) * segments(plot)
    #print("debug:", len(plot), segments(plot))

print("price:", price)
print("price w/discount:", price_discount)
