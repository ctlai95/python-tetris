import pyglet
import config
import piece
from pyglet.gl import *


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.piece = piece.Piece(config.I_PIECE,
                                 config.I_PIECE_ROTATION,
                                 config.I_PIECE_COLOR)

    def on_draw(self):
        self.clear()
        self.render_grid()
        self.piece.render()

    def on_text_motion(self, motion):
        if motion == pyglet.window.key.MOTION_LEFT:
            self.piece.move_left()
        if motion == pyglet.window.key.MOTION_RIGHT:
            self.piece.move_right()
        if motion == pyglet.window.key.MOTION_DOWN:
            self.piece.move_down()

    def on_key_press(self, symbol, modifier):
        if symbol == pyglet.window.key.SPACE:
            self.piece.hard_drop()
        if symbol == pyglet.window.key.MOTION_UP:
            self.piece.rotate_cw()
        if symbol == pyglet.window.key.Z:
            self.piece.rotate_ccw()
    def render_grid(self):
        vertex_list = pyglet.graphics.vertex_list(4, 'v2i', 'c3B')
        for x in range(10):
            for y in range(22):
                left = x*config.UNIT
                right = (x+1)*config.UNIT
                bottom = y*config.UNIT
                top = (y+1)*config.UNIT
                vertex_list.vertices = [left, bottom,
                                        right, bottom,
                                        right, top,
                                        left, top]
                if (x%2 is 0 and y%2 is 0) or ((x+1)%2 is 0 and (y+1)%2 is 0):
                    vertex_list.colors = [40, 40, 40,
                                         40, 40, 40,
                                         40, 40, 40,
                                         40, 40, 40]
                else:
                    vertex_list.colors = [50, 50, 50,
                                         50, 50, 50,
                                         50, 50, 50,
                                         50, 50, 50]
                vertex_list.draw(GL_TRIANGLE_FAN)

    def piece_gravity(self, dt):
        self.piece.move_down()

if __name__ == '__main__':
    window = Window(10*config.UNIT, 22*config.UNIT,
                    "Python Tetris", resizable=True)
    pyglet.clock.schedule_interval(window.piece_gravity,
                                   config.GRAVITY_INTERVAL)
    pyglet.app.run()
