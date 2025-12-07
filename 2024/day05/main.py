from collections import defaultdict

data = open('input.txt').read()
rules, updates = data.split('\n\n')

answer1 = 0
answer2 = 0

lower = defaultdict(set)
for rule in rules.splitlines():
    x, y = map(int, rule.split('|'))
    lower[y].add(x)

for update in updates.splitlines():
    nums = [int(x) for x in update.split(',')]
    n = len(nums)
    if not any(
        any(num in lower[nums[i]] for num in nums[i+1:])
        for i in range(n - 1)
    ):
        answer1 += nums[(n-1)//2]
    else:
        # Bubble sort
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j+1] in lower[nums[j]]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        answer2 += nums[(n-1)//2]

print('Answer 1:', answer1)
print('Answer 2:', answer2)