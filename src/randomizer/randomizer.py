from random import shuffle

from src import config


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
        return self.list.pop()

    def new_list(self):
        self.list = []
        for k in list(config.LAYOUTS.keys()):
            self.list.append(k)
        shuffle(self.list)
