from argparse import ArgumentParser
from enum import Enum
import numpy as np


class Position:
    def __init__(self):
        self.horizontal = 0
        self.vertical = 0

    def move(self, command):
        a, u = command
        if a == 'forward':
            self.horizontal += u
        elif a == 'up':
            self.vertical -= u
        elif a == 'down':
            self.vertical += u

    def prod(self):
        return self.horizontal * self.vertical

    
def parse_command(line):
    line_s = line.strip()
    aim, units = line_s.split(' ')
    return (aim, int(units))


def parse_input(input):
    with open(input, 'r') as f:
        commands = [parse_command(line) for line in f]
    return commands


def move(position, command):
    a, u = command
    if a == 'forward':
        return [position[0]+u, position[1]]
    elif a == 'up':
        return [position[0], position[1]-u]
    elif a == 'down':
        return [position[0], position[1]+u]
    

def main(args):
    p = Position()

    commands = parse_input(args.input)
    for c in commands: p.move(c)

    print('Part 1')
    print('Result: {:d}'.format(p.prod()))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()

    main(args)
