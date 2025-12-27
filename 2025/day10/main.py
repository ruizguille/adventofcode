import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

data = open('input.txt').read()

def min_ops_part1(target, buttons):
    n = len(buttons)
    states = [(0, 0)]
    for ops in range(1, n+1):
        next_states = []
        for val, next_idx in states:
            for i in range(next_idx, n):
                next_val = val ^ buttons[i]
                if next_val == target:
                    return ops
                next_states.append((next_val, i + 1))
        states = next_states

ans1 = 0
ans2 = 0
for line in data.splitlines():
    lights_str, *buttons_strs, jolts_str = line.split()
    # Part 1
    target = sum(1 << i for i, c in enumerate(lights_str[1:-1]) if c == '#')
    buttons = [sum(1 << int(p) for p in b[1:-1].split(',')) for b in buttons_strs]
    ans1 += min_ops_part1(target, buttons)
    # Part 2
    jolts = list(map(int, jolts_str[1:-1].split(',')))
    buttons = [[1 if i in map(int, b[1:-1].split(',')) else 0 for i in range(len(jolts))] for b in buttons_strs]
    A = np.array(buttons).T
    b = np.array(jolts)
    n = len(buttons)
    result = milp(
        c=np.ones(n),  # Minimize sum of x
        constraints=LinearConstraint(A, b, b),  # Ax = b
        bounds=Bounds(0, np.inf),  # x >= 0
        integrality=np.ones(n)  # All integers
    )
    if result.success:
        ans2 += int(result.fun)

print('Answer 1:', ans1)
print('Answer 2:', ans2)

