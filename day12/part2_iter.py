import sys
from collections import defaultdict, deque

with open(sys.argv[1]) as f:
    edges = defaultdict(list)
    for line in f:
        src, dest = line.strip().split('-')
        edges[src].append(dest)
        edges[dest].append(src)

for src,dests in edges.items():
    print(f'{src:6s} -> {",".join(dests)}')

is_small = lambda x: x.islower() # visit at most once
is_big = lambda x: x.isupper() # visit any number of times

num_paths = 0

stack = [['start']]

while stack:
    path = stack.pop()
    tail = path[-1]
    if tail == 'end':
        num_paths += 1
        #print(path)
    else:
        k = 1 if 2 in [path.count(n) for n in path if is_small(n)] else 2
        stack.extend([path + [n] for n in edges[tail] if n != 'start' and (is_big(n) or path.count(n) < k)])

# test1: 36 paths
# test2: 103 paths
# test3: 3509 paths

print(f'Answer: {num_paths}')
