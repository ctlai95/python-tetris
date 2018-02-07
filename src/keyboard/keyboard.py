import pyglet
from pyglet.window import Window, key


class Keyboard:
    def __init__(self, window, board, movement, key_handler):
        self.board = board
        self.movement = movement
        self.key_handler = key_handler

    def on_key_press(self, symbol, modifier):
        if symbol == key.LEFT:
            self.key_handler[key.LEFT] = True
        elif symbol == key.RIGHT:
            self.key_handler[key.RIGHT] = True
        elif symbol == key.DOWN:
            self.key_handler[key.DOWN] = True
        elif symbol == key.UP:
            self.movement.rotate_cw()
        elif symbol == key.Z:
            self.movement.rotate_ccw()
        elif symbol == key.SPACE:
            self.movement.hard_drop()
        elif symbol == key.LSHIFT or \
                symbol == key.RSHIFT or \
                symbol == key.C:
            self.board.hold_piece()
        elif symbol == key.ESCAPE:
            pyglet.app.exit()

    def on_key_release(self, symbol, modifier):
        if symbol == key.LEFT:
            self.key_handler[key.LEFT] = False
        elif symbol == key.RIGHT:
            self.key_handler[key.RIGHT] = False
        elif symbol == key.DOWN:
            self.key_handler[key.DOWN] = False