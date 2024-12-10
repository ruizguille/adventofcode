data = open('input.txt').read()

l1, l2 = zip(*[map(int, line.split()) for line in data.splitlines()])

answer1 = sum(abs(x1 - x2) for x1, x2 in zip(sorted(l1), sorted(l2)))
print(answer1)

answer2 = sum(x1 * l2.count(x1) for x1 in l1)
print(answer2)