import pyglet
import config
import operator


class Piece:
    def __init__(self, coords, rotation):
        self.coords = []
        for c in coords:
            self.coords.append(tuple(x * config.UNIT for x in c))
        self.point_of_rotation = tuple((rotation[0]*config.UNIT,
                                        rotation[1]*config.UNIT))

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
            self.point_of_rotation = tuple(
                map(operator.add, self.point_of_rotation, (0, -config.UNIT))
                )

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
            self.point_of_rotation = tuple(
                map(operator.add, self.point_of_rotation, (-config.UNIT, 0))
                )

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
            self.point_of_rotation = tuple(
                map(operator.add, self.point_of_rotation, (config.UNIT, 0))
                )

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
        tmp = self.coords
        self.coords = []
        for c in tmp:
            normalized_point = tuple(map(operator.sub, c, self.point_of_rotation))
            btm_right = tuple(map(operator.add, normalized_point, tuple((config.UNIT, 0))))
            normalized_new_point = tuple((btm_right[1], -btm_right[0]))
            new_point = tuple(map(operator.add, normalized_new_point, self.point_of_rotation))
            self.coords.append(tuple((int(new_point[0]), int(new_point[1]))))
        for c in self.coords:
            if c[0] < config.LEFT_BORDER * config.UNIT:
                self.move_right()
            if c[0] >= config.RIGHT_BORDER * config.UNIT:
                self.move_left()

    def rotate_ccw(self):
        tmp = self.coords
        self.coords = []
        for c in tmp:
            normalized_point = tuple(map(operator.sub, c, self.point_of_rotation))
            top_left = tuple(map(operator.add, normalized_point, tuple((0, config.UNIT))))
            normalized_new_point = tuple((-top_left[1], top_left[0]))
            new_point = tuple(map(operator.add, normalized_new_point, self.point_of_rotation))
            self.coords.append(tuple((int(new_point[0]), int(new_point[1]))))
        for c in self.coords:
            if c[0] < config.LEFT_BORDER * config.UNIT:
                self.move_right()
            if c[0] >= config.RIGHT_BORDER * config.UNIT:
                self.move_left()
