from collections import defaultdict
from queue import Queue
import sys

graph = defaultdict(lambda: [])
ps = defaultdict(lambda: [])
input = open(sys.argv[1]).read().splitlines()
for line in input:
    node, rest = line.split(":")
    for n in rest.split():
        graph[node].append(n)
        ps[n].append(node)

# Assuming acyclic
start = "svr"

# Check cycles and reachability.
# visited = defaultdict(lambda: False)
# stack = [start]
# visited[start] = True
# while len(stack) > 0:
#     current = stack.pop()
#     for n in graph[current]:
#         if not visited[n]:
#             visited[n] = True
#             stack.append(n)
#         else:
#             if n in stack:
#                 print("cycle", stack)

# print("v", sum([1 if not visited[n] else 0 for n in graph if len(graph[n]) > 0]))
# no cycles, 0 not reachable

ps2 = defaultdict(lambda: [])
for k in ps:
    ps2[k] += ps[k]

zero = [n for n in graph if len(ps2[n]) == 0]
order = []
while len(zero) > 0:
    node = zero.pop()
    order.append(node)
    for n in graph[node]:
        ps2[n].remove(node)
        if len(ps2[n]) == 0:
            zero.append(n)

key = { node: position for position, node in enumerate(order) }

fft = defaultdict(lambda: False)
dac = defaultdict(lambda: False)
fft["fft"] = True
dac["dac"] = True

q = [start]
while len(q) > 0:
    q.sort(key=lambda x: key[x], reverse=True)
    node = q.pop()

    # Cut connections that will never visit fft/dac.
    if any(fft[n] for n in ps[node]):
        for n in ps[node]:
            if not fft[n]:
                graph[n].remove(node)
        fft[node] = True
    if any(dac[n] for n in ps[node]):
        for n in ps[node]:
            if not dac[n]:
                graph[n].remove(node)
        dac[node] = True

    for n in graph[node]:
        if n not in q:
            q.append(n)


q = [start]
count = defaultdict(lambda: 0)
count[start] = 1
while len(q) > 0:
    q.sort(key=lambda x: key[x], reverse=True)
    node = q.pop()
    for n in graph[node]:
        pc = count[n]
        count[n] += count[node]
        if pc == 0:
            q.append(n)

print(count["out"])
