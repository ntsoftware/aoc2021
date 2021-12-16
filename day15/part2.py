import sys
from itertools import repeat, product
from colorama import init, Fore, Back, Style, Cursor

init()

get_w = lambda a: len(a[0])
get_h = lambda a: len(a)

def load(filename):
    with open(filename) as f:
        return [[int(d) for d in line.strip()] for line in f]

def enlarge(a):
    w = get_w(a)
    h = get_h(a)
    return [[1 + (a[y%h][x%w] - 1 + (x//w) + (y//h)) % 9 for x in range(5*w)] for y in range(5*h)]

def dump(a, m=None):
    if m is None:
        for row in a:
            print(''.join([f'{x:3d}' for x in row]))
    else:
        state_to_color = {
            0: Fore.RED,
            1: Fore.CYAN,
            2: Fore.WHITE,
            }
        for row_a, row_m in zip(a,m):
            print(''.join([state_to_color[c] + f'{x:3d}' for x,c in zip(row_a,row_m)]) + Fore.RESET)

e = load(sys.argv[1])
e = enlarge(e)
w = get_w(e)
h = get_h(e)

d = [[0]*w for _ in range(h)]
m = [[0]*w for _ in range(h)]
# 0: not in output graph (distance from start=+inf)
# 1: in output graph, not visited
# 2: in output graph, visited

def neighbors(x, y):
    n = []
    if x > 0    and m[y][x-1] != 2: n.append((x-1, y, e[y][x-1]))
    if x < w-1  and m[y][x+1] != 2: n.append((x+1, y, e[y][x+1]))
    if y > 0    and m[y-1][x] != 2: n.append((x, y-1, e[y-1][x]))
    if y < h-1  and m[y+1][x] != 2: n.append((x, y+1, e[y+1][x]))
    return n

def visit(x, y):
    m[y][x] = 2
    for nx, ny, ne in neighbors(x, y):
        if m[ny][nx] == 0:
            d[ny][nx] = d[y][x] + ne
        else:
            d[ny][nx] = min(d[ny][nx], d[y][x] + ne)
        m[ny][nx] = 1

def nearest():
    to_visit = [(x,y) for x,y in product(range(w), range(h)) if m[y][x] == 1]
    to_visit = sorted(to_visit, key=lambda xy: d[xy[1]][xy[0]])
    return to_visit[0]

start = 0, 0
end = w-1, h-1

i = 0
pos = start
while pos != end:
    visit(*pos)
    #dump(d, m)
    #print(Cursor.UP(h+1))
    pos = nearest()
    i += 1
    if i % 100 == 0:
        print(f'Progress {i}/{w*h} ({100*i/(w*h):.1f}%)')

print(f'Answer: {d[h-1][w-1]}')
