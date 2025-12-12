import sys

DIM = 3

presents, problems = open(sys.argv[1]).read().rsplit("\n\n", maxsplit=1)
presents = [present.splitlines()[1:] for present in presents.split("\n\n")]
presents = [[[cell == "#" for cell in row] for row in present] for present in presents]

def to_string(box):
    return "\n".join("".join("#" if cell else "." for cell in row) for row in box)

def pp(box):
    print(to_string(box))

def flip(box):
    return [list(reversed(line)) for line in box]

def rotate(box):
    cells = [(y, -(x-1) + 1) for y, row in enumerate(box) for x, cell in enumerate(row) if cell]
    result = [[False] * 3 for _ in range(3)]
    for x, y in cells:
        result[y][x] = True
    return result

boxes = []
for present in presents:
    b = []
    variations = set()

    for _ in range(2):
        for _ in range(4):
            present = rotate(present)
            s = to_string(present)
            if s not in variations:
                b.append(present)
                variations.add(s)
        present = flip(present)

    boxes.append(b)

flats = [[[(x, y) for y, row in enumerate(box) for x, cell in enumerate(row) if cell] for box in bs] for bs in boxes]


w, h = 0, 0
grid = []
counts = []
def solve(c):
    global w, h, grid, counts

    if c >= len(counts):
        return True
    if counts[c] == 0:
        return solve(c + 1)

    counts[c] -= 1

    for y in range(h-DIM+1):
        for x in range(w-DIM+1):
            for flat in flats[c]:
                if any(grid[y + dy][x + dx] for (dx, dy) in flat):
                    continue

                for (dx, dy) in flat:
                    grid[y + dy][x + dx] = True
                if solve(c):
                    return True
                for (dx, dy) in flat:
                    grid[y + dy][x + dx] = False

    counts[c] += 1
    return False


total = 0
for line in problems.splitlines():
    print(line, file=sys.stderr)
    dim, counts = line.split(":")
    w, h = map(int, dim.split("x"))
    counts = [*(map(int, counts.split()))]
    blocks = sum(len(flats[c][0]) * count for c, count in enumerate(counts))
    if blocks > w * h:
        continue

    grid = [[False for _ in range(w)] for _ in range(h)]
    if solve(0):
        total += 1

print(total)
