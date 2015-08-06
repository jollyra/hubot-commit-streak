from collections import namedtuple

from lxml import etree


def extract_commits(svg):
    """
    Extract current and longest streak from svg content.
    """
    year_of_commits = []
    columns = etree.fromstring(svg).find('g').getchildren()
    for column in columns:
        if column.tag != 'g':  # Ignore last few text entries
            break
        for day in column.getchildren():
            commits = int(day.get('data-count', 0))
            year_of_commits.append(commits)
    return year_of_commits


def _best_streak(year_of_commits):
    """
    Return our longest streak in days, given a yeare of commits.
    """
    best = 0
    streak = 0
    for commits in year_of_commits:
        if commits > 0:
            streak += 1
        else:
            streak = 0
        if streak > best:
            best = streak
    return best


def _latest_streak(year_of_commits):
    """
    Return our most recent streak in days, given a year of commits.
    """
    latest = 0
    for x in year_of_commits[::-1]:
        if x > 0:
            latest += 1
        else:
            return latest


def find_streaks(commits):
    """
    Return a namedtuple of best & latest streaks, given a year of commits.
    """
    Streak = namedtuple('Streak', 'best, latest')
    return Streak(_best_streak(commits), _latest_streak(commits))

