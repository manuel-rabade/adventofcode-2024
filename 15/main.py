import sys

with open(sys.argv[1], "r") as file:
    map, moves = file.read().split("\n\n")

map = [ list(line) for line in map.split() ]

def draw(map):
    for line in map:
        print("".join(line))

for y in range(len(map)):
    if "@" in map[y]:
        robot = { "x": map[y].index("@"), "y": y }

codes = { '^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0) }

for move in moves.replace("\n", ""):
    # next robot position
    x, y = robot["x"] + codes[move][0], robot["y"] + codes[move][1]

    # can the robot move?
    while map[y][x] == "O":
        x, y = x + codes[move][0], y + codes[move][1]
    if map[y][x] != ".":
        continue

    # move robot
    map[robot["y"]][robot["x"]] = "."
    robot = { "x": robot["x"] + codes[move][0], "y": robot["y"] + codes[move][1] }

    # move boxes
    x, y = robot["x"], robot["y"]
    if map[y][x] == "O":
        while map[y][x] == "O":
            x, y = x + codes[move][0], y + codes[move][1]
        map[y][x] = "O"

    # update robot in map
    map[robot["y"]][robot["x"]] = "@"

draw(map)
res = sum([ 100 * y + x for y, row in enumerate(map) for x, e in enumerate(row) if e == "O" ])
print("gps coordinates sum:", res)
