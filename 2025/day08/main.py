import math
from collections import defaultdict

data = open('input.txt').read()
boxes = [tuple(map(int, line.split(','))) for line in data.splitlines()]
d_pairs = []
for i, (x1, y1, z1) in enumerate(boxes):
    for j, (x2, y2, z2) in enumerate(boxes):
        if j > i:
            d = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
            d_pairs.append((d, i, j))

circuits = [-1] * len(boxes)
next_circuit = 0
for idx, (d, i, j) in enumerate(sorted(d_pairs)):
    if circuits[i] == -1 and circuits[j] == -1:
        circuits[i] = circuits[j] = next_circuit
        next_circuit += 1
    elif circuits[i] == -1:
        circuits[i] = circuits[j]
    elif circuits[j] == -1:
        circuits[j] = circuits[i]
    elif circuits[i] != circuits[j]:
        old_c = circuits[j]
        new_c = circuits[i]
        circuits = [c if c != old_c  else new_c for c in circuits]
    if idx == 999:
        counts = defaultdict(int)
        for c in circuits:
            if c != -1:
                counts[c] += 1
        ans1 = math.prod(sorted(counts.values(), reverse=True)[:3])
    if len(set(circuits)) == 1:
        ans2 = boxes[i][0] * boxes[j][0]
        break

print('Answer 1:', ans1)
print('Answer 2:', ans2)