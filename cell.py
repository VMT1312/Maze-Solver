from window import Line, Point, Window


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win

    def draw(self, x1, x2, y1, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x1, self.__y1),
                    Point(self.__x1, self.__y2)
                )
            )

        if self.has_right_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x1, self.__y1),
                    Point(self.__x2, self.__y1)
                )
            )

        if self.has_top_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x2, self.__y1),
                    Point(self.__x2, self.__y2)
                )
            )

        if self.has_bottom_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x1, self.__y2),
                    Point(self.__x2, self.__y2)
                )
            )

    def draw_move(self, to_cell, undo=False):
        line = Line(
                Point(
                    (self.__x1 + self.__x2) / 2,
                    (self.__y1 + self.__y2) / 2
                ),
                Point(
                    (to_cell.__x1 + to_cell.__x2) / 2,
                    (to_cell.__y1 + to_cell.__y2) / 2
                )
            )
        
        if undo:
            self.__win.draw_line(line, 'gray')
        else:
            self.__win.draw_line(line, 'red')