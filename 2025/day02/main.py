data = open('input.txt').read()

def invalid_p1(x):
    s = str(x)
    div, mod = divmod(len(s), 2)
    return mod == 0 and s[:div] * 2 == s

def invalid_p2(x):
    s = str(x)
    for d in range(1, len(s)//2 + 1):
        div, mod = divmod(len(s), d)
        if mod == 0 and s[:d] * div == s:
            return True
    return False

ans1 = 0
ans2 = 0
for r in data.split(','):
    fid, lid = map(int, r.split('-'))
    for x in range(fid, lid + 1):
        if invalid_p1(x):
            ans1 += x
        if invalid_p2(x):
            ans2 += x

print('Answer 1:', ans1)
print('Answer 2:', ans2)