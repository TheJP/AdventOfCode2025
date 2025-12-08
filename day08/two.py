from queue import PriorityQueue
import sys

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

maxlen = len(vectors)
clen = [1 for i in range(len(vectors))]
cref = [i for i in range(len(vectors))]
while not pq.empty():
    d, u, v = pq.get()

    if cref[u] != cref[v]:
        ru, rv = cref[u], cref[v]
        l = clen[ru] + clen[rv]
        m = min(ru, rv)
        clen[m] = l
        clen[max(ru, rv)] = 0
        for i in range(len(vectors)):
            if cref[i] == ru or cref[i] == rv:
                cref[i] = m
        if l >= maxlen:
            break

print(vectors[u][0] * vectors[v][0])
