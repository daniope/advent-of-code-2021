from argparse import ArgumentParser
import numpy as np


def parse_lines(lines):
    called = np.asarray([int(n) for n in lines[0].split(',')])

    bs_lines = lines[1:]
    bs_n = int(len(bs_lines) / 6)

    bs = []
    for _ in range(bs_n):
        curr, bs_lines = bs_lines[1:6], bs_lines[6:]
        ns = parse_board(curr)
        bs.append(Board(ns))

    return called, bs


def parse_board(lines):
    board = np.stack([
        np.array([int(c) for c in line.split()])
        for line in lines
        ])
    return board


class Board(object):
    def __init__(self, numbers):
        self.ns = numbers
        self.status = np.full(self.ns.shape, False)

    def mark(self, x):
        idxs = np.where(self.ns == x)
        self.status[idxs] = True
    
    def check_rows(self):
        rows_status = np.any(np.all(self.status, axis=1))
        return rows_status

    def check_cols(self):
        cols_status = np.any(np.all(self.status, axis=0))
        return cols_status

    def check(self):
        return self.check_cols() or self.check_rows()

    def update(self, x):
        self.mark(x)
        return self.check()

    def unmarked_sum(self):
        us = self.ns[np.logical_not(self.status)]
        return np.sum(us)


def part_1(called, boards):
    for c in called:
        for b in boards:
            if b.update(c): return (b.unmarked_sum() * c)


def main(args):
    with open(args.input, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    called, boards = parse_lines(lines)
    
    print('Part 1')
    print('Answer: {:d}'.format(part_1(called, boards)))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()

    main(args)
