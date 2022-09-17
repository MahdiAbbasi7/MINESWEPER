import sys
from tkinter import Button, Label
import random
import setting
import ctypes
import sys
class Cells:
    all = []
    cell_count = setting.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.is_opened = False
        self.is_mine_candidate = False
        self.x = x
        self.y = y

        # Append the object to the cell.all list
        Cells.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=4,
            height=2,

        )
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-3>', self.right_click)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_label(loaction):
        lbl = Label(
            loaction,
            bg='black',
            fg='white',
            font=("",15)
        )
        Cells.cell_count_label_object = lbl


    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()

            self.show_cell()
        if Cells.cell_count == setting.MINES_COUNT:
            ctypes.windll.user32.MessageBoxW(0, "OMG YOU WIN")

        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x,y
        for cell in Cells.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cells.cell_count -= 1.
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # Replace the text of cell count label with the newer count
            if Cells.cell_count_label_object:
                Cells.cell_count_label_object.configure(
                    text=f'Cell left : {Cells.cell_count}'
                )

                self.cell_btn_object.configure(
                    bg='SystemButtonFace'
                )
        # Mark the cell as opened (Use is as the last line of this method)
        self.is_opened = True

    def show_mine(self):
        ctypes.windll.user32.MessageBoxW(0, "YOU FUCKED UP", "GAME'OVER!!!", 0)
        self.cell_btn_object.configure(bg='red')

        #sys.exit()

    def right_click(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate: True
        else:
            self.cell_btn_object.configure(
                bg='gray'
            )
            self.is_mine_candidate: False

    @staticmethod
    def random_mines():
        picked_mines = random.sample(
            Cells.all, setting.MINES_COUNT
        )
        for picked_mine in picked_mines:
            picked_mine.is_mine = True

    def __repr__(self):
        #  __repr__ is a special method used to represent a class's objects as a string.
        return f'cell({self.x},{self.y})'
