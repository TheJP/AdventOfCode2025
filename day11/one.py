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
start = "you"

# Check cycles and reachability.
# visited = defaultdict(lambda: False)
# stack = ["you"]
# visited["you"] = True
# while len(stack) > 0:
#     current = stack.pop()
#     for n in graph[current]:
#         if not visited[n]:
#             visited[n] = True
#             stack.append(n)
#         else:
#             if n in stack:
#                 print("cycle", stack)

# print(sum([1 if not visited[n] else 0 for n in graph if len(graph[n]) > 0]))
# no cycles, 481 not reachable

zero = [n for n in graph if len(ps[n]) == 0]
order = []
while len(zero) > 0:
    node = zero.pop()
    order.append(node)
    for n in graph[node]:
        ps[n].remove(node)
        if len(ps[n]) == 0:
            zero.append(n)

# print(order)
key = { node: position for position, node in enumerate(order) }

q = ["you"]
count = defaultdict(lambda: 0)
count["you"] = 1
while len(q) > 0:
    q.sort(key=lambda x: key[x], reverse=True)
    node = q.pop()
    for n in graph[node]:
        pc = count[n]
        count[n] += count[node]
        if pc == 0:
            q.append(n)

print(count["out"])
