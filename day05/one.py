import sys

ranges, xs = open(sys.argv[1]).read().split("\n\n")

fresh = []
for range in ranges.splitlines():
    l, r = range.split("-")
    fresh.append((int(l), int(r)))

total = 0
for x in xs.splitlines():
    x = int(x)
    for l, r in fresh:
        if l <= x <= r:
            total += 1
            break

print(total)
