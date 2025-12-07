from operator import add, mul

data = open('input.txt').read()

answer1 = 0
answer2 = 0

def concat(x, y):
    return int(str(x) + str(y))

def is_valid(nums, total, ops):
    if len(nums) == 1:
        return nums[0] == total
    for op in ops:
        subtotal = op(nums[0], nums[1])
        if subtotal <= total and is_valid([subtotal] + nums[2:], total, ops):
            return True
    return False

for line in data.splitlines():
    total, rest = line.split(': ')
    total = int(total)
    nums = [int(x) for x in rest.split()]
    if is_valid(nums, total, (add, mul)):
        answer1 += total
    if is_valid(nums, total, (add, mul, concat)):
        answer2 += total

print('Answer 1:', answer1)
print('Answer 2:', answer2)