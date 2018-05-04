"""Keyboard press handler"""
import logging

import pyglet
from pyglet.window import key

log = logging.getLogger(__name__)


class Keyboard:
    """Keyboard handles all the key presses in the game."""

    def __init__(self, movement):
        """
        Initialize a Keyboard object.

        Args:
            movement (Movement): The game's movement handler.
        """
        log.info("Initializing keyboard")
        self.movement = movement

    def on_key_press(self, symbol, modifier):
        """
        Override pyglet's on_key_press function with tetromino movements.

        Args:
            symbol (int): A virtual key code, constants defined in `pyglet.window.key`.
            modifier (int): A modifer key, constants defined in `pyglet.window.key`.
        """
        if symbol == key.LEFT:
            self.movement.move_left()
        elif symbol == key.RIGHT:
            self.movement.move_right()
        elif symbol == key.DOWN:
            self.movement.move_down()
        elif symbol == key.UP:
            self.movement.rotate_cw()
        elif symbol == key.Z:
            self.movement.rotate_ccw()
        elif symbol == key.SPACE:
            self.movement.hard_drop()
        elif symbol == key.LSHIFT or \
                symbol == key.RSHIFT or \
                symbol == key.C:
            self.movement.board.hold_current_tetromino()
        elif symbol == key.ESCAPE:
            pyglet.app.exit()
