import pyglet
from pyglet.window import Window, key

import config
import map
import movement
import point
import square
import tetromino


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.map = map.Map(10, 22)
        self.movement = movement.Movement(self.map)

    def on_draw(self):
        self.clear()
        self.map.render_map()

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
        elif modifier & key.MOD_SHIFT:
            self.map.hold_piece()
        elif symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()


if __name__ == '__main__':
    window = Window(10 * config.UNIT, 22 * config.UNIT, "Python Tetris")
    pyglet.app.run()
