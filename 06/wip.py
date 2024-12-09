import sys

size = {"x": 0, "y": 0}
guard = {"x": 0, "y": 0, "d": None}
obstacules = []

with open(sys.argv[1], "r") as file:
    for line in file:
        line = line.rstrip("\n")
        size["x"] = len(line)
        for e in range(size["x"]):
            if line[e] == "#":
                obstacules.append((e, size["y"]))
            elif line[e] in "^><v":
                guard["x"] = e
                guard["y"] = size["y"]
                guard["d"] = line[e]
        size["y"] += 1
orig = guard.copy()

def is_inside(guard, size):
    if guard["x"] < 0 or guard["y"] < 0:
        return False
    if guard["x"] >= size["x"] or guard["y"] >= size["y"]:
        return False
    return True

def patrol(guard, obstacules):
    x, y = guard["x"], guard["y"]
    if guard["d"] == "^":
        y -= 1
        turn = ">"
    elif guard["d"] == "v":
        y += 1
        turn = "<"
    elif guard["d"] == ">":
        x += 1
        turn = "v"
    elif guard["d"] == "<":
        x -= 1
        turn = "^"
    if (x, y) in obstacules:
        guard["d"] = turn
        return patrol(guard, obstacules)
    else:
        guard["x"] = x
        guard["y"] = y
        return guard

positions = [ ]

while(is_inside(guard, size)):
    pos = (guard["x"],guard["y"])
    if pos not in positions:
        positions.append(pos)
    guard = patrol(guard, obstacules)

print("positions:", len(positions))

new_obstacules = [ ]
for i in range(1, len(positions)):
    obstacule = positions[i]
    print(i, "/", len(positions))
    guard = orig.copy()
    obstacules.append(obstacule)
    # print(obstacules)
    track = [ ]
    while(is_inside(guard, size)):
        track.append(guard.copy())
        if len(track) > i and track[i - 1] == guard:
            print("loop!")
            new_obstacules.append(obstacule)
            break
        guard = patrol(guard, obstacules)
    # print(track)
    # print("-"*50)
    obstacules.pop()

print("new obstacules:", len(new_obstacules))
# print(new_obstacules)