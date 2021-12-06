import sys

with open(sys.argv[1]) as f:
    d = [int(line) for line in f]

n = sum([1 if x > y else 0 for x,y in zip(d[1:], d[:-1])])

print(f'Answer: {n}')
