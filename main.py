from tkinter import *  # * = import everything
from cell import Cells
import setting
windows = Tk()  # build TK window 1
windows.configure(bg='black')
windows.geometry('600x500')  # for size of window('WIDTHHxHEIGHT')
windows.title('MINESWEEPER 😍💣')
windows.resizable(False, False)  # deactivate window size


frame_up = Frame(
    windows,
    bg='black', width='1400', height='120'
)
frame_up.place(x=0, y=0)

game_title = Label(
    frame_up,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 38)
)
game_title.place(x=70, y=10)
frame_left = Frame(
    windows,
    bg='black', width='185', height='1200'
)
frame_left.place(x=0, y=120)

frame_center = Frame(
    windows,
    bg='black', width='1400', height='1200'
)
frame_center.place(x=185, y=120)

for x in range(setting.GRIDE_SIZE):
    for y in range(setting.GRIDE_SIZE):
        c = Cells(x, y)
        c.create_btn_object(frame_center)
        c.cell_btn_object.grid(
            column=x, row=y
        )
Cells.random_mines()
Cells.create_cell_label(frame_left)
Cells.cell_count_label_object.place(x=0, y=0)


windows.mainloop()  # build TK window 2
