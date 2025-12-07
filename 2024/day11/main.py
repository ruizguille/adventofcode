from functools import cache
from collections import defaultdict

data = open('input.txt').read()

@cache
def blink(s):
    if s == 0:
        return [1]
    s_str = str(s)
    if len(s_str) % 2 == 0:
        mid = len(s_str) // 2
        return [int(s_str[:mid]), int(s_str[mid:])]
    return [s * 2024]

initial_stones = list(map(int, data.split()))
stones_freq = defaultdict(int)  # dict with default value of 0
for s in initial_stones:
    stones_freq[s] += 1

# Track unique stone frequencies and only transform each unique stone once per iteration
for i in range(75):
    new_stones_freq = defaultdict(int)
    for stone, freq in stones_freq.items():
        for s in blink(stone):
            new_stones_freq[s] += freq
    stones_freq = new_stones_freq
    if i == 24:
        print('Answer 1:', sum(stones_freq.values()))

print('Answer 2:', sum(stones_freq.values()))