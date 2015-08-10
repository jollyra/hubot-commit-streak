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
    rects =  plt.barh(y_pos, streaks, facecolor='#7AE2FF', edgecolor='#6699FF',
                      align='center')
    plt.yticks(y_pos, users)
    plt.xlim([0, max(streaks) + 10])  # x-limits a bit wider at right
    plt.ylim([-1, len(users)])  # tighten y-limits
    plt.subplots_adjust(left=0.25)  # Wider left margin for long usernames
    plt.title(title)
    ax = plt.gca()
    ax.set_frame_on(False)  # Turn off all frame lines
    ax.yaxis.set_ticks_position('none')  # Remove axis ticks
    ax.xaxis.set_visible(False)

    for rect in rects:
        width = int(rect.get_width())
        xloc = width + 2   # Shift text to right side of right edge

        yloc = rect.get_y() + rect.get_height() / 2  # Center text vertically
        ax.text(xloc, yloc, str(width),
                horizontalalignment='left', verticalalignment='center',
                color='black')

    for format in ('png', 'svg'):
        figure.savefig('temp/top_{}.{}'.format(sort, format), format=format)

