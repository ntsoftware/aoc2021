import sys

with open(sys.argv[1]) as f:
    crabs = [int(s) for s in f.readline().strip().split(',')]

print(crabs)

def sign(x):
    if x > 0:
        return +1
    elif x < 0:
        return -1
    else:
        return 0

# sum of triangular numbers from 0..|d| (inclusive)
def get_cost(d):
    n = abs(d)
    return n*(n+1) / 2

def get_cost_prime(d):
    n = abs(d)
    return n + 0.5

def get_fuel(x):
    return sum([get_cost(x-i) for i in crabs])

def get_fuel_prime(x):
    return sum([sign(x-i) * get_cost_prime(abs(x-i)) for i in crabs])

x = (max(crabs)+1) / 2
y = None
i = 0

eta = float(sys.argv[2])

while True:
    y1 = get_fuel(x)
    z1 = get_fuel_prime(x)
    print(f'[{i}] x={x} f={y1} f\'={z1}')
    if y is not None and y1 >= y:
        f = get_fuel(round(x))
        print(f'Answer: {int(f)}')
        break
    x -= eta*z1
    y = y1
    i += 1


