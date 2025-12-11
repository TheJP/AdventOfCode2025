from collections import defaultdict
from functools import cache
from queue import Queue
import sys


BIG = 2**60


@cache
def all_nodes(length):
    if length <= 1:
        return [".", "#"]
    nodes = all_nodes(length - 1)
    return [node + "." for node in nodes] + [node + "#" for node in nodes]


def switch(node, toggles):
    return "".join(node[i] if not toggles[i] else ("." if node[i] == "#" else "#") for i in range(len(node)))


total = 0
input = open(sys.argv[1]).read().splitlines()
for line in input:
    target = []
    switches = []
    joltage = []

    for part in line.split():
        inner = part[1:-1]
        match part[0]:
            case "[":
                # target = [light == "#" for light in inner]
                target = inner
            case "(":
                switches.append((*map(int, inner.split(",")),))
            case "{":
                joltage = (*map(int, inner.split(",")),)

    nodes = all_nodes(len(target))

    # Number of edges
    # print(len(nodes) * len(switches))

    # switches[0] = (3,)
    # graph[".##."][0] = ".###"
    graph = defaultdict(lambda: [None] * len(switches))
    for switch_index, s in enumerate(switches):
        toggles = [i in s for i in range(len(target))]
        for node in nodes:
            to = switch(node, toggles)
            graph[node][switch_index] = to

    start = "." * len(target)
    q = Queue()
    q.put(start)
    distance = defaultdict(lambda: BIG)
    distance[start] = 0

    found = False
    while not q.empty() and not found:
        node = q.get()
        for n in graph[node]:
            d = distance[node] + 1
            if d < distance[n]:
                distance[n] = d
                q.put(n)
                if n == target:
                    found = True
                    break

    assert(found)
    total += distance[target]


print(total)
