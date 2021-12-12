import sys
from collections import defaultdict

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

def visit(src, path=None, nodes=None):
    if path is None:
        path = []
    if nodes is None:
        nodes = defaultdict(int)
    path.append(src)
    #print(path)
    if src == 'end':
        return 1
    n = 0
    nodes[src] += 1
    for dest in edges[src]:
        if is_big(dest) or nodes[dest] == 0:
            n += visit(dest, path, nodes)
    path.pop()
    nodes[src] -= 1
    return n

n = visit('start')

# test1: 10 paths
# test2: 19 paths
# test3: 226 paths

print(f'Answer: {n}')
