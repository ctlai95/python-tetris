import pyglet
import config
import piece


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.piece = piece.Piece(config.T_PIECE,
                                 config.T_PIECE_ROTATION)

    def on_draw(self):
        self.clear()
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


if __name__ == '__main__':
    window = Window(10*config.UNIT, 22*config.UNIT,
                    "Python Tetris", resizable=True)
    pyglet.app.run()
