import sys

with open(sys.argv[1], "r") as file:
    map = [ int(x) for x in file.readline().rstrip("\n").strip() ]

print("map:", map)

disk = [ ]
files = [ ]
spaces = [ ]
for dir in range(0, len(map)):
    item = { "offset": len(disk), "size": map[dir] }
    if dir % 2 == 0:
        content = len(files)
        files.append(item)
    else:
        content = "."
        spaces.append(item)
    disk += [ content for l in range(0, map[dir]) ]

print("disk:", disk)
print("size:", len(disk))

for i in reversed(range(0, len(files))):
    #print("file: ", files[i])
    for j in range(0, i):
        #print("   space: ", spaces[j])
        if files[i]["size"] > spaces[j]["size"]:
            continue
        #print("     movemos")
        for p in range(0, files[i]["size"]):
            disk[spaces[j]["offset"] + p] = disk[files[i]["offset"] + p]
            disk[files[i]["offset"] + p] = "."
        spaces[j]["offset"] += files[i]["size"]
        spaces[j]["size"] -= files[i]["size"]
        break

print("disk:", disk)
print("size:", len(disk))

checksum = 0
for pos in range(0, len(disk)):
    if disk[pos] != ".":
        checksum += pos * disk[pos]

print("checksum:", checksum)
