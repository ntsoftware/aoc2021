import sys

with open(sys.argv[1]) as f:
    crabs = [int(s) for s in f.readline().strip().split(',')]

print(crabs)

x_max = max(crabs)

costs = [0]
for x in range(1, x_max+1):
    costs.append(costs[-1] + x)

x_min = None
fuel_min = None

for x in range(x_max+1):
    fuel = sum([costs[abs(x-i)] for i in crabs])
    print(f'{x}: {fuel}')
    if x_min is None or fuel < fuel_min:
        x_min = x
        fuel_min = fuel


print(f'Answer: {fuel_min}')

