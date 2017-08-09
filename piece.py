import pyglet
import config


class Piece:
    def __init__(self, coords):
        self.coords = []
        for c in coords:
            self.coords.append(tuple(x * config.UNIT for x in c))

    def render(self):
        for i in range(len(self.coords)):
            pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                         [0, 1, 2, 0, 2, 3],
                                         ('v2i', self.opengl_coords()[i]))

    def opengl_coords(self):
        t = []
        for c in self.coords:
            t.append(
                (c[0], c[1],
                 c[0]+config.UNIT, c[1],
                 c[0]+config.UNIT, c[1]+config.UNIT,
                 c[0], c[1]+config.UNIT)
            )
        return t

    def move_down(self):
        moveable = True
        for c in self.coords:
            if c[1] <= config.LOWER_BORDER*config.UNIT:
                moveable = False
        if moveable is True:
            tmp = self.coords
            self.coords = []
            for c in tmp:
                self.coords.append(tuple((c[0], c[1]-config.UNIT)))

    def move_left(self):
        moveable = True
        for c in self.coords:
            if c[0] <= config.LEFT_BORDER*config.UNIT:
                moveable = False
        if moveable is True:
            tmp = self.coords
            self.coords = []
            for c in tmp:
                self.coords.append(tuple((c[0]-config.UNIT, c[1])))

    def move_right(self):
        moveable = True
        for c in self.coords:
            if c[0]+config.UNIT >= config.RIGHT_BORDER*config.UNIT:
                moveable = False
        if moveable is True:
            tmp = self.coords
            self.coords = []
            for c in tmp:
                self.coords.append(tuple((c[0]+config.UNIT, c[1])))

    def hard_drop(self):
        height = config.UPPER_BORDER*config.UNIT
        for c in self.coords:
            if c[1] < height:
                height = c[1]
        tmp = self.coords
        self.coords = []
        for c in tmp:
            self.coords.append(tuple((c[0], c[1]-height)))

    def rotate_cw(self):
        pass

    def rotate_ccw(self):
        pass
