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
    # TODO: Return github org members, not a placeholder
    return ['supermitch', 'Jollyra']


def svg_data(username):
    """
    Returns the contribution streak SVG file contents from Github
    for a specific username.
    """
    url = 'https://github.com/users/{}/contributions'.format(username)
    r = requests.get(url)
    return r.text

