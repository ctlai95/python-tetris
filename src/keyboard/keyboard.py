import pyglet
from pyglet.window import Window, key


class Keyboard:
    def __init__(self, window, board, movement):
        self.board = board
        self.movement = movement

    def on_key_press(self, symbol, modifier):
        if symbol == key.UP:
            self.movement.rotate_cw()
        elif symbol == key.LEFT:
            self.movement.move_left()
        elif symbol == key.RIGHT:
            self.movement.move_right()
        elif symbol == key.DOWN:
            self.movement.move_down()
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
