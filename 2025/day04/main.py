data = open('input.txt').read()

grid = [list(row) for row in data.splitlines()]
num_rows = len(grid)
num_cols = len(grid[0])

ans1 = 0
ans2 = 0
rolls = []
while True:
    rolls_i = 0
    new_grid = [row[:] for row in grid]
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '@':
                subgrid = [subrow[max(0, c-1):c+2] for subrow in grid[max(0, r-1):r+2]]
                if sum(row.count('@') for row in subgrid) < 5:
                    rolls_i += 1
                    new_grid[r][c] = 'x'
    if rolls_i == 0:
        break
    rolls.append(rolls_i)
    grid = new_grid

print('Answer 1:', rolls[0])
print('Answer 2:', sum(rolls))

    
