import sys

ranges, xs = open(sys.argv[1]).read().split("\n\n")

consider = []
for range in ranges.splitlines():
    l, r = map(int, range.split("-"))
    consider.append((l, r))

total = 0
fresh = []
while len(consider) > 0:
    l, r = consider.pop()
    for a, b in fresh:
        if l < a and b < r:
            consider.append((b + 1, r))
            r = a - 1
            continue
        if a <= l <= b:
            l = b + 1
            if l > r:
                break
        if a <= r <= b:
            r = a -1
            if l > r:
                break

    if l <= r:
        fresh.append((l, r))
        total += r - l + 1

print(total)
