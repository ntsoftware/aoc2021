import sys

sums = None
n = 0

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        n = n + 1
        if not sums:
            sums = [0] * len(line)
        for i, bit in enumerate(line):
            sums[i] += int(bit)

g = map(lambda s: '0' if s < n/2 else '1', sums)
g = int(''.join(g), 2)

e = map(lambda s: '1' if s < n/2 else '0', sums)
e = int(''.join(e), 2)

print(f'gamma={g}')
print(f'epsilon={e}')
print(f'Answer: {g*e}')
