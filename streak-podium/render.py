import pygal


def horizontal_bar(sorted_streaks, sort):
    """
    Render a horizontal bar chart of streaks.

    Values have already been sorted by sort.
    """
    users = [user for user, _ in sorted_streaks][::-1]
    streaks = [getattr(streak, sort) for _, streak in sorted_streaks][::-1]

    chart = pygal.HorizontalStackedBar(show_y_labels=False,
                                       show_x_labels=False,
                                       show_legend=False,
                                       print_values=True,
                                       print_zeroes=False,
                                       print_labels=True)
    chart.title = 'Top contributors by {} streak'.format(sort)
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

    chart.render_to_file('top_{}.svg'.format(sort))


def output_png():
    from wand.api import library
    import wand.color
    import wand.image

    with open('top_best.svg', 'rb') as svg_file:
        with wand.image.Image(blob=svg_file.read(), format='svg') as image:
            png_image = image.make_blob('png')
        output_filename = 'top_best.png'
        with open(output_filename, 'wb') as out:
            out.write(png_image)
        return

        with wand.image.Image() as image:
            with wand.color.Color('transparent') as background_color:
                library.MagickSetBackgroundColor(image.wand,
                                                 background_color.resource)
            image.read(blob=svg_file.read())
            png_image = image.make_blob('png32')

        output_filename = 'top_best.png'
        with open(output_filename, 'wb') as out:
            out.write(png_image)

