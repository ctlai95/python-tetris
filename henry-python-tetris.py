from pyglet.gl import pyglet
import config


class Piece:
    def __init__(self, coords):
        self.shape = coords
        self.coords = []
        for x, y in coords:
            self.coords.append(tuple((x*40, y*40)))

    def opengl_coords():
        triangles = []
        for x, y in self.coords:
            triangles.append((x, y,
                              x+config.UNIT, y,
                              x+config.UNIT, y+config.UNIT,
                              x, y+config.UNIT))
        return triangles

    def render(self):
        for i in self.triangles:
            pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                         [0, 1, 2, 0, 2, 3],
                                         ('v2i', i))



class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.piece = Piece(config.O_PIECE)

    def on_draw(self):
        self.clear()
        self.piece.render()





if __name__ == '__main__':
    window = Window(10*config.UNIT, 22*config.UNIT,
            "Python Tetris", resizable=True)
    pyglet.app.run()
