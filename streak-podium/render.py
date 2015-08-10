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

    figure = plt.figure(num=None, figsize=(6, 15))
    y_pos = np.arange(len(users))  # y-location of bars
    print('y_pos', y_pos)
    plt.barh(y_pos, streaks, facecolor='#7AE2FF', edgecolor='#6699FF',
             align='center')
    plt.yticks(y_pos, users)
    plt.xlim([0, max(streaks) + 10])  # x-limits a bit wider at right
    plt.ylim([-1, len(users)])  # tighten y-limits
    plt.subplots_adjust(left=0.25)  # Wider left margin for long usernames
    plt.title(title)
    ax = plt.gca()
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('bottom')

    for format in ('png', 'svg'):
        figure.savefig('temp/top_{}.{}'.format(sort, format), format=format)

