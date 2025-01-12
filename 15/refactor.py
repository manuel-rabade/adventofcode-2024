import sys

with open(sys.argv[1], "r") as file:
    map, moves = file.read().split("\n\n")

map = map.split()

for i in range(len(map)):
    line = map[i]
    line = line.replace("#", "##")
    line = line.replace("O", "[]")
    line = line.replace(".", "..")
    line = line.replace("@", "@.")
    map[i] = list(line)

def draw(map):
    for line in map:
        print("".join(line))

for y in range(len(map)):
    if "@" in map[y]:
        robot = { "x": map[y].index("@"), "y": y }

codes = { '^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0) }

def can_move_box_y(move, y, x1, x2):
    y = y + codes[move][1]
    if x2 < x1:
        x1, x2 = x2, x1

    if map[y][x1] == "." and map[y][x2] == ".":
        return True
    elif map[y][x1] == "[" and map[y][x2] == "]":
        return can_move_box_y(move, y, x1, x2)
    elif map[y][x1] == "]" and map[y][x2] == ".":
        return can_move_box_y(move, y, x1 - 1, x1)
    elif map[y][x1] == "." and map[y][x2] == "[":
        return can_move_box_y(move, y, x2, x2 + 1)
    elif map[y][x1] == "]" and map[y][x2] == "[":
        return can_move_box_y(move, y, x1 - 1, x1) and can_move_box_y(move, y, x2, x2 + 1)

    return False

def move_box_y(move, y_orig, x1, x2):
    y = y_orig + codes[move][1]
    if x2 < x1:
        x1, x2 = x2, x1

    # move other boxes
    if map[y][x1] == "[" and map[y][x2] == "]":
        move_box_y(move, y, x1, x2)
    elif map[y][x1] == "]" or map[y][x2] == "[":
        if map[y][x1] == "]":
            move_box_y(move, y, x1 - 1, x1)
        if map[y][x2] == "[":
            move_box_y(move, y, x2, x2 + 1)

    # move this box
    map[y][x1] = "["
    map[y][x2] = "]"
    map[y_orig][x1] = "."
    map[y_orig][x2] = "."


for move in moves.replace("\n", ""):
    # next robot position
    x, y = robot["x"] + codes[move][0], robot["y"] + codes[move][1]

    # can the robot move?
    if move in [">", "<"]:
        while map[y][x] in [ "[", "]" ]:
            x = x + codes[move][0] * 2
        if map[y][x] != ".":
            continue
    elif move in ["^", "v"]:
        if map[y][x] == "[":
            if not can_move_box_y(move, y, x, x + 1):
                continue
        elif map[y][x] == "]":
            if not can_move_box_y(move, y, x - 1, x):
                continue
        else:
            if map[y][x] != ".":
                continue

    # move robot
    map[robot["y"]][robot["x"]] = "."
    robot = { "x": robot["x"] + codes[move][0], "y": robot["y"] + codes[move][1] }

    # move boxes
    x, y = robot["x"], robot["y"]
    if move in [">", "<"]:
        if map[y][x] == "[":
            map[y][x] = "."
            map[y][x + 1] = "["
            map[y][x + 2] = "]"
            x += 3
            while map[y][x] == "]":
                map[y][x] = "["
                map[y][x + 1] = "]"
                x += 2
        elif map[y][x] == "]":
            map[y][x] = "."
            map[y][x - 1] = "]"
            map[y][x - 2] = "["
            x -= 3
            while map[y][x] == "[":
                map[y][x] = "]"
                map[y][x - 1] = "["
                x -= 2
    elif move in ["^", "v"]:
        if map[y][x] == "[":
            move_box_y(move, y, x, x + 1)
        elif map[y][x] == "]":
            move_box_y(move, y, x - 1, x)

    # update robot in map
    map[robot["y"]][robot["x"]] = "@"

draw(map)
res = sum([ 100 * y + x for y, row in enumerate(map) for x, e in enumerate(row) if e == "[" ])
print("gps coordinates sum:", res)
