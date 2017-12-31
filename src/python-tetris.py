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

    def on_draw(self):
        self.clear()
        self.board.render_board()

    def on_key_press(self, symbol, modifier):
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
            self.board.hold_piece()
        elif symbol == key.ESCAPE:
            pyglet.app.exit()


if __name__ == '__main__':
    window = Window(400, 880, "Python Tetris")
    pyglet.app.run()
