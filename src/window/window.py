"""The game's window."""
import logging

from pyglet.window import Window

from src import config
from src.board.board import Board
from src.keyboard.keyboard import Keyboard
from src.movement.movement import Movement

log = logging.getLogger(__name__)


class Window(Window):
    """Window inherits a pyglet window."""

    def __init__(self, *args, **kwargs):
        """Initialize a Window object."""
        log.info("Initializing window {}".format(args))
        super().__init__(*args, **kwargs)
        self.board = Board(int(self.width / config.UNIT),
                           int(self.height / config.UNIT))
        self.movement = Movement(self.board)
        self.keyboard = Keyboard(self, self.board, self.movement)
        self.on_text_motion = self.keyboard.on_text_motion
        self.on_key_press = self.keyboard.on_key_press

    def on_draw(self):
        """Override the pyglet on_draw function."""
        self.board.render_board()
