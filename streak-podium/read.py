import requests


def input_file(filename):
    """
    Return username list, assuming on username per line.
    """
    with open(filename, 'r') as f:
        return list(line.strip() for line in f if line.strip())


def org_members(org_name):
    """
    Return all members from a Github organization.
    """
    # TODO: Return github org members, not a placeholder
    return ['supermitch', 'Jollyra']


def svg_data(username):
    """
    Read username's streak data from Github.
    """
    url = 'https://github.com/users/{}/contributions'.format(username)
    r = requests.get(url)
    return r.text

