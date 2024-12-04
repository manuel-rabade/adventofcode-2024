import sys

input = []
with open(sys.argv[1], "r") as file:
    for line in file:
        input.append(list(line.rstrip("\n")))

res = 0
s = len(input)
for x in range(1, s - 1):
    for y in range(1, s - 1):
        if input[x][y] != "A":
            continue
        if input[x-1][y-1] == "M" and input[x+1][y+1] == "S" and input[x-1][y+1] == "M" and input[x+1][y-1] == "S":
            res += 1
        if input[x-1][y-1] == "S" and input[x+1][y+1] == "M" and input[x-1][y+1] == "S" and input[x+1][y-1] == "M":
            res += 1
        if input[x-1][y-1] == "M" and input[x+1][y+1] == "S" and input[x-1][y+1] == "S" and input[x+1][y-1] == "M":
            res += 1
        if input[x-1][y-1] == "S" and input[x+1][y+1] == "M" and input[x-1][y+1] == "M" and input[x+1][y-1] == "S":
            res += 1

print("x-mas count:", res)
