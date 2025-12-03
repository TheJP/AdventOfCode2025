import sys

total = 0
input = open(sys.argv[1]).read().splitlines()
for line in input:
    total += max(int(line[i] + line[j]) for i in range(len(line)) for j in range(i + 1, len(line)))

print(total)
