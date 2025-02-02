from window import Window, Line, Point


def main():
    win = Window(800, 600)
    win.draw_line(
        Line(
            Point(1, 1),
            Point(100, 8)
        ),
        'red'
    )
    win.wait_for_close()


main()