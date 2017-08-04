import pyglet
import config
import piece


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.piece = Piece(O_PIECE)

    def on_draw(self):
        self.clear()
        self.piece.render()

    def on_text_motion(self, direction):
        tmp = []
        if direction == pyglet.window.key.MOTION_LEFT:
            for x, y in self.piece.shape:
                tmp.append(tuple((x-1, y)))
            self.piece = Piece(tmp)



@window.event
def on_text_motion(motion):
    if motion == pyglet.window.key.MOTION_LEFT or \
       motion == pyglet.window.key.MOTION_RIGHT or \
       motion == pyglet.window.key.MOTION_DOWN:
        current_piece.move(motion)


@window.event
def on_key_press(symbol, modifier):
    if symbol == pyglet.window.key.SPACE or \
       symbol == pyglet.window.key.MOTION_UP:
        current_piece.move(symbol)


current_piece = piece.piece(config.O_PIECE)


@window.event
def on_draw():
    window.clear()

    for i in range(current_piece.size):
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                     [0, 1, 2, 0, 2, 3],
                                     ('v2i', current_piece.opengl_coords()[i]))


if __name__ == '__main__':
    window = Window(10*UNIT, 22*UNIT, "Python Tetris", resizable=True)
    pyglet.app.run()
