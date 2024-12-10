data = open('input.txt').read().splitlines()
rows = len(data)
cols = len(data[0])

# Part 1
answer1 = 0

def count_xmas(line):
    return line.count('XMAS') + line.count('SAMX')

for row in data:
    answer1 += count_xmas(row)

for i in range(cols):
    col = ''.join(row[i] for row in data)
    answer1 += count_xmas(col)

for offset in range(-cols+1, rows):
    diag1 = ''.join(row[i+offset] for i, row in enumerate(data) if 0 <= i+offset < len(row))
    diag2 = ''.join(row[i+offset] for i, row in enumerate(data[::-1]) if 0 <= i+offset < len(row))
    answer1 += count_xmas(diag1) + count_xmas(diag2)

# Part 2
answer2 = 0
for i in range(1, rows-1):
    for j in range(1, cols-1):
        if (
            data[i][j] == 'A'
            and data[i-1][j-1] + data[i+1][j+1] in ['MS', 'SM']
            and data[i-1][j+1] + data[i+1][j-1] in ['MS', 'SM']
        ):
            answer2 += 1

print('Answer 1:', answer1)
print('Answer 2:', answer2)