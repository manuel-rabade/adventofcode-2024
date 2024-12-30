import sys
import time
import psutil

with open(sys.argv[1], "r") as file:
    input = file.readline().rstrip("\n")

stones = [ int(e) for e in input.split() ]
blinks = int(sys.argv[2])

for b in range(blinks):
    start = time.time()
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            s = str(stones[i])
            stones[i] = int(s[0:len(s)//2])
            stones.insert(i + 1, int(s[len(s)//2:]))
            i += 1
        else:
            stones[i] *= 2024
        i += 1
    end = time.time()
    print("blink:", b + 1, "time:", "{0:0.1f}".format(end - start), "stones:", len(stones), "vms:", "{0:0.1f}".format(psutil.Process().memory_info().vms/pow(1024, 3)))
