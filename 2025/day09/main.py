data = open('input.txt').read()
tiles = [tuple(map(int, line.split(','))) for line in data.splitlines()]

# PART 1
ans1 = max(abs(x1-x2+1) * abs(y1-y2+1) for i, (x1, y1) in enumerate(tiles) for x2, y2 in tiles[i+1:])
print('Answer 1:', ans1)

# PART 2
xs = sorted({x for x, _ in tiles})
ys = sorted({y for _, y in tiles})
x_sizes = [s for i in range(len(xs)) for s in ([xs[i] - xs[i-1] - 1, 1] if i > 0 else [1])]
y_sizes = [s for i in range(len(ys)) for s in ([ys[i] - ys[i-1] - 1, 1] if i > 0 else [1])]

X, Y = 2*len(xs) - 1, 2*len(ys) - 1
grid = [['.' for _ in range(X)] for _ in range(Y)]
proj_tiles = [(xs.index(x) * 2, ys.index(y) * 2) for x, y in tiles]

# Add projected tiles and connections to grid
for i, (x1, y1) in enumerate(proj_tiles):
    grid[y1][x1] = '#'
    x0, y0 = proj_tiles[i-1]
    if x1 == x0:
        step = 1 if y1 >= y0 else -1
        for y in range(y0 + step, y1, step):
            grid[y][x1] = 'X'
    else:
        step = 1 if x1 >= x0 else -1
        for x in range(x0 + step, x1, step):
            grid[y1][x] = 'X'

# Add interior tiles to grid
for y in range(Y):
    last_wall = False
    inside = False
    for x in range(X):
        if grid[y][x] in ('#', 'X'):
            last_wall = True
        else:
            if last_wall:
                inside = not inside
                last_wall = False
            if inside:
                grid[y][x] = 'X'

# Calculate max area of rectangle with all interior tiles of same color
max_area = 0
for i, (x1, y1) in enumerate(proj_tiles):
    for x2, y2 in proj_tiles[i+1:]:
        lo_x, hi_x = min(x1, x2), max(x1, x2)
        lo_y, hi_y = min(y1, y2), max(y1, y2)
        interior = (grid[y][x] for y in range(lo_y + 1, hi_y) for x in range(lo_x + 1, hi_x))
        first = next(interior, None)
        if all(cell == first for cell in interior):
            area = sum(x_sizes[lo_x:hi_x+1]) * sum(y_sizes[lo_y:hi_y+1])
            max_area = max(max_area, area)

print('Answer 2:', max_area)