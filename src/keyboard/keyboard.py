"""Keyboard press handler"""
import logging

import pyglet
from pyglet.window import key

from src.config import AUTO_SHIFT_DELAY

log = logging.getLogger(__name__)


class Keyboard:
    """Keyboard handles all the key presses in the game."""

    def __init__(self, window, board, movement):
        """
        Initialize a Keyboard object.

        Args:
            window (Window): The game's window object.
            board (Board): The game's board object.
            movement (Movement): The game's movement handler.
        """
        log.info("Initializing keyboard")
        self.window = window
        self.board = board
        self.movement = movement

    def on_key_press(self, symbol, modifier):
        """
        Override pyglet's on_key_press function with tetromino movements.

        Args:
            symbol (int): A virtual key code, constants defined in `pyglet.window.key`.
            modifier (int): A modifer key, constants defined in `pyglet.window.key`.
        """
        if symbol == key.LEFT:
            self.movement.move_left(1)
            pyglet.clock.schedule_once(self.schedule_delayed_interval,
                                       AUTO_SHIFT_DELAY, self.movement.move_left, 1 / 60.0)
        elif symbol == key.RIGHT:
            self.movement.move_right(1)
            pyglet.clock.schedule_once(self.schedule_delayed_interval,
                                       AUTO_SHIFT_DELAY, self.movement.move_right, 1 / 60.0)
        elif symbol == key.DOWN:
            self.movement.move_down(1)
            pyglet.clock.schedule_once(self.schedule_delayed_interval,
                                       AUTO_SHIFT_DELAY, self.movement.move_down, 1 / 60.0)
        elif symbol == key.UP:
            self.movement.rotate_cw()
        elif symbol == key.Z:
            self.movement.rotate_ccw()
        elif symbol == key.SPACE:
            self.movement.hard_drop()
        elif symbol == key.LSHIFT or \
                symbol == key.RSHIFT or \
                symbol == key.C:
            self.board.hold_current_tetromino()
        elif symbol == key.ESCAPE:
            pyglet.app.exit()

    def on_key_release(self, symbol, modifier):
        if symbol == key.LEFT:
            pyglet.clock.unschedule(self.movement.move_left)
            pyglet.clock.unschedule(self.schedule_delayed_interval)
        elif symbol == key.RIGHT:
            pyglet.clock.unschedule(self.movement.move_right)
            pyglet.clock.unschedule(self.schedule_delayed_interval)
        elif symbol == key.DOWN:
            pyglet.clock.unschedule(self.movement.move_down)
            pyglet.clock.unschedule(self.schedule_delayed_interval)

    def schedule_delayed_interval(self, delay, movement, fps):
        pyglet.clock.schedule_interval(movement, fps)
