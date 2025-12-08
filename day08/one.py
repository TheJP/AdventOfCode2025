from queue import PriorityQueue
import sys

# connections = 10  # for example
connections = 1000  # for puzzle input

ds = []
vectors = []
input = open(sys.argv[1]).read().splitlines()
for line in input:
    vectors.append(list(map(int, line.split(","))))

pq = PriorityQueue()
for i in range(len(vectors)):
    x, y, z = vectors[i]
    for j in range(i+1, len(vectors)):
        u, v, w = vectors[j]
        d = (x-u)**2 + (y-v)**2 + (z-w)**2
        pq.put((d, i, j))

clen = [1 for i in range(len(vectors))]
cref = [i for i in range(len(vectors))]
cs = set()
while not pq.empty():
    d, u, v = pq.get()
    cs.add((u, v))

    if cref[u] != cref[v]:
        ru, rv = cref[u], cref[v]
        l = clen[ru] + clen[rv]
        m = min(ru, rv)
        clen[m] = l
        clen[max(ru, rv)] = 0
        for i in range(len(vectors)):
            if cref[i] == ru or cref[i] == rv:
                cref[i] = m

    if len(cs) >= connections:
        break

total = 1
for x in sorted(clen, reverse=True)[:3]:
    total *= x
print(total)
