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
    elif len(unsafe) == 1:
        level_a = level.copy()
        level_a.pop(unsafe[0])
        level_b = level.copy()
        level_b.pop(unsafe[0] + 1)
        unsafe_a = unsafe_reports(level_a)
        unsafe_b = unsafe_reports(level_b)
        if len(unsafe_a) < 1 or len(unsafe_b) < 1:
            safe_levels_dampener += 1
        elif unsafe[0] > 0:
            level_c = level.copy()
            level_c.pop(unsafe[0] - 1)
            unsafe_c = unsafe_reports(level_c)
            if len(unsafe_c) < 1:
                safe_levels_dampener += 1
    # else:
    #     print(level)
    #     print(unsafe)
    #     print("-" * 50)

print("safe:", safe_levels)
print("safe w/dampener:", safe_levels + safe_levels_dampener)
