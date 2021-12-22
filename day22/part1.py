import re
import sys
from itertools import product

cubes = set()

with open(sys.argv[1]) as f:
    for line in f:
        m = re.match(r'(\w+) x=([-\d]+)..([-\d]+),y=([-\d]+)..([-\d]+),z=([-\d]+)..([-\d]+)', line.strip())
        xmin = max(-50, int(m.group(2)))
        xmax = min(50, int(m.group(3)))
        ymin = max(-50, int(m.group(4)))
        ymax = min(50, int(m.group(5)))
        zmin = max(-50, int(m.group(6)))
        zmax = min(50, int(m.group(7)))
        cuboid = {(x,y,z) for x,y,z in product(range(xmin, xmax+1), range(ymin, ymax+1), range(zmin, zmax+1))}
        if m.group(1) == 'on':
            cubes |= cuboid
        else:
            cubes -= cuboid

print(f'Answer: {len(cubes)}')



