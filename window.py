from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__canvas = Canvas(self.__root, bg='white', width=width, height=height)
        self.__canvas.pack(fill='both', expand=1)
        self.__running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close())


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()


    def close(self):
        self.__running = False


    def draw_line(self, line, fill_color='black'):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1=Point, point2=Point):
        self.p1 = point1
        self.p2 = point2


    def draw(self, canvas=Canvas, fill_color=str):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
