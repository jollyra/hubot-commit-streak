import pygal
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


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

    # Export SVG using pygal
    chart = pygal.HorizontalStackedBar(show_y_labels=False,
                                       show_x_labels=False,
                                       show_legend=False,
                                       print_values=True,
                                       print_zeroes=False,
                                       print_labels=True)
    chart.title = title
    chart.x_labels = users

    values = []
    for value, user in zip(streaks, users):
        if value > 0:
            values.append({
                'value': value,
                'label': user,
                'xlink': 'https://github.com/{}'.format(user)
            })
        else:
            values.append(0)  # Let zeroes be boring
    chart.add('Streaks', values)

    chart.render_to_file('temp/top_{}.svg'.format(sort))

