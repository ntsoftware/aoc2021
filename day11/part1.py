import sys
from itertools import product, count
from colorama import init, Fore, Back, Style

init()

with open(sys.argv[1]) as f:
    levels = [[int(x) for x in line.strip()] for line in f]

def dump(a):
    col_normal = Style.DIM + Fore.WHITE
    col_flash = Style.BRIGHT + Fore.RED
    for row in a:
        print(''.join([(col_flash if x == 0 else col_normal) + f'{x:2d}' for x in row]))
    print(Style.RESET_ALL)

def step(a):
    # increase
    for x,y in product(range(10), range(10)):
        a[y][x] += 1
    # flash
    n = 0
    while any([a[y][x] > 9 for x,y in product(range(10), range(10))]):
        for x,y in product(range(10), range(10)):
            if a[y][x] > 9:
                a[y][x] = 0
                n += 1
                if x>0 and y>0 and a[y-1][x-1] != 0: a[y-1][x-1] += 1
                if         y>0 and a[y-1][x  ] != 0: a[y-1][x  ] += 1
                if x<9 and y>0 and a[y-1][x+1] != 0: a[y-1][x+1] += 1
                if x>0         and a[y  ][x-1] != 0: a[y  ][x-1] += 1
                if x<9         and a[y  ][x+1] != 0: a[y  ][x+1] += 1
                if x>0 and y<9 and a[y+1][x-1] != 0: a[y+1][x-1] += 1
                if         y<9 and a[y+1][x  ] != 0: a[y+1][x  ] += 1
                if x<9 and y<9 and a[y+1][x+1] != 0: a[y+1][x+1] += 1
    return n

n = 0
for i in range(100):
    print(f'step {i+1}, flashes={n}')
    dump(levels)
    n += step(levels)

print(f'Answer={n}')
