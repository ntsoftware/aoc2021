import sys


class Board(object):

    def __init__(self):
        self.values = []
        self.markings = []

    def add_row(self, values):
        self.values.extend(values)
        self.markings.extend([False] * len(values))

    def is_won(self):
        # check rows
        for i in range(5):
            view = self.markings[5*i:5*(i+1)]
            if sum(view) == 5:
                return True
        # check columns
        for i in range(5):
            view = self.markings[i:i+21:5]
            if sum(view) == 5:
                return True

    def mark_number(self, value):
        if value in self.values:
            i = self.values.index(value)
            self.markings[i] = True

    def get_score(self):
        values = [v for v,m in zip(self.values, self.markings) if not m]
        return sum(values)

    def dump(self):
        print('values')
        for i in range(5):
            print(' '.join([f'{x:2d}' for x in self.values[5*i:5*(i+1)]]))
        print('markings')
        for i in range(5):
            print(' '.join([' *' if x else ' .' for x in self.markings[5*i:5*(i+1)]]))


def load_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        lines = [s for s in lines if s]

    numbers = [int(s) for s in lines.pop(0).split(',')]
    print(numbers)

    boards = []
    while lines:
        boards.append(Board())
        for _ in range(5):
            values = [int(s) for s in lines.pop(0).split()]
            boards[-1].add_row(values)
    print(len(boards))

    return numbers, boards


def play(numbers, boards):
    for x in numbers:
        for b in boards:
            b.mark_number(x)
        new_wins = [b for b in boards if b.is_won()]
        if new_wins:
            last_win = new_wins[-1]
            last_number = x
        for b in new_wins:
            boards.remove(b)

    last_win.dump()

    s = last_win.get_score()
    print(f'last board to win has score={s}')
    print(f'Answer: {last_number*s}')


def main():
    play(*load_input(sys.argv[1]))


if __name__ == '__main__':
    main()


