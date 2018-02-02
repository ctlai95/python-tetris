from pyglet.window import Window, key

from src import config
from src.board.board import Board
from src.keyboard.keyboard import Keyboard
from src.movement.movement import Movement


class Window(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.board = Board(int(self.width / config.UNIT),
                           int(self.height / config.UNIT))
        self.movement = Movement(self.board)
        self.keyboard = Keyboard(self, self.board, self.movement)
        self.on_key_press = self.keyboard.on_key_press

    def on_draw(self):
        self.clear()
        self.board.render_board()
