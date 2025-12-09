import sys

rs = []
input = open(sys.argv[1]).read().splitlines()
for line in input:
    rs.append(list(map(int, line.split(","))))

N = len(rs)
max_area = 0
for i in range(N):
    x, y = rs[i]
    for j in range(i + 1, N):
        u, v = rs[j]
        max_area = max(max_area, (abs(x - u) + 1) * (abs(y - v) + 1))

print(max_area)
