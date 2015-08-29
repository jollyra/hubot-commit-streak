import logging

import requests


def input_file(filename):
    """
    Read a file and return list of usernames.

    Assumes one username per line and ignores blank lines.
    """
    with open(filename, 'r') as f:
        return list(line.strip() for line in f if line.strip())


def org_members(org_name):
    """
    Query Github API and return list of members from a Github organization.
    """
    if org_name is None:
        org_name = 'pulseenergy'

    url = 'https://github.com/orgs/{}/members'.format(org_name)
    headers = {'Accept': 'application/vnd.github.ironman-preview+json'}
    try:
        r = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        logging.warn('Connection error trying to get org members: [{}]'.format(url))
        return []
    if r.status_code == 404:
        print('Got 404')
        print(r.status_code)
    return []

    print('response')
    print(r.text)
    return r.text


def svg_data(username):
    """
    Returns the contribution streak SVG file contents from Github
    for a specific username.
    """
    url = 'https://github.com/users/{}/contributions'.format(username)
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        logging.warn('Connection error trying to get url: [{}]'.format(url))
        return None

    return r.text

