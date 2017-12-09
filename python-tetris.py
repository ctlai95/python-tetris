import pyglet

import board
import config
import movement
import point
import square
import tetromino


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.board = board.Board(int(self.width / config.UNIT),
                                 int(self.height / config.UNIT))
        self.movement = movement.Movement(self.board)

    def on_draw(self):
        self.clear()
        self.board.render_board()

    def on_key_press(self, symbol, modifier):
        if symbol == pyglet.window.key.LEFT:
            self.movement.move_left()
        elif symbol == pyglet.window.key.RIGHT:
            self.movement.move_right()
        elif symbol == pyglet.window.key.DOWN:
            self.movement.move_down()
        elif symbol == pyglet.window.key.UP:
            self.movement.rotate_cw()
        elif symbol == pyglet.window.key.Z:
            self.movement.rotate_ccw()
        elif symbol == pyglet.window.key.SPACE:
            self.movement.hard_drop()
        elif symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()


if __name__ == '__main__':
    window = Window(400, 880, "Python Tetris")
    pyglet.app.run()
