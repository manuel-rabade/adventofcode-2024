import sys
import re

x_max = int(sys.argv[2])
y_max = int(sys.argv[3])
secs = int(sys.argv[4])

quadrants = [ 0, 0, 0, 0 ]

with open(sys.argv[1], "r") as file:
    for robot in file:
        p_x, p_y, v_x, v_y = [ int(n) for n in re.findall(r"[-\d]+", robot) ]
        x = (p_x + (secs * v_x)) % x_max
        y = (p_y + (secs * v_y)) % y_max
        if x < x_max // 2 and y < y_max // 2:
            quadrants[0] += 1
        elif x > x_max // 2 and y < y_max // 2:
            quadrants[1] += 1
        elif x < x_max // 2 and y > y_max // 2:
            quadrants[2] += 1
        elif x > x_max // 2 and y > y_max // 2:
            quadrants[3] += 1

print("safety factor:", quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
