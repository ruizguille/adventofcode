data = open('input.txt').read()

grid = []
starts = []
for x, line in enumerate(data.splitlines()):
    row = [int(c) for c in line]
    grid.append(row)
    starts.extend((x, y) for y, c in enumerate(row) if c == 0)
num_rows = len(grid)
num_cols = len(grid[0])

STEPS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def find_peaks(pos, height=0):
    if height == 9:
        return [pos]
    peaks = []
    for s in STEPS:
        next_pos = (pos[0] + s[0], pos[1] + s[1])
        if (
            0 <= next_pos[0] < num_rows and 0 <= next_pos[1] < num_cols 
            and grid[next_pos[0]][next_pos[1]] == height+1
        ):
            peaks += find_peaks(next_pos, height+1)
    return peaks

answer1 = 0
answer2 = 0
for start in starts:
    peaks = find_peaks(start)
    answer1 += len(set(peaks))
    answer2 += len(peaks)

print('Answer 1:', answer1)
print('Answer 2:', answer2)