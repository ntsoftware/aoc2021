import sys
import json
import math
from collections import deque
from dataclasses import dataclass

class Node:
    def __init__(self, p):
        self.p = p

    def __repr__(self):
        return f'[{self.l},{self.r}]'

class Leaf(Node):
    def __init__(self, v, p):
        self.v = v
        self.p = p

    def __repr__(self):
        return str(self.v)

is_leaf = lambda a: isinstance(a, Leaf)

def make_graph(a, p=None):
    if isinstance(a, int):
        return Leaf(a, p)
    n = Node(p)
    n.l = make_graph(a[0], n)
    n.r = make_graph(a[1], n)
    return n

def load(filename):
    with open(filename) as f:
        return [make_graph(json.loads(line)) for line in f]

def add(a, b):
    n = Node(b)
    n.l = a
    n.r = b
    a.p = n
    b.p = n
    return n

def magnitude(a):
    if is_leaf(a):
        return a.v
    return 3*magnitude(a.l) + 2*magnitude(a.r)

def explode(a):
    if a.p.l == a:
        n = a
        while n.p is not None and n.p.l == n:
            n = n.p
        if n.p is not None:
            n = n.p.l
            while not is_leaf(n):
                n = n.r
            n.v += a.l.v
        n = a.p.r
        while not is_leaf(n):
            n = n.l
        n.v += a.r.v
        a.p.l = Leaf(0, a.p)
    elif a.p.r == a:
        n = a
        while n.p is not None and n.p.r == n:
            n = n.p
        if n.p is not None:
            n = n.p.r
            while not is_leaf(n):
                n = n.l
            n.v += a.r.v
        n = a.p.l
        while not is_leaf(n):
            n = n.r
        n.v += a.l.v
        a.p.r = Leaf(0, a.p)

def split(a):
    n = Node(a.p)
    n.l = Leaf(math.floor(a.v/2), n)
    n.r = Leaf(math.ceil(a.v/2), n)
    if a.p.l == a:
        a.p.l = n
    elif a.p.r == a:
        a.p.r = n

def reduce(a, d=0):
    if is_leaf(a):
        if a.v >= 10:
            print(f'split {a}')
            split(a)
            return True
        else:
            return False
    if d == 4:
        print(f'explode {a}')
        explode(a)
        return True
    if reduce(a.l, d+1):
        return True
    if reduce(a.r, d+1):
        return True
    return False

numbers = load(sys.argv[1])

a = make_graph([1,2])
b = make_graph([[3,4],5])

assert(repr(a) == '[1,2]')
assert(repr(b) == '[[3,4],5]')

assert(repr(add(a,b)) == '[[1,2],[[3,4],5]]')

assert(magnitude(make_graph([[1,2],[[3,4],5]])) == 143)
assert(magnitude(make_graph([[[[0,7],4],[[7,8],[6,0]]],[8,1]])) == 1384)
assert(magnitude(make_graph([[[[1,1],[2,2]],[3,3]],[4,4]])) == 445)
assert(magnitude(make_graph([[[[3,0],[5,3]],[4,4]],[5,5]])) == 791)
assert(magnitude(make_graph([[[[5,0],[7,4]],[5,5]],[6,6]])) == 1137)
assert(magnitude(make_graph([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])) == 3488)

a = make_graph([[[[[9,8],1],2],3],4])
n = a.l.l.l.l
print('---')
print(n)
print(a)
explode(n)
print(a)

a = make_graph([7,[6,[5,[4,[3,2]]]]])
n = a.r.r.r.r
print('---')
print(n)
print(a)
explode(n)
print(a)

a = make_graph([[6,[5,[4,[3,2]]]],1])
n = a.l.r.r.r
print('---')
print(n)
print(a)
explode(n)
print(a)

a = make_graph([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
n = a.l.r.r.r
print('---')
print(n)
print(a)
explode(n)
print(a)

a = make_graph([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
n = a.r.r.r.r
print('---')
print(n)
print(a)
explode(n)
print(a)

a = make_graph([[[[0,7],4],[[7,8],[0,13]]],[1,1]])
n = a.l.r.r.r
print(n)
print(a)
split(n)
print(a)

a = make_graph([[[[4,3],4],4],[7,[[8,4],9]]])
b = make_graph([1,1])
c = add(a,b)
print('---')
print(c)
while reduce(c):
    print(c)
