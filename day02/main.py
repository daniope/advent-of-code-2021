from argparse import ArgumentParser
from enum import Enum
import numpy as np


class Position:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def move_1(self, command):
        m, u = command
        if m == 'forward':
            self.horizontal += u
        elif m == 'up':
            self.depth -= u
        elif m == 'down':
            self.depth += u

    def move_2(self, command):
        m, u = command
        if m == 'forward':
            self.horizontal += u
            self.depth += self.aim * u
        elif m == 'up':
            self.aim -= u
        elif m == 'down':
            self.aim += u

    def prod(self):
        return self.horizontal * self.depth

    
def parse_command(line):
    line_s = line.strip()
    movement, units = line_s.split(' ')
    return (movement, int(units))


def parse_input(input):
    with open(input, 'r') as f:
        commands = [parse_command(line) for line in f]
    return commands


def main(args):
    commands = parse_input(args.input)

    p = Position()
    for c in commands: p.move_1(c)
    print('Part 1')
    print('Result: {:d}'.format(p.prod()))

    p = Position()
    for c in commands: p.move_2(c)
    print('Part 2')
    print('Result: {:d}'.format(p.prod()))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()

    main(args)
