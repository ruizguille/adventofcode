data = open('input.txt').read()

answer1 = 0
answer2 = 0

def is_safe(nums):
    diffs_set = set([nums[i+1] - nums[i] for i in range(len(nums) - 1)])
    return diffs_set.issubset({1, 2, 3}) or diffs_set.issubset({-1, -2, -3})

for line in data.splitlines():
    nums = list(map(int, line.split()))
    safe = is_safe(nums)
    answer1 += int(safe)
    safe_dampener = safe or any(is_safe(nums[:i] + nums[i+1:]) for i in range(len(nums)))
    answer2 += int(safe_dampener)

print('Answer 1:', answer1)
print('Answer 2:', answer2)