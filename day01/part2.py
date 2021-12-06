import sys

with open(sys.argv[1]) as f:
    d = [int(line) for line in f]

f = [x+y+z for x,y,z in zip(d[:-2], d[1:-1], d[2:])]

n = sum([1 if x > y else 0 for x,y in zip(f[1:], f[:-1])])

print(f'Answer: {n}')
