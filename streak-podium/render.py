import pygal


def horizontal_bar(sorted_streaks, sort_attrib):
    """
    Render a horizontal bar chart of streaks.

    Values have already been sorted by sort_attrib.
    """
    users = [user for user, _ in sorted_streaks]
    values = [getattr(streak, sort_attrib) for _, streak in sorted_streaks]
    print(users, values)

    chart = pygal.HorizontalStackedBar()
    chart.title = 'Top {} Streaks'.format(sort_attrib)
    chart.x_labels = users
    chart.add('Streaks', values)
    chart.render_to_file('top.svg')
