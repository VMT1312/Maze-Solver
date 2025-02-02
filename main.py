from window import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.draw(100, 125, 300, 400)
    cell2 = Cell(win)
    cell2.draw(500, 250, 10, 20)
    cell1.draw_move(cell2, 'True')
    win.wait_for_close()


main()