import matplotlib.pyplot as plt
import numpy as np


def horizontal_bar(sorted_streaks, sort):
    """
    Render a horizontal bar chart of streaks.

    Values have already been sorted by sort.
    """
    # Only extract those users & streaks for streaks that are non-zero:
    if not sorted_streaks:
        return
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
    plt.title(title, fontsize=20)
    ax = plt.gca()
    ax.set_frame_on(False)  # Turn off all frame lines
    ax.yaxis.set_ticks_position('none')  # Remove axis ticks
    ax.xaxis.set_visible(False)

    seen = set()
    top_color = (122/255, 226/255, 255/255)  # scale to 0-1
    for count, rect in enumerate(rects[::-1]):  # Start from the top for labels
        width = int(rect.get_width())

        if width not in seen:  # Only print the first label of this value
            xloc = width + 2   # Shift text to right side of right edge
            yloc = rect.get_y() + rect.get_height() / 2  # Center text vertically
            ax.text(xloc, yloc, str(width),
                    horizontalalignment='left', verticalalignment='center')
        seen.add(width)

        scaling = (len(rects) - 1 - count) / (len(rects) - 1)
        new_color = [x * scaling for x in top_color]
        rect.set_color(new_color)  # Scale colour by position

    for format in ('png', 'svg'):
        figure.savefig('temp/top_{}.{}'.format(sort, format), format=format)

