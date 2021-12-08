import sys
from itertools import chain

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

n = len([x for x in chain(*outputs) if len(x) in [2,4,3,7]])
print(f'Answer: {n}')


