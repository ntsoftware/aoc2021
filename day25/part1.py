import sys
from itertools import count
from colorama import Cursor

def load(filename):
    with open(filename) as f:
        return [list(s.strip()) for s in f]

def dump(s):
    for row in s:
        print(''.join(row))

def update_h(s):
    w = len(s[0])
    h = len(s)
    t = [[''] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            a, b, c = s[y][(x-1)%w], s[y][x], s[y][(x+1)%w]
            if a == '>' and b == '.':
                t[y][x] = '>'
            elif b == '>' and c == '.':
                t[y][x] = '.'
            else:
                t[y][x] = b
    return t

def update_v(s):
    w = len(s[0])
    h = len(s)
    t = [[''] * w for _ in range(h)]
    for x in range(w):
        for y in range(h):
            a, b, c = s[(y-1)%h][x], s[y][x], s[(y+1)%h][x]
            if a == 'v' and b == '.':
                t[y][x] = 'v'
            elif b == 'v' and c == '.':
                t[y][x] = '.'
            else:
                t[y][x] = b
    return t

def update(s):
    s = update_h(s)
    s = update_v(s)
    return s

s = load(sys.argv[1])
for i in count():
    s2 = update(s)
    print(f'after {i+1} steps')
#    dump(s2)
    if s2 == s:
        break
    s = s2

