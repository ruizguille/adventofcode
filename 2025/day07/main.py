from functools import cache

data = open('input.txt').read()
grid = [list(line) for line in data.splitlines()]

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == 'S':
            r0, c0 = r, c

seen = set()
def splits(r, c):
    if r+1 == len(grid) or (r, c) in seen:
        return 0
    seen.add((r, c))
    if grid[r+1][c] == '^':
        return splits(r+1, c-1) + splits(r+1, c+1) + 1
    else:
        return splits(r+1, c)

print('Answer 1:', splits(r0, c0))

@cache
def timelines(r, c):
    if r+1 == len(grid):
        return 1
    if grid[r+1][c] == '^':
        return timelines(r+1, c-1) + timelines(r+1, c+1)
    else:
        return timelines(r+1, c)

print('Answer 2:', timelines(r0, c0))