import sys

rules = {}
updates = []
with open(sys.argv[1], "r") as file:
    for line in file:
        line = line.rstrip("\n")
        if "|" in line:
            a, b = line.split("|")
            rules[a] = rules.get(a, [])
            rules[a].append(b)
        elif "," in line:
            updates.append(line.split(","))

def is_valid(u):
    for i in range(1, len(u)):
        rule = rules.get(u[i])
        if not rule:
            continue
        for j in range(0, i):
            if u[j] in rule:
                return False
    return True

def fix(u):
    for i in range(1, len(u)):
        rule = rules.get(u[i])
        if not rule:
            continue
        for j in range(0, i):
            if u[j] in rule:
                tmp = u[j]
                u[j] = u[i]
                u[i] = tmp
                continue
    return u

print("valid updates sum:", sum(int(u[(len(u)-1)//2]) for u in updates if is_valid(u)))
print("fixed updates sum:", sum(int(u[(len(u)-1)//2]) for u in [ fix(u) for u in updates if not is_valid(u) ]))
