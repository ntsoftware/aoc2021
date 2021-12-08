import sys

N = 80

with open(sys.argv[1]) as f:
    fishes = [int(s) for s in f.readline().strip().split(',')]

print(f'init: {fishes}')

for i in range(N):
    updated = []
    num_new = 0
    for f in fishes:
        if f == 0:
            updated.append(6)
            num_new += 1
        else:
            updated.append(f-1)
    fishes = updated + [8] * num_new
    print(f'gen {i+1}: {fishes}')

print(f'Answer: {len(fishes)}')

