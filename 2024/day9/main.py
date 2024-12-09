from collections import deque

data = open('input.txt').read().strip()

blocks = deque([])
files = {}
space = []
file_id = 0
pos = 0
for i, b in enumerate(data):
    size = int(b)
    if i % 2 == 0:
        blocks.extend([file_id] * size)
        files[file_id] = (pos, size)
        file_id += 1
    else:
        blocks.extend([None] * size)
        space.append((pos, size))
    pos += size

# PART 1
answer1 = 0
pos = 0
while blocks:
    b = blocks.popleft()
    while blocks and b is None:
        b = blocks.pop()
    if b is not None:
        answer1 += pos * b
        pos += 1

print('Answer 1:', answer1)

# PART 2
answer2 = 0
for f_id in reversed(files):
    f_pos, f_size = files[f_id]
    for i, (s_pos, s_size) in enumerate(space):
        if s_pos >= f_pos:
            break
        if s_size >= f_size:
            files[f_id] = (s_pos, f_size)
            if s_size == f_size:
                del space[i]
            else:
                space[i] = (s_pos + f_size, s_size - f_size)
            break

for f_id, (f_pos, f_size) in files.items():
    answer2 += f_id * sum(range(f_pos, f_pos + f_size))

print('Answer 2:', answer2)