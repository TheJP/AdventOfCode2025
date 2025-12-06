from collections import defaultdict
import sys

total = 0
input = open(sys.argv[1]).read().splitlines()
cols = len(input[0])

op = "+"
subresult = 0
for x in range(cols):
    if input[-1][x] == "*":
        total += subresult
        subresult = 1
        op = "*"
    elif input[-1][x] == "+":
        total += subresult
        subresult = 0
        op = "+"

    n = ""
    for y in range(len(input) - 1):
        if input[y][x] != " ":
            n += input[y][x]

    if len(n) > 0:
        if op == "+":
            subresult += int(n)
        elif op == "*":
            subresult *= int(n)

print(total + subresult)
