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
        self.key_handler = key.KeyStateHandler()
        self.push_handlers(self.key_handler)
        self.keyboard = Keyboard(
            self, self.board, self.movement, self.key_handler)
        self.on_key_press = self.keyboard.on_key_press
        self.on_key_release = self.keyboard.on_key_release

    def on_draw(self):
        self.clear()
        self.board.render_board()

    def update(self, dt):
        if self.key_handler[key.LEFT]:
            self.movement.move_left()
        if self.key_handler[key.RIGHT]:
            self.movement.move_right()
        if self.key_handler[key.DOWN]:
            self.movement.move_down()
