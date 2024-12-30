from multiprocessing import Pool

import sys
import time
import psutil

with open(sys.argv[1], "r") as file:
    input = file.readline().rstrip("\n")

stones = [ int(e) for e in input.split() ]
blinks = int(sys.argv[2])
procs = int(sys.argv[3])

def evolve(stones):
    tmp = [ ]
    for s in stones:
        if s == 0:
             tmp.append(1)
        elif len(str(s)) % 2 == 0:
            s = str(s)
            tmp += [ int(s[0:len(s)//2]), int(s[len(s)//2:]) ]
        else:
            tmp.append(s * 2024)
    return tmp

def chunks(data, count):
    size = int(len(data) / count)
    res = [ ]
    for i in range(0, count - 1):
        res.append(data[i * size:(i + 1) * size])
    res.append(data[(count - 1) * size:])
    return res

for b in range(blinks):
    start = time.time()
    if len(stones) < 400:
        stones = evolve(stones)
    else:
        with Pool(procs) as p:
            stones = [ s for chunk in p.map(evolve, chunks(stones, procs)) for s in chunk ]
    end = time.time()
    print("blink:", b + 1, "time:", "{0:0.1f}".format(end - start), "stones:", len(stones), "vms:", "{0:0.1f}".format(psutil.Process().memory_info().vms/pow(1024, 3)))
