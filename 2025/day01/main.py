data = open('input.txt').read()

ans1 = 0
ans2 = 0
dial = 50
for line in data.splitlines():
    turn = int(line[1:]) if line[0] == 'R' else -int(line[1:])
    div, new_dial = divmod(dial + turn, 100)
    if new_dial == 0:
        ans1 += 1
    zeros = abs(div)
    if turn < 0:
        if new_dial == 0:
            zeros += 1
        if dial == 0 and zeros > 0:
            zeros -= 1
    ans2 += zeros
    dial = new_dial

print('Answer 1:', ans1)
print('Answer 2:', ans2)
