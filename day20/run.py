import sys
from itertools import product
from PIL import Image

def convert_line(line):
    return bytes([1 if c == '#' else 0 for c in line.strip()])

def load(filename):
    with open(filename) as f:
        line = f.readline()
        rules = convert_line(line)
        line = f.readline()
        rows = [convert_line(line) for line in f]
        return rules, rows, 0

def save(filename, rows):
    w = len(rows[0])
    h = len(rows)
    d = b''.join(rows)
    im = Image.new('1', (w,h))
    im.putdata(d)
    im.save(filename)

def count_pixels(rows):
    return sum(b''.join(rows))

def enhance(rules, rows, border):
    w = len(rows[0])
    h = len(rows)
    out = [bytearray(w+2) for _ in range(h+2)]
    for x,y in product(range(w+2), range(h+2)):
        idx = 0
        for i,j in product([-1,0,1], [-1,0,1]):
            if 0 <= x-1+j < w and 0 <= y-1+i < h:
                pixel = rows[y-1+i][x-1+j]
            else:
                pixel = border
            idx = (idx << 1) | pixel
        out[y][x] = rules[idx]
    return out

def enhance_border(rules, border):
    return rules[0] if border == 0 else rules[511]

rules, rows, border = load(sys.argv[1])

for i in range(50):
    rows = enhance(rules, rows, border)
    border = enhance_border(rules, border)
    save(f'step{i+1}.png', rows)
    print(f'after step {i+1}: {count_pixels(rows)}')

