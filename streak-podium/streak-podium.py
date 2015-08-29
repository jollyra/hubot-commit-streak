#!/usr/bin/env python
import argparse
import collections
import os
import json

import parse
import read
import render


def setup_args():
    """
    Add and return command line arguments.
    """
    parser = argparse.ArgumentParser('Streak Podium')
    parser.add_argument('-f', '--file', help='member list input filename')
    parser.add_argument('-o', '--org', help='organization to sort')
    parser.add_argument('-l', '--limit', type=int, default=5, help='limit number of users')
    return parser.parse_args()


def gather_usernames(args):
    """
    Return username list from chosen input source.
    """
    if args.file:
        return read.input_file('temp/' + args.file)
    elif args.org:
        return read.org_members(args.org)
    else:
        return ['supermitch']  # Some default for now


def main():

    args = setup_args()

    print('Running Streak Podium')
    print('---------------------')

    if os.path.isfile('temp/streaks.json'):
        print('Found json streaks')
        with open('temp/streaks.json', 'r') as f:
            streaks = json.load(f)
    else:
        print('Did not find json streaks')
        kind = 'file' if args.file else 'Github org'
        name = args.file if args.file else args.org
        print('Input is {} [{}]'.format(kind, name))
        print('\tlimiting query to {} users'.format(args.limit))

        print('Gathering usernames...')
        usernames = gather_usernames(args)
        print('\tfound {} usernames'.format(len(usernames)))

        print('Reading streaks...')
        svgs = (read.svg_data(username) for username in usernames[:args.limit])

        commits = (parse.extract_commits(svg) for svg in svgs)
        streaks = {user: parse.find_streaks(x) for user, x in zip(usernames, commits)}
        print('\tfound {} streaks'.format(len(streaks)))


    if not streaks:
        return

    with open('temp/streaks.json', 'w') as f:
        json.dump(streaks, f)

    for sort in ('best', 'latest'):  # Sort by best, then by latest
        sorted_streaks = sorted(streaks.items(), key=lambda t: t[1].get(sort), reverse=True)
        print('\nTop {} streaks:'.format(sort))
        print('============')
        for user, streak in sorted_streaks[:min(len(sorted_streaks), 5)]:  # Top 5
            print('{} - best: {} - latest: {}'.format(user, streak['best'], streak['latest']))
        render.horizontal_bar(sorted_streaks, sort)


if __name__ == '__main__':
    main()

