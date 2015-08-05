import argparse

import read


def setup_args():
    """
    Add and return command line arguments.
    """
    parser = argparse.ArgumentParser('Streak Podium')
    parser.add_argument('-f', '--file', help='member list input filename')
    parser.add_argument('-o', '--org', help='organization to sort')
    return parser.parse_args()


def gather_usernames(args):
    """
    Return username list from chosen input source.
    """
    if args.file:
        return read.input_file(args.file)
    elif args.org:
        return read.org_members(args.org)
    else:
        return ['supermitch']  # Some default for now


def main():
    print('Running Streak Podium')
    args = setup_args()

    usernames = gather_usernames(args)
    print('Usernames: {}'.format(usernames))


if __name__ == '__main__':
    main()

