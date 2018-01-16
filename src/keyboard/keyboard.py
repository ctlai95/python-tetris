import threading

import pyglet
from pyglet.window import key


class Keyboard:
    def __init__(self, window, board, movement):
        self.keys = key.KeyStateHandler()
        window.push_handlers(self.keys)
        self.board = board
        self.movement = movement

    def handle_actions(self, symbol, modifier):
        if symbol == key.UP:
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
            exit()

    def listen_left(self):
        if self.keys[key.LEFT]:
            self.movement.move_left()

    def listen_right(self):
        if self.keys[key.RIGHT]:
            self.movement.move_right()

    def listen_down(self):
        if self.keys[key.DOWN]:
            self.movement.move_down()

    def start_listeners(self):
        threading.Thread(target=self.listen_left).start()
        threading.Thread(target=self.listen_right).start()
        threading.Thread(target=self.listen_down).start()
