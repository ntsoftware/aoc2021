import sys
from itertools import permutations

# 0 abcefg
# 1 cf
# 2 acdeg
# 3 acdfg
# 4 bcdf
# 5 abdfg
# 6 abdefg
# 7 acf
# 8 abcdefg
# 9 abcdfg

# easy digits: the ones that have a unique number of segments
# digit: # of segments
# 1: 2
# 4: 4
# 7: 3
# 8: 7

patterns = []
outputs = []
with open(sys.argv[1]) as f:
    for line in f:
        a,b = line.strip().split(' | ')
        patterns.append(a.split())
        outputs.append(b.split())

def to_digit(segments):
    mapping = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9',
    }
    return mapping[''.join(sorted(segments))]

def get_value(wiring, segments):
    table = str.maketrans(wiring)
    digits = [to_digit(s.translate(table)) for s in segments]
    value = int(''.join(digits))
    return value

def find_wiring(segments):
    for p in permutations('abcdefg'):
        wiring = dict(zip('abcdefg', p))
        try:
            get_value(wiring, segments)
        except:
            continue
        return wiring

wiring = {
    'a': 'c',
    'b': 'f',
    'c': 'g',
    'd': 'a',
    'e': 'b',
    'f': 'd',
    'g': 'e',
}

#patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
#outputs = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']

n = 0

for p,o in zip(patterns, outputs):
    w = find_wiring(p)
    x = get_value(w, o)
    n += x
    print(x)

print(f'Answer: {n}')


