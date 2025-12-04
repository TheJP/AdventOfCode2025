from collections import defaultdict
import sys

input = open(sys.argv[1]).read().splitlines()

grid = defaultdict(lambda: '#')
for r, row in enumerate(input):
    for c, char in enumerate(row):
        grid[r * 1j + c] = char

h = len(input)
w = len(input[0])

total = 0
has_change = True
while has_change:
    has_change = False
    for y in range(h):
        for x in range(w):
            current = y * 1j + x
            if grid[current] != "@":
                continue

            ns = 0
            for adj in (1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j):
                if grid[current + adj] == "@":
                    ns += 1

            if ns < 4:
                grid[current] = "."
                total += 1
                has_change = True

print(total)
