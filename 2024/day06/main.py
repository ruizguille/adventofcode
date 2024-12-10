data = open('input.txt').read()

STEPS = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}
TURNS = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

grid = data.splitlines()
num_rows = len(grid)
num_cols = len(grid[0])
for x, row in enumerate(grid):
    for y, cell in enumerate(row):
        if cell in ('^', '>', '<', 'v'):
            start_pos, start_dir = (x, y), cell

def run_path(start_pos, start_dir, obst=None):
    x, y = start_pos
    dir = start_dir
    visited = {(x, y, dir)}
    while True:
        step_x, step_y = STEPS[dir]
        next_x, next_y = x + step_x, y + step_y
        if not (0 <= next_x < num_rows and 0 <= next_y < num_cols):
            return visited, False
        if grid[next_x][next_y] == '#' or (next_x, next_y) == obst:
            dir = TURNS[dir]
        else:
            x, y = next_x, next_y
        if (x, y, dir) in visited:
            return visited, True
        visited.add((x, y, dir))

# PART 1
visited, is_loop = run_path(start_pos, start_dir)
visited_positions = {(x, y) for x, y, _ in visited}
answer1 = len(visited_positions)
print('Answer 1:', answer1)

# PART 2
answer2 = 0
# Only need to place obstructions in the visited positions
for pos in visited_positions:
    visited, is_loop = run_path(start_pos, start_dir, obst=pos)
    answer2 += int(is_loop)
print('Answer 2:', answer2)