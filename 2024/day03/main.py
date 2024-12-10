import re

data = open('input.txt').read()

answer1 = 0
answer2 = 0

regex = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
enabled = True
for x, y, do, dont in re.findall(regex, data):
    if x and y:
        mul = int(x) * int(y)
        answer1 += mul
        if enabled:
            answer2 += mul
    elif do:
        enabled = True
    elif dont:
        enabled = False

print('Answer 1:', answer1)
print('Answer 2:', answer2)