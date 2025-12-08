data = open('input.txt').read()

ans1 = 0
for line in data.splitlines():
    batts = list(map(int, line))
    max1 = max(batts[:-1])
    max2 = max(batts[batts.index(max1)+1:])
    ans1 += max1*10 + max2
print('Answer 1:', ans1)

ans2 = 0
for line in data.splitlines():
    batts = list(map(int, line))
    max_jolt = 0
    for i in range(11, 0, -1):
        max_i = max(batts[:-i])
        max_jolt = max_jolt*10 + max_i
        batts = batts[batts.index(max_i)+1:]
    max_jolt = max_jolt*10 + max(batts)
    ans2 += max_jolt
print('Answer 2:', ans2)