import sys
import re

x_max = int(sys.argv[2])
y_max = int(sys.argv[3])
count = int(sys.argv[4])

robots = [ ]

with open(sys.argv[1], "r") as file:
    for robot in file:
        robots.append([ int(n) for n in re.findall(r"[-\d]+", robot) ])

def pos(robot, secs):
    p_x, p_y, v_x, v_y = robot
    x = (p_x + (secs * v_x)) % x_max
    y = (p_y + (secs * v_y)) % y_max
    return x, y

def see(frame):
    for y in range(y_max):
        for x in range(x_max):
            if (x, y) in frame:
                print(frame.count((x,y)), end="")
            else:
                print(" ", end="")
        print("")

def tip(frame):
    for y in range(y_max):
        for x in range(x_max):
            tip = [ (x, y), (x - 1, y + 1), (x + 1, y + 1), (x - 2, y + 2), (x + 2, y + 2) ]
            if all(robot in frame for robot in tip):
                return True
    return False

for secs in range(count):
    frame = [ pos(robot, secs) for robot in robots ]
    if tip(frame):
        print("seconds:", secs)
        see(frame)
        print("=" * x_max)
