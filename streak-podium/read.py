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
    return ['supermitch']

