import enum
from cell import *
import random


class DifficultyLevel():
    rndm = 0,
    easy = 1,
    hard = 2,


class AiOpponent:
    def __init__(self, difficulty_level=DifficultyLevel.rndm):
        self.difficulty_level = difficulty_level

    def choose_cell(self, available_cells):
        cell = None
        if self.difficulty_level == DifficultyLevel.rndm:
            cell = random.sample(available_cells, 1)[0]
        elif self.difficulty_level == DifficultyLevel.easy:
            pass  # TODO
        else:
            pass  # TODO
        return cell
