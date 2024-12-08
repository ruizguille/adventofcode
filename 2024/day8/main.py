from collections import defaultdict

data = open('input.txt').read()
lines = data.splitlines()
num_rows = len(lines)
num_cols = len(lines[0])
freq_map = defaultdict(list)
for i, line in enumerate(lines):
    for j, cell in enumerate(line):
        if cell != '.':
            freq_map[cell].append((i, j))

def get_antinode(ant, delta, n):
    an = (ant[0] + n*delta[0], ant[1] + n*delta[1])
    return an if 0 <= an[0] < num_rows and 0 <= an[1] < num_cols else None

antinodes1 = set()
antinodes2 = set()
for antennas in freq_map.values():
    num_ant = len(antennas)
    if num_ant > 1:
        for i in range(num_ant - 1):
            for j in range(i+1, num_ant):
                ant1, ant2 = antennas[i], antennas[j]
                delta = (ant2[0] - ant1[0], ant2[1] - ant1[1])
                # Part 1
                if (an := get_antinode(ant2, delta, n=1)):
                    antinodes1.add(an)
                if (an := get_antinode(ant1, delta, n=-1)):
                    antinodes1.add(an)
                # Part 2
                antinodes2.update((ant1, ant2))
                n = 1
                while (an := get_antinode(ant2, delta, n)):
                    antinodes2.add(an)
                    n += 1
                n = -1
                while (an := get_antinode(ant1, delta, n)):
                    antinodes2.add(an)
                    n -= 1

print('Answer 1:', len(antinodes1))
print('Answer 2:', len(antinodes2))