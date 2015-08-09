import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np


def horizontal_bar(sorted_streaks, sort):
    """
    Render a horizontal bar chart of streaks.

    Values have already been sorted by sort.
    """
    users = [user for user, _ in sorted_streaks][::-1]
    print('users', users)
    streaks = [streak.get(sort) for _, streak in sorted_streaks][::-1]

    non_zero = len([x for x in streaks if x > 0])
    non_zero = max(5, non_zero)

    title = 'Top contributors by {} streak'.format(sort)

    figure = plt.figure()
    y_pos = np.arange(len(users))  # y-location of bars
    print('y_pos', y_pos)
    plt.barh(y_pos, streaks, facecolor='#ff9999', edgecolor='grey', align='center')
    plt.yticks(y_pos, users)
    plt.xlim([0, max(streaks) + 0.5])  # x-limits a bit wider at right
    plt.subplots_adjust(left=0.2)  # Wider left margin
    plt.title(title)

    for format in ('png', 'svg'):
        figure.savefig('temp/top_{}.{}'.format(sort, format), format=format)

