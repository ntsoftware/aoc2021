import sys
from itertools import count

p1 = 7
p2 = 10

s1 = 0
s2 = 0

for i in count():
    # player 1
    x = 1 + (5 + 18*i) % 100
    p1 = 1 + (p1 + x - 1) % 10
    s1 += p1
    print(f'[{i}] Player 1 moves to space {p1}, score {s1}')
    if s1 >= 1000:
        print(f'Answer: {s2*(6*i+3)}')
        sys.exit()

    # player 2
    x = 1 + (14 + 18*i) % 100
    p2 = 1 + (p2 + x - 1) % 10
    s2 += p2
    print(f'[{i}] Player 2 moves to space {p2}, score {s2}')
    if s2 >= 1000:
        print(f'Answer: {s1*(6*i+6)}')
        sys.exit()
