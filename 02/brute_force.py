import sys

def unsafe_reports(level):
    res = [ ]
    prev_diff = 0
    for i in range(0, len(level) - 1):
        diff = level[i] - level[i + 1]
        if abs(diff) < 1 or abs(diff) > 3:
            res.append(i)
        elif (prev_diff > 0 and diff < 0) or (prev_diff < 0 and diff > 0):
            res.append(i)
        prev_diff = diff
    return res

matrix = []

with open(sys.argv[1], "r") as file:
    for line in file:
        levels = [ int(x) for x in line.strip().split() ]
        matrix.append(levels)

safe_levels = 0
safe_levels_dampener = 0

for level in matrix:
    unsafe = unsafe_reports(level)
    if len(unsafe) < 1:
        safe_levels += 1
    else:
        for i in range(0, len(level)):
            sublevel = level.copy()
            sublevel.pop(i)
            subunsafe = unsafe_reports(sublevel)
            if len(subunsafe) < 1:
                safe_levels_dampener += 1
                # if len(unsafe) > 1:
                #     print(level)
                #     print(unsafe)
                #     print(sublevel)
                #     print("-" * 50)
                # if i != unsafe[0] and i != unsafe[0] + 1:
                #     print(i)
                #     print(level)
                #     print(unsafe)
                #     print(sublevel)
                #     print("-" * 50)
                break

print("safe:", safe_levels)
print("safe w/dampener:", safe_levels + safe_levels_dampener)
