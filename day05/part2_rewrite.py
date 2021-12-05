import sys
from itertools import chain

lines = []
with open(sys.argv[1]) as f:
    for line in f:
        p1, p2 = line.strip().split(' -> ')
        x1, y1 = map(int, p1.split(','))
        x2, y2 = map(int, p2.split(','))
        lines.append([x1, y1, x2, y2])

w = max([x for x,_,_,_ in lines] + [x for _,_,x,_ in lines]) + 1
h = max([y for _,y,_,_ in lines] + [y for _,_,_,y in lines]) + 1
m = [[0] * w for _ in range(h)]

for x1, y1, x2, y2 in lines:
    if y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2+1):
            m[y1][x] += 1
    elif x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2+1):
            m[y][x1] += 1
    else:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        # point 1 is on the left side
        for i in range(x2 - x1 + 1):
            x = x1 + i
            y = y1 + i if y2 > y1 else y1 - i
            m[y][x] += 1

for row in m:
    print(''.join(['.' if x == 0 else str(x) for x in row]))

n = len([x for x in chain(*m) if x >= 2])
print(f'Answer: {n}')

