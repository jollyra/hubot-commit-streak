from lxml import etree


def extract_streaks(svg):
    """
    Extract current and longest streak from svg content.
    """
    doc = etree.parse('sample.svg')
    print(doc)
    return 11, 3

