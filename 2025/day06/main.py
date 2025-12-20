import math

data = open('input.txt').read()

ans1 = 0
for *nums, op in zip(*[line.split() for line in data.splitlines()]):
    nums = map(int, nums)
    ans1 += sum(nums) if op == '+' else math.prod(nums)
print('Answer 1:', ans1)

ans2 = 0
nums = []
op = None
for *col_nums, col_op in list(zip(*data.splitlines())):
    if not any(num.strip() for num in col_nums):
        ans2 += sum(nums) if op == '+' else math.prod(nums)
        nums = []
        continue
    if col_op.strip():
        op = col_op
    nums.append(int(''.join(col_nums)))
ans2 += sum(nums) if op == '+' else math.prod(nums)
print('Answer 2:', ans2)