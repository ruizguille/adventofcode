import re

data = open('input.txt').read()
num_rows = 103
num_cols = 101

# PART 1
q1 = q2 = q3 = q4 = 0
robots = []
for line in data.splitlines():
    px, py, vx, vy = [int(num) for num in re.findall(r'-?\d+', line)]
    robots.append((px, py, vx, vy))
    px_100 = (px + vx*100) % num_cols
    py_100 = (py + vy*100) % num_rows
    if py_100 < num_rows // 2:
        if px_100 < num_cols // 2:
            q1 += 1
        elif px_100 > num_cols // 2:
            q2 += 1
    elif py_100 > num_rows // 2:
        if px_100 < num_cols // 2:
            q3 += 1
        elif px_100 > num_cols // 2:
            q4 += 1

answer1 = q1 * q2 * q3 * q4
print('Answer 1:', answer1)

# PART 2
def print_robots(robots):
    grid = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]
    for px, py, _, _ in robots:
        grid[py][px] = '*'
    print('\n'.join(''.join(row) for row in grid))

# To find the christmas tree picture, find the robots arrangement with the lowest safety factor
min_sf = answer1
for t in range(10000):
    q1 = q2 = q3 = q4 = 0
    for i, (px, py, vx, vy) in enumerate(robots):
        px = (px + vx) % num_cols
        py = (py + vy) % num_rows
        robots[i] = (px, py, vx, vy)
        if py < num_rows // 2:
            if px < num_cols // 2:
                q1 += 1
            elif px > num_cols // 2:
                q2 += 1
        elif py > num_rows // 2:
            if px < num_cols // 2:
                q3 += 1
            elif px > num_cols // 2:
                q4 += 1
    sf = q1 * q2 * q3 * q4
    if sf < min_sf:
        answer2 = t
        min_sf = sf
        min_sf_robots = robots.copy()

print_robots(min_sf_robots)
print('Answer 2:', answer2)