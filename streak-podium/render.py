import matplotlib.pyplot as plt
import numpy as np


def horizontal_bar(sorted_streaks, sort):
    """
    Render a horizontal bar chart of streaks.

    Values have already been sorted by sort.
    """
    # Only extract those users & streaks for streaks that are non-zero:
    users, streaks = zip(*[(user, streak.get(sort)) for user, streak
                           in sorted_streaks if streak.get(sort) > 0][::-1])

    title = 'Top Contributors by {} Streak'.format(sort.title())

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

