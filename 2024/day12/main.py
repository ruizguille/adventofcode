data = open('input.txt').read()

grid = data.splitlines()
num_rows = len(grid)
num_cols = len(grid[0])

DIRS = [('up', -1, 0), ('right', 0, 1), ('down', 1, 0), ('left', 0, -1)]
SIDE_STEPS = {
    'up': [(0, 1), (0, -1)],
    'down': [(0, 1), (0, -1)],
    'right': [(1, 0), (-1, 0)],
    'left': [(1, 0), (-1, 0)]
}

def find_region(x, y, visited):
    visited.add((x, y))
    area = 1
    plot_sides = []
    for dir, dx, dy in DIRS:
        nx, ny = x + dx, y  + dy
        if 0 <= nx < num_cols and 0 <= ny < num_rows and grid[nx][ny] == grid[x][y]:
            if (nx, ny) not in visited:
                a, ps = find_region(nx, ny, visited)
                area += a
                plot_sides += ps
        else:
            plot_sides.append((x, y, dir))
    return area, plot_sides

def count_sides(plot_sides):
    counted = set()
    sides = 0
    for ps in plot_sides:
        if ps in counted:
            continue
        counted.add(ps)
        x, y, dir = ps
        for dx, dy in SIDE_STEPS[dir]:
            next_ps = (x + dx, y + dy, dir)
            while next_ps in plot_sides:
                counted.add(next_ps)
                next_ps = (next_ps[0] + dx, next_ps[1] + dy, dir)
        sides += 1
    return sides

answer1 = 0
answer2 = 0
visited = set()
for x, row in enumerate(grid):
    for y, c in enumerate(row):
        if (x, y) in visited:
            continue
        area, plot_sides = find_region(x, y, visited)
        answer1 += area * len(plot_sides)
        answer2 += area * count_sides(plot_sides)

print('Answer 1:', answer1)
print('Answer 2:', answer2)