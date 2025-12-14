data = open('input.txt').read()
ranges_block, ings_block = data.split('\n\n')
ranges = [tuple(map(int, r.split('-'))) for r in ranges_block.splitlines()]
ings = map(int, ings_block.splitlines())

ans1 = 0
for ing in ings:
    for r1, r2 in ranges:
        if r1 <= ing <= r2:
            ans1 += 1
            break
print('Answer 1:', ans1)

ans2 = 0
prev = None
for r1, r2 in sorted(ranges):
    if not prev:
        prev = (r1, r2)
    elif r1 <= prev[1]:
        prev = (prev[0], max(prev[1], r2))
    else:
        ans2 += prev[1] - prev[0] + 1
        prev = (r1, r2)
ans2 += prev[1] - prev[0] + 1
print('Answer 2:', ans2)