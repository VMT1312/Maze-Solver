from window import Window
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(100, 25, 4, 10, 15, 27, win)
    maze._create_cells()
    win.wait_for_close()


main()