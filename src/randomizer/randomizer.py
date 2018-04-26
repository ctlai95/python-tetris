from random import shuffle

from src.point.point import Point
from src.tetromino.constants import COLORS, LAYOUTS, SPAWN
from src.tetromino.tetromino import Tetromino


class Randomizer:
    """
    Randomizer generates a list of next tetrominos, making sure
    every tetromino is used once before making another set
    """

    def __init__(self):
        self.new_list()

    def next(self):
        if len(self.list) == 0:
            self.new_list()
        next_tetromino_id = self.list.pop()
        return Tetromino(
            next_tetromino_id,
            Point(SPAWN[next_tetromino_id]),
            COLORS[next_tetromino_id],
        )

    def new_list(self):
        self.list = []
        for k in list(LAYOUTS.keys()):
            self.list.append(k)
        shuffle(self.list)
