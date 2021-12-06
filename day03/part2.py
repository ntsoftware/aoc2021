import math
import sys

with open(sys.argv[1]) as f:
    numbers = [int(line.strip(), 2) for line in f]

print(numbers)

num_bits = math.ceil(math.log(max(numbers), 2))
print(f'num_bits={num_bits}')

def filter_based_on_bit(values, bit):
    list_0 = list(filter(lambda n: (n >> bit) & 1 == 0, values))
    list_1 = list(filter(lambda n: (n >> bit) & 1 == 1, values))
    return (list_0, list_1) if len(list_0) > len(list_1) else (list_1, list_0)

x = list(numbers)
for bit in range(num_bits):
    x, _ = filter_based_on_bit(x, (num_bits-1) - bit)
    if len(x) == 1:
        oxygen = x[0]
        print(f'oxygen={oxygen}')
        break

x = list(numbers)
for bit in range(num_bits):
    _, x = filter_based_on_bit(x, (num_bits-1) - bit)
    if len(x) == 1:
        co2 = x[0]
        print(f'co2={co2}')
        break

print(f'Answer: {oxygen*co2}')
