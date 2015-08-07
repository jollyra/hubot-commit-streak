import pygal


def horizontal_bar(sorted_streaks, sort_attrib):
    """
    Render a horizontal bar chart of streaks.

    Values have already been sorted by sort_attrib.
    """
    users = [user for user, _ in sorted_streaks][::-1]
    values = [getattr(streak, sort_attrib) for _, streak in sorted_streaks][::-1]

    chart = pygal.HorizontalStackedBar(show_legend=False,
                                       print_values=True, print_zeroes=False,
                                       show_y_guides=False, show_x_guides=False)
    chart.title = 'Top contributors by {} streak'.format(sort_attrib)
    chart.x_labels = users
    chart.add('Streaks', values)
    chart.render_to_file('top.svg')

