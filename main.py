from tkinter import *
from cell import *
from game import *
import settings

root = Tk()
root.geometry(f"{settings.WINDOW_WIDTH}x{settings.WINDOW_HEIGHT}")
root.resizable(False, False)
root.title("Tic Tac Toe")

title_frame = Frame(
    root,
    bg="black",
    width=settings.WINDOW_WIDTH,
    height=settings.TITLE_FRAME_HEIGHT
)
title_frame.place(x=0, y=0)

game_frame = Frame(
    root,
    bg="red",
    width=settings.WINDOW_WIDTH,
    height=settings.GAME_FRAME_HEIGHT
)
game_frame.place(x=0, y=settings.TITLE_FRAME_HEIGHT)

game = Game(game_frame, DifficultyLevel.rndm)


root.mainloop()
