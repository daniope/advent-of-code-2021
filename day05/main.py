from argparse import ArgumentParser


def main(args):
    pass


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()

    main(args)
