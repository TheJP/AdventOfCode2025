import sys


def check(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    return s[:len(s) // 2] == s[len(s) // 2:]


total = 0
input = open(sys.argv[1]).read().split(",")
for line in input:
    first, last = map(int, line.split("-"))
    for i in range(first, last + 1):
        if check(i):
            total += i

print(total)
