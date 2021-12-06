import sys

with open(sys.argv[1]) as f:
    ages = [int(s) for s in f.readline().strip().split(',')]

N = int(sys.argv[2])

# description of the data model:
# fishes[age] = (number of fishes of this age)
# age   action
# 0     create a new child and reset to 6
# 1-6   alive, decrement
# 8     newborn, decrement

fishes = [0] * 9
for age in ages:
    fishes[age] += 1
print(f'init: {fishes}')

for i in range(N):
    new_fishes = [0] * 9
    for age, num in enumerate(fishes):
        if age == 0:
            new_fishes[6] += num
            new_fishes[8] += num
        else:
            new_fishes[age-1] += num
    fishes = new_fishes
    print(f'gen {i+1}: {fishes}')

print(f'Answer: {sum(fishes)}')
