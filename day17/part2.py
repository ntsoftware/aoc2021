import multiprocessing
from itertools import product

xmin,xmax = 124,174
ymin,ymax = -123,-86

#xmin,xmax = 20,30
#ymin,ymax = -10,-5
#answer = 112

def hit_or_miss(v):
    vx, vy = v
    ax = 1 if vx < 0 else -1
    x = 0
    y = 0
    while True:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            print(f'{v[0]},{v[1]}')
            return True
        elif x > xmax or y < ymin:
            return False
        x += vx
        y += vy
        vx += ax if vx != 0 else 0
        vy -= 1

def main():
    with multiprocessing.Pool() as p:
        result = p.map(hit_or_miss, product(range(1,1000), range(-1000, 1000)))

    print(f'Answer: {sum(result)}')

if __name__ == '__main__':
    main()

