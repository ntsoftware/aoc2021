import sys
import numpy as np
from itertools import product

def load(filename):
    with open(filename) as f:
        s = []
        for line in f:
            if 'scanner' in line:
                s.append([])
            elif len(line.strip()) != 0:
                s[-1].append(tuple(map(int, line.split(','))))
        return s

def overlap(s1, s2):
    for x1,y1,z1 in s1:
        p1 = np.array([x1,y1,z1])
        d1 = set([(x-x1,y-y1,z-z1) for x,y,z in s1])
        for i,j,k in product([-1,1],[-1,1],[-1,1]):
            for x2,y2,z2 in s2:
                p2 = np.array([x2,y2,z2])
                r1 = np.array([[i,0,0],[0,j,0],[0,0,k]])
                r2 = np.array([[0,j,0],[0,0,k],[i,0,0]])
                r3 = np.array([[0,0,k],[i,0,0],[0,j,0]])
                r4 = np.array([[i,0,0],[0,0,k],[0,j,0]])
                r5 = np.array([[0,0,k],[0,j,0],[i,0,0]])
                r6 = np.array([[0,j,0],[i,0,0],[0,0,k]])
                for m in r1,r2,r3,r4,r5,r6:
                    d2 = set([(x,y,z) for x,y,z in np.matmul(s2-p2, m)])
                    n = len(d1 & d2)
                    if n >= 12:
                        return p1,p2,m

def transform(s, t):
    p,m = t
    return p+np.matmul(s, m)

def find_overlap(s1, scanners):
    for j,s2 in enumerate(scanners):
        if s1 != s2:
            t = overlap(s1, s2)
            if t is not None:
                return j,t

scanners = load(sys.argv[1])

transforms = dict()

for i,s1 in enumerate(scanners):
    j,(p1,p2,m) = find_overlap(s1, scanners)
    t21 = p1-np.matmul(p2,m),m
    transforms[(j,i)] = t21 
    t12 = p2-np.matmul(p1,np.linalg.inv(m)),np.linalg.inv(m)
    transforms[(i,j)] = t12

import pickle
pickle.dump(transforms, open('transforms-test', 'w'))

def find_path(edges, src, dest, visited=None):
    if visited is None:
        visited = []
    if src == dest:
        return [dest]
    else:
        for s,d in edges:
            if s == src and d not in visited:
                p = find_path(edges, d, dest, visited + [s])
                if p is not None:
                    return [s] + p

