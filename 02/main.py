import sys

matrix = []

with open(sys.argv[1], "r") as file:
    for line in file:
        levels = [ int(x) for x in line.strip().split() ]
        matrix.append(levels)

safe = 0

for level in matrix:
    prev_diff = 0
    this_safe = True
    for i in range(0, len(level) - 1):
        diff = level[i] - level[i + 1]
        if abs(diff) < 1 or abs(diff) > 3:
            this_safe = False
        if (prev_diff > 0 and diff < 0) or (prev_diff < 0 and diff > 0):
            this_safe = False
        prev_diff = diff
    if this_safe:
        safe += 1

print("safe:", safe)
