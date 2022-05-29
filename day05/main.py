from argparse import ArgumentParser
from enum import Enum
import numpy as np


class Part(Enum):
    ONE = 1
    TWO = 2


class Diagram():
    def __init__(self, part, shape):
        self.part = part
        self.shape = shape
        self.ns = np.zeros(shape)

    def get_dir(self, x1, x2):
        return -1 if x1 > x2 else 1

    def get_range(self, x1, x2):
        return np.linspace(x1, x2, num=abs(x2-x1)+1, dtype=int)

    def update(self, segment):
        y1, x1 = segment[0]
        y2, x2 = segment[1]
        x_dir = self.get_dir(x1, x2)
        y_dir = self.get_dir(y1, y2)
        x_range = self.get_range(x1, x2)
        y_range = self.get_range(y1, y2)

        if y1 == y2: 
            for x in x_range: self.ns[x, y1] += 1
        elif x1 == x2:
            for y in y_range: self.ns[x1, y] += 1
        elif self.part == Part.TWO:
            for x, y in zip(x_range, y_range): self.ns[x, y] += 1

    def get_sum(self):
        idxs = np.where(self.ns >= 2)
        return len(idxs[0])


def main(args):
    with open(args.input, 'r') as f:
        lines = [line.strip().split(' -> ') for line in f.readlines()]

    segments = [[
        tuple(int(c) for c in coord.split(','))
        for coord in line
        ] for line in lines
        ]

    max_coords = np.max(np.max(segments, axis=0), axis=0)
    shape = (max_coords[0]+1, max_coords[1]+1)

    d1 = Diagram(Part.ONE, shape)
    for s in segments: d1.update(s)
    print('Part 1')
    print('Answer: {:.1f}\n'.format(d1.get_sum()))

    d2 = Diagram(Part.TWO, shape)
    for s in segments: d2.update(s)
    print('Part 2')
    print('Answer: {:.1f}\n'.format(d2.get_sum()))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()

    main(args)
