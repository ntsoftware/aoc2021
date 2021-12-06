import sys

p = 0
d = 0

with open(sys.argv[1]) as f:
    for line in f:
        cmd, val = line.split()
        if cmd == 'forward':
            p += int(val)
        elif cmd == 'down':
            d += int(val)
        elif cmd == 'up':
            d -= int(val)
        else:
            print(f'ignored: "{line}"')

print(f'Answer: {p*d}')

