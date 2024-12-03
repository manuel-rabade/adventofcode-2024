import sys

left = []
right = []

with open(sys.argv[1], "r") as file:
    for line in file:
        a, b = line.strip().split()
        left.append(int(a))
        right.append(int(b))

left.sort()
right.sort()

d = 0
s = 0

for i in range(0, len(left)):
    # distance
    if left[i] > right[i]:
        d += left[i] - right[i]
    elif left[i] < right[i]:
        d += right[i] - left[i]
    # similarity
    s += left[i] * right.count(left[i])

print("distance:", d)
print("similarity:", s)
