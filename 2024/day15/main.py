from collections import deque

data = open('input.txt').read()

STEPS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

g, moves = data.split('\n\n')
start_grid = []
for y, row in enumerate(g.splitlines()):
    start_grid.append(list(row))
    if '@' in row:
        start_y, start_x = y, row.index('@')
moves = ''.join(moves.splitlines())

# PART 1
grid = [row[:] for row in start_grid]
y, x = start_y, start_x
for m in moves:
    sy, sx = STEPS[m]
    ny, nx = y + sy, x + sx
    if grid[ny][nx] == '#':
        continue
    if grid[ny][nx] == 'O':
        by, bx = ny + sy, nx + sx
        while grid[by][bx] == 'O':
            by += sy
            bx += sx
        if grid[by][bx] == '#':
            continue
        grid[by][bx] = 'O'
    grid[y][x] = '.'
    grid[ny][nx] = '@'
    y, x = ny, nx

Y, X = len(grid), len(grid[0])
answer1 = sum(100*y + x for y in range(Y) for x in range(X) if grid[y][x] == 'O')
print('Answer 1:', answer1)

# PART 2
grid_mapping = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
grid = [[char for c in row for char in grid_mapping[c]] for row in start_grid]
y, x = start_y, start_x * 2
for m in moves:
    sy, sx = STEPS[m]
    ny, nx = y + sy, x + sx
    if grid[ny][nx] == '#':
        continue
    if grid[ny][nx] in ['[', ']']:
        # Push boxes horizontally if no wall
        if sy == 0:
            bx = nx
            while grid[ny][bx] in ['[', ']']:
                bx += 2*sx
            if grid[ny][bx] == '#':
                continue
            if bx > nx:
                grid[ny][nx+1:bx+1] = grid[ny][nx:bx]
            else:
                grid[ny][bx:nx] = grid[ny][bx+1:nx+1]
        # Push boxes vertically if no wall
        else:
            boxes_to_push = []
            can_push = True
            bx = nx if grid[ny][nx] == '[' else nx - 1
            next_boxes = deque([(ny, bx)])
            while can_push and next_boxes:
                by, bx = next_boxes.popleft()
                if (by, bx) in boxes_to_push:
                    continue
                boxes_to_push.append((by, bx))
                next_y = by + sy
                if grid[next_y][bx] == '#' or grid[next_y][bx+1] == '#':
                    can_push = False
                    break
                if grid[next_y][bx] == '[':
                    next_boxes.append((next_y, bx))
                elif grid[next_y][bx] == ']':
                    next_boxes.append((next_y, bx-1))
                if grid[next_y][bx+1] == '[':
                    next_boxes.append((next_y, bx+1))
            if not can_push:
                continue
            for by, bx in reversed(boxes_to_push):
                grid[by+sy][bx:bx+2] = grid[by][bx:bx+2]
                grid[by][bx:bx+2] = ['.', '.']
    grid[y][x] = '.'
    grid[ny][nx] = '@'
    y, x = ny, nx

Y, X = len(grid), len(grid[0])
answer2 = sum(100*y + x for y in range(Y) for x in range(X) if grid[y][x] == '[')
print('Answer 2:', answer2)