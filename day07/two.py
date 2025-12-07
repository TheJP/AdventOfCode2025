from collections import defaultdict
import sys

input = open(sys.argv[1]).read().splitlines()

s = input[0].find("S")
bs = set([s])
c = defaultdict(lambda: 0)
c[s] = 1
for line in input[1:]:
    nbs = set()
    nc = defaultdict(lambda: 0)
    for b in bs:
        if line[b] == ".":
            nbs.add(b)
            nc[b] += c[b]
        elif line[b] == "^":
            nbs.add(b - 1)
            nc[b - 1] += c[b]
            nbs.add(b + 1)
            nc[b + 1] += c[b]

    bs = nbs
    c = nc

print(sum(nc.values()))
