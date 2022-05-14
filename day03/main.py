from argparse import ArgumentParser
import numpy as np


def parse_input(input):
    with open(input, 'r') as f:
        result = [
            [int(x) for x in line.strip()]
            for line in f
            ]
    return np.asarray(result)


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


def get_oxygen_gen_rating(report):
    n_bits = report.shape[1]
    kept = report

    for idx in range(n_bits):
        size = kept.shape[0]
        if size == 1: break
        sum = np.sum(kept[:, idx])
        bit_to_keep = int(sum >= size / 2)
        loc = np.where(kept[:, idx] == bit_to_keep)
        kept = kept[loc]

    ogr = int(''.join([str(el) for el in kept[0]]), 2)
    return ogr


def get_co2_scrubber_rating(report):
    n_bits = report.shape[1]
    kept = report

    for idx in range(n_bits):
        size = kept.shape[0]
        if size == 1: break
        sum = np.sum(kept[:, idx])
        bit_to_keep = int(sum < size / 2)
        loc = np.where(kept[:, idx] == bit_to_keep)
        kept = kept[loc]

    csr = int(''.join([str(el) for el in kept[0]]), 2)
    return csr


def main(args):
    report = parse_input(args.input)
    gamma = get_gamma(report)
    epsilon = get_epsilon(report)
    pc = gamma * epsilon
    print('Part 1')
    print('Power consumption: {:d}'.format(pc))

    ogr = get_oxygen_gen_rating(report)
    csr = get_co2_scrubber_rating(report)
    lsr = ogr * csr
    print('Part 2')
    print('Life support rating: {:d}'.format(lsr))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()

    main(args)
