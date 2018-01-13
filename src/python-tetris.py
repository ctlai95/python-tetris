#!/usr/bin/env python3
import threading

import pyglet
from pyglet.window import Window, key

from src import config
from src.board.board import Board
from src.movement.movement import Movement


class Window(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.board = Board(int(self.width / config.UNIT),
                           int(self.height / config.UNIT))
        self.movement = Movement(self.board)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

    def on_draw(self):
        self.clear()
        self.board.render_board()

    def on_key_press(self, symbol, modifier):
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


if __name__ == '__main__':
    window = Window(400, 880, "Python Tetris")

    while True:
        pyglet.clock.tick()
        window.start_listeners()

        for win in pyglet.app.windows:
            win.switch_to()
            win.dispatch_events()
            win.dispatch_event('on_draw')
            win.flip()

        if window.keys[key.ESCAPE]:
            break
