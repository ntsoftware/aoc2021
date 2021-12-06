import sys

p = 0
d = 0
a = 0

with open(sys.argv[1]) as f:
    for line in f:
        cmd, val = line.split()
        v = int(val)
        if cmd == 'forward':
            p += v
            d += a*v
        elif cmd == 'down':
            a += v
        elif cmd == 'up':
            a -= v
        else:
            print(f'ignored: "{line}"')

print(f'Answer: {p*d}')

