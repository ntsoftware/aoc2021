import sys
from dataclasses import dataclass


@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_horizontal(self):
        return self.y1 == self.y2

    def is_vertical(self):
        return self.x1 == self.x2


class Canvas(object):

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.data = [0] * (w*h)

    def draw_lines(self, lines):
        for line in lines:
            self.draw(line)

    def draw(self, line):
        if line.is_horizontal():
            self.draw_h(line)
        elif line.is_vertical():
            self.draw_v(line)
        else:
            pass

    def draw_h(self, line):
        x1 = min(line.x1, line.x2)
        x2 = max(line.x1, line.x2)
        for x in range(x1, x2+1):
            self.data[x + line.y1*self.w] += 1

    def draw_v(self, line):
        y1 = min(line.y1, line.y2)
        y2 = max(line.y1, line.y2)
        for y in range(y1, y2+1):
            self.data[line.x1 + y*self.w] += 1

    def dump(self):
        for i in range(self.h):
            row = self.data[i*self.w:(i+1)*self.w]
            print(''.join(['.' if x == 0 else str(x) for x in row]))

    def count_dangerous_areas(self):
        return len([x for x in self.data if x >= 2])


def load(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            p1, p2 = line.strip().split(' -> ')
            x1, y1 = map(int, p1.split(','))
            x2, y2 = map(int, p2.split(','))
            lines.append(Line(x1, y1, x2, y2))
    return lines


def get_width(lines):
    xs = []
    xs.extend([line.x1 for line in lines])
    xs.extend([line.x2 for line in lines])
    return max(xs) + 1


def get_height(lines):
    ys = []
    ys.extend([line.y1 for line in lines])
    ys.extend([line.y2 for line in lines])
    return max(ys) + 1


def main():
    lines = load(sys.argv[1])
    w = get_width(lines)
    h = get_height(lines)
    canvas = Canvas(w, h)
    canvas.draw_lines(lines)
    canvas.dump()
    print(f'Answer: {canvas.count_dangerous_areas()}')


if __name__ == '__main__':
    main()


