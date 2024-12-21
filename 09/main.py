import sys

with open(sys.argv[1], "r") as file:
    map = [ int(x) for x in file.readline().rstrip("\n").strip() ]

print("map:", map)

disk = [ ]
file_id = 0
for dir in range(0, len(map)):
    if dir % 2 == 0:
        content = file_id
        file_id += 1
    else:
        content = "."
    disk += [ content for l in range(0, map[dir]) ]

print("disk:", disk)
print("size:", len(disk))

left = 0
right = len(disk) - 1
while left < right:
    if disk[left] == ".":
        if disk[right] != ".":
            disk[left] = disk[right]
            left += 1
        disk.pop(right)
        right -= 1
    else:
        left += 1

print("disk:", disk)
print("size:", len(disk))

checksum = 0
for pos in range(0, len(disk)):
    if disk[pos] != ".":
        checksum += pos * disk[pos]

print("checksum:", checksum)
