import sys

with open(sys.argv[1]) as f:
    crabs = [int(s) for s in f.readline().strip().split(',')]

print(crabs)

x_min = None
fuel_min = None

for x in range(max(crabs)+1):
    fuel = sum([abs(x-i) for i in crabs])
    print(f'{x}: {fuel}')
    if x_min is None or fuel < fuel_min:
        x_min = x
        fuel_min = fuel


print(f'Answer: {fuel_min}')

