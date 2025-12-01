# import sys
# import re

# input = open(sys.argv[1]).read()
# matches = re.findall("mul\\(([0-9]+),([0-9]+)\\)", input, re.DOTALL)
# print(sum(int(x) * int(y) for (x, y) in matches))

import sys

total = 50
result = 0

input = open(sys.argv[1]).read().splitlines()
for line in input:
    n = int(line[1:])

    while n > 0:
        n -= 1
        if line[0] == 'L':
            total -= 1
        else:
            total += 1

        if total > 99:
            total = 0
        if total < 0:
            total = 99

        if total == 0:
            result += 1

print(result)
