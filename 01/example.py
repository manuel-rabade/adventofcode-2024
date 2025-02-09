left = [ ]
right = [ ]

with open("input.txt", "r") as file:
    for line in file:
        a, b = line.strip().split()
        left.append(int(a))
        right.append(int(b))

left.sort()
right.sort()

d = sum([ abs(left[i] - right[i]) for i in range(0, len(left)) ])

print("distance:", d)
