import sys

def load(filename):
    dots = set()
    folds = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith('fold along '):
                axis, value = line.lstrip('fold along ').split('=')
                folds.append((axis, int(value)))
            elif line:
                x, y = line.split(',')
                dots.add((int(x), int(y)))
    return dots, folds

def dump(dots):
    w = max([x for x,y in dots]) + 1
    h = max([y for x,y in dots]) + 1
    for y in range(h):
        print(''.join([('#' if (x,y) in dots else '.') for x in range(w)]))

def fold_along_x(dots, i):
    folded = set()
    for x,y in dots:
        if x > i:
            x = 2*i - x
        folded.add((x,y))
    return folded

def fold_along_y(dots, i):
    folded = set()
    for x,y in dots:
        if y > i:
            y = 2*i - y
        folded.add((x,y))
    return folded

dots, folds = load(sys.argv[1])

for i, (axis, value) in enumerate(folds):
    print(f'after {i} folds={len(dots)}')
    if axis == 'x':
        dots = fold_along_x(dots, value)
    elif axis == 'y':
        dots = fold_along_y(dots, value)

dump(dots)
