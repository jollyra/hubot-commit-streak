import pygal


def horizontal_bar(sorted_streaks, sort_attrib):
    """
    Render a horizontal bar chart of streaks.

    Values have already been sorted by sort_attrib.
    """
    users = [user for user, _ in sorted_streaks][::-1]
    streaks = [getattr(streak, sort_attrib) for _, streak in sorted_streaks][::-1]

    chart = pygal.HorizontalStackedBar(show_y_labels=False,
                                       show_x_labels=False,
                                       show_legend=False,
                                       print_values=True,
                                       print_zeroes=False,
                                       print_labels=True)
    chart.title = 'Top contributors by {} streak'.format(sort_attrib)
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
    chart.render_to_file('top.svg')

