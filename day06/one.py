import sys

total = 0
cols = []
input = open(sys.argv[1]).read().splitlines()
for line in input:
    if line.startswith("*") or line.startswith("+"):
        for i, x in enumerate(line.split()):
            if x == "+":
                total += sum(cols[i])
            elif x == "*":
                subtotal = 1
                for n in cols[i]:
                    subtotal *= n
                total += subtotal
        break
    for i, x in enumerate(map(int, line.split())):
        if i >= len(cols):
            cols.append([])
        cols[i].append(x)

print(total)
