from random import shuffle

from src.point.point import Point
from src.tetromino.constants import COLORS, LAYOUTS, SPAWN
from src.tetromino.tetromino import Tetromino


class Randomizer:
    """Randomizer handles the order of upcoming tetrominos in the game."""

    def __init__(self):
        """Initialize a Randomizer object with a list of keys."""
        self.new_list()

    def next(self):
        """
        Select a random tetromino to be next in play.

        Returns:
            Tetromino: The tetromino selected to be next.

        """
        if len(self.list) == 0:
            self.new_list()
        next_tetromino_id = self.list.pop()
        return Tetromino(
            next_tetromino_id,
            Point(SPAWN[next_tetromino_id][0], SPAWN[next_tetromino_id][1]),
            COLORS[next_tetromino_id],
        )

    def new_list(self):
        """Create a new random list of keys."""
        self.list = []
        for k in list(LAYOUTS.keys()):
            self.list.append(k)
        shuffle(self.list)
