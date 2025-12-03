from functools import cache
import sys


@cache
def best(line, digits, start):
    if digits < 0:
        return 0
    mult = 10 ** digits
    return max(int(line[i]) * mult + best(line, digits - 1, i + 1) for i in range(start, len(line) - digits))


total = 0
input = open(sys.argv[1]).read().splitlines()
for line in input:
    total += best(line, 11, 0)

print(total)
