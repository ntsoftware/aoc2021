import sys
from itertools import product, chain
from math import prod
import matplotlib.pyplot as plt

with open(sys.argv[1]) as f:
    rows = [[int(c) for c in row.strip()] for row in f]
h = len(rows)
w = len(rows[0])

def sign(x):
    if x < 0: return -1
    if x > 0: return 1
    return 0

def diff1(a):
    return [sign(a[i+1] - a[i]) for i in range(len(a)-1)]

def diff2(a):
    return [sign(a[i] - a[i+1]) for i in range(len(a)-1)]

grad_l = [[0]*w for _ in range(h)]
grad_r = [[0]*w for _ in range(h)]
grad_u = [[0]*w for _ in range(h)]
grad_d = [[0]*w for _ in range(h)]

for y in range(h):
    a = [9] + rows[y] + [9]
    for x in range(w):
        grad_l[y][x] = sign(a[x+1] - a[x])
        grad_r[y][x] = sign(a[x+1] - a[x+2])

for x in range(w):
    a = [9] + [rows[y][x] for y in range(h)] + [9]
    for y in range(h):
        grad_u[y][x] = sign(a[y+1] - a[y])
        grad_d[y][x] = sign(a[y+1] - a[y+2])

lows = [(x,y) for x,y in product(range(w), range(h))
    if grad_l[y][x] == -1 and
        grad_r[y][x] == -1 and
        grad_u[y][x] == -1 and
        grad_d[y][x] == -1]
print(lows)

def dump(a):
    for y in range(h):
        print(' '.join([f'{a[y][x]:2d}' for x in range(w)]))

#print('grad_l'); dump(grad_l)
#print('grad_r'); dump(grad_r)
#print('grad_u'); dump(grad_u)
#print('grad_d'); dump(grad_d)

print(f'risk={sum([rows[y][x] for x,y in lows])+len(lows)}')

#plt.imshow(paint)
#plt.show()

marks = [[0]*w for _ in range(h)]

def visit(x, y):
    if marks[y][x] == 1 or rows[y][x] == 9:
        return 0
    marks[y][x] = 1
    size = 1
    if x > 0: size += visit(x-1, y)
    if x < w-1: size += visit(x+1, y)
    if y > 0: size += visit(x, y-1)
    if y < h-1: size += visit(x, y+1)
    return size

sizes = sorted([visit(x, y) for x,y in lows], reverse=True)
print(sizes)

print(f'Answer={prod(sizes[:3])}')

