import sys
import time
import psutil

with open(sys.argv[1], "r") as file:
    input = file.readline().rstrip("\n")

stones = [ int(e) for e in input.split() ]
blinks = int(sys.argv[2])

for b in range(blinks):
    start = time.time()
    tmp = [ ]
    for s in stones:
        if s == 0:
             tmp.append(1)
        elif len(str(s)) % 2 == 0:
            s = str(s)
            tmp += [ int(s[0:len(s)//2]), int(s[len(s)//2:]) ]
        else:
            tmp.append(s * 2024)
    stones = tmp
    end = time.time()
    print("blink:", b + 1, "time:", "{0:0.1f}".format(end - start), "stones:", len(stones), "vms:", "{0:0.1f}".format(psutil.Process().memory_info().vms/pow(1024, 3)))
