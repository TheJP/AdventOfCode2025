import sys

input = open(sys.argv[1]).read().splitlines()

splits = 0
s = input[0].find("S")
bs = set([s])
for line in input[1:]:
    nbs = set()
    for b in bs:
        if line[b] == ".":
            nbs.add(b)
        elif line[b] == "^":
            nbs.add(b - 1)
            nbs.add(b + 1)
            splits += 1
    bs = nbs

print(splits)
