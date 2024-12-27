import sys

map = { }

with open(sys.argv[1], "r") as file:
    pos = (0,0)
    for line in file:
        line = line.rstrip("\n")
        for e in line:
            map[pos] = int(e)
            pos = (pos[0] + 1, pos[1])
        pos = (0, pos[1] + 1)

def trail(p):
    peaks = [ ]
    for n in [ (p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1) ]:
        if n in map and map[n] == map[p] + 1:
            if map[n] == 9:
                peaks.append(n)
            else:
                peaks += trail(n)
    return peaks

scores = 0
raitings = 0

for pos in map:
    if map[pos] == 0:
        peaks = trail(pos)
        scores += len(set(peaks))
        raitings += len(peaks)

print("scores:", scores)
print("raitings:", raitings)
