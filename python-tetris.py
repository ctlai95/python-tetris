import pyglet
import config
import piece


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.piece = piece.Piece(config.O_PIECE)

    def on_draw(self):
        self.clear()
        self.piece.render()

    def on_text_motion(self, motion):
        if motion == pyglet.window.key.MOTION_LEFT or \
           motion == pyglet.window.key.MOTION_RIGHT or \
           motion == pyglet.window.key.MOTION_DOWN:
                self.piece.move(motion)

    def on_key_press(self, symbol, modifier):
        if symbol == pyglet.window.key.SPACE or \
           symbol == pyglet.window.key.MOTION_UP:
                self.piece.move(symbol)


if __name__ == '__main__':
    window = Window(10*config.UNIT, 22*config.UNIT,
                    "Python Tetris", resizable=True)
    pyglet.app.run()
