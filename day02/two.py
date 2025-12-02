import sys


def check(n: int) -> bool:
    s = str(n)
    for l in range(1, len(s) // 2 + 1):
        equal = True
        for i in range(l, len(s), l):
            if s[:l] != s[i:i+l]:
                equal = False
                break
        if equal:
            return True
    return False


total = 0
input = open(sys.argv[1]).read().split(",")
for line in input:
    first, last = map(int, line.split("-"))
    total += sum(i for i in range(first, last + 1) if check(i))

print(total)
