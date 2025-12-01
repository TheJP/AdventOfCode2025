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
    if line[0] == 'L':
        total -= int(line[1:])
    else:
        total += int(line[1:])
    while total < 0:
        total += 100
    while total > 99:
        total -= 100
    if total == 0:
        result += 1

print(result)
