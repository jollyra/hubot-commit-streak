import argparse

import parse
import read


def setup_args():
    """
    Add and return command line arguments.
    """
    parser = argparse.ArgumentParser('Streak Podium')
    parser.add_argument('-f', '--file', help='member list input filename')
    parser.add_argument('-o', '--org', help='organization to sort')
    parser.add_argument('-l', '--limit', type=int, help='limit number of users', default=5)
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
    args = setup_args()

    print('Running Streak Podium')
    print('---------------------')

    kind = 'file' if args.file else 'Github org'
    name = args.file if args.file else args.org
    print('Input is {} [{}]'.format(kind, name))
    print('\tlimiting to is {} streaks'.format(args.limit))

    print('Gathering usernames...')
    usernames = gather_usernames(args)
    print('\tfound {} usernames'.format(len(usernames)))

    print('Reading streaks...')
    svgs = (read.svg_data(username) for username in usernames[:args.limit])

    commits = (parse.extract_commits(svg) for svg in svgs)
    streaks = {user: parse.find_streaks(x) for user, x in zip(usernames, commits)}

    print('\tfound {} streaks'.format(len(streaks)))
    print(streaks)


if __name__ == '__main__':
    main()

