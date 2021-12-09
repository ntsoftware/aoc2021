import sys
from itertools import chain

with open(sys.argv[1]) as f:
    rows = [[int(c) for c in row.strip()] for row in f]
h = len(rows)
w = len(rows[0])
heightmap = list(chain(*rows))

def sign(x):
    if x < 0: return -1
    if x > 0: return 1
    return 0

def diff1(a):
    return [sign(a[i+1] - a[i]) for i in range(len(a)-1)]

def diff2(a):
    return [sign(a[i] - a[i+1]) for i in range(len(a)-1)]

gradients = [0] * len(heightmap)

for i in range(h):
    b = w*i
    e = w*(i+1)
    a = heightmap[b:e]
    d1 = diff1([9] + a)
    d2 = diff2(a + [9])
    gradients[b:e] = [x+y+z for x,y,z in zip(gradients[b:e], d1, d2)]

for i in range(w):
    b = i
    e = i+w*(h-1)+1
    a = heightmap[b:e:w]
    d1 = diff1([9] + a)
    d2 = diff2(a + [9])
    gradients[b:e:w] = [x+y+z for x,y,z in zip(gradients[b:e:w], d1, d2)]

lows = [height for height,gradient in zip(heightmap, gradients) if gradient == -4]

print(f'Answer: {sum(lows)+len(lows)}')

