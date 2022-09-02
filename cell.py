from tkinter import Button
import settings
import ctypes
import sys
from ai_opponent import *
from game import *


class Cell:

    def __init__(self, x, y, game):
        self.game = game
        self.x = x
        self.y = y
        self.text = ""
        self.button = None
        self.cell_played = False

    def create_connected_button(self, location):
        btn = Button(
            location,
            bg="white",
            font=("", 9),  # TODO: change font size without also changing size of button
            width=13,  # settings.CELL_WIDTH, #TODO: what??
            height=6,  # settings.CELL_HEIGHT
        )
        btn.grid(column=self.x, row=self.y)
        btn.bind("<Button-1>", self.left_click_action)
        self.button = btn

    def left_click_action(self, event):
        if not self.cell_played:
            self.mark_as_played(self.game.current_turn)
            self.game.check_game_end()
            self.game.end_players_turn()

    def mark_as_played(self, player):
        self.button.configure(text=player)
        self.text = player
        self.cell_played = True  # TODO: attribute can be removed, can look at text attribute for same info

    @staticmethod
    def get_cell_by_coordinates(x, y):
        for i in range(3 ** 2):
            cell = Cell.All_cells[i]
            if cell.x == x and cell.y == y:
                return cell

    def __repr__(self):
        return f"Cell at ({self.x},{self.y})"
