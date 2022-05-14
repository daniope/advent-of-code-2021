from argparse import ArgumentParser
import numpy as np


def parse_input(input):
    with open(input, 'r') as f:
        result = [
            [int(x) for x in line.strip()]
            for line in f
            ]
    return result


def get_gamma(report):
    half = len(report) / 2
    sums = np.sum(report, axis=0)
    ms = ''.join([str(int(s > half)) for s in sums])
    return int(ms, 2)


def get_epsilon(report):
    half = len(report) / 2
    sums = np.sum(report, axis=0)
    ms = ''.join([str(int(s < half)) for s in sums])
    return int(ms, 2)


def main(args):
    report = parse_input(args.input)
    gamma = get_gamma(report)
    epsilon = get_epsilon(report)
    pc = gamma * epsilon

    print('Part 1')
    print('Power consumption: {:d}'.format(pc))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()

    main(args)
