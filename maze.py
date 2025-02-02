from window import Window
from cell import Cell
import time, random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)


    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                column.append(cell)
            self._cells.append(column)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
                

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        self._cells[i][j].draw(
            self.x1 + (i * self.cell_size_x),
            self.y1 + (j * self.cell_size_y),
            self.x1 + (i * self.cell_size_x) + self.cell_size_x,
            self.y1 + (j * self.cell_size_y) + self.cell_size_y
        )
        self._animate()
        

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Check north
            if (i - 1) >= 0 and (i - 1) < self.num_cols:
                if not self._cells[i - 1][j].visited:
                    to_visit.append((i-1, j))
            # Check south
            if (i + 1) >= 0 and (i + 1) < self.num_cols:
                if not self._cells[i + 1][j].visited:
                    to_visit.append((i + 1, j))
            # Check west
            if (j - 1) >= 0 and (j - 1) < self.num_rows:
                if not self._cells[i][j - 1].visited:
                    to_visit.append((i, j - 1))
            # Check east
            if (j + 1) >= 0 and (j + 1) < self.num_rows:
                if not self._cells[i][j + 1].visited:
                    to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._cells[i][j].draw()
                return
            else:
                direction = random.randrange(len(to_visit))
                next_i, next_j = to_visit[direction]
                if next_i < i:
                    self._cells[i][j].has_top_wall = False
                    self._cells[next_i][j].has_bottom_wall = False
                elif next_i > i:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[next_i][next_j].has_top_wall = False
                elif next_j < j:
                    self._cells[i][j].has_left_wall = False
                    self._cells[next_i][next_j].has_right_wall = False
                else:
                    self._cells[i][j].has_right_wall = False
                    self._cells[next_i][next_j].has_left_wall = False
                self._break_walls_r(next_i, next_j)

