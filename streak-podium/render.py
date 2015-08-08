import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np


def horizontal_bar(sorted_streaks, sort):
    """
    Render a horizontal bar chart of streaks.

    Values have already been sorted by sort.
    """
    users = [user for user, _ in sorted_streaks][::-1]
    streaks = [getattr(streak, sort) for _, streak in sorted_streaks][::-1]

    title = 'Top contributors by {} streak'.format(sort)

    figure = plt.figure()
    y_pos = np.arange(len(users))  # y-location of bars
    plt.barh(y_pos, streaks, align='center', alpha=0.4)
    plt.yticks(y_pos, users)
    plt.title(title)
    plt.xlim([0, max(streaks) + 0.5])  # x-limits a bit wider at right

    figure.savefig('temp/top_{}.png'.format(sort), format='png')
    figure.savefig('temp/top_{}.svg'.format(sort), format='svg')

