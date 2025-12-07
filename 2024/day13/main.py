data = open('input.txt').read()

# 2 linear equations with 2 unknowns
def find_min_tokens(ax, ay, bx, by, px, py):
    ai = (by*px - bx*py) / (by*ax - bx*ay)
    bi = (py - ai*ay) / by
    return 3*int(ai) + int(bi) if int(ai) == ai and int(bi) == bi else 0

answer1 = 0
answer2 = 0
for m in data.split('\n\n'):
    a, b, p = m.splitlines()
    ax, ay = [int(p.split('+')[1]) for p in a.split(', ')]
    bx, by = [int(p.split('+')[1]) for p in b.split(', ')]
    px, py = [int(p.split('=')[1]) for p in p.split(', ')]
    answer1 += find_min_tokens(ax, ay, bx, by, px, py)
    answer2 += find_min_tokens(ax, ay, bx, by, px+10**13, py+10**13)

print('Answer 1:', answer1)
print('Answer 2:', answer2)