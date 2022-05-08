import numpy as np


def get_number_of_increases(ds):
    return len([
        y - x for x, y in zip(ds, ds[1:])
        if (y - x) > 0
        ])

def main():
    ds = np.loadtxt('input.txt')
    n = get_number_of_increases(ds)
    print('Part 1')
    print('Number of increases: {:d}\n'.format(n))

    window = np.ones(3)
    ds_c = np.convolve(ds, window, mode='valid')
    n = get_number_of_increases(ds_c)
    print('Part 2')
    print('Number of increases: {:d}'.format(n))

if __name__ == '__main__':
    main()
