import pyglet
import config
import operator
from pyglet.gl import *


class Piece:
    def __init__(self, coords, rotation, color):
        self.coords = []
        for c in coords:
            self.coords.append(tuple(x * config.UNIT for x in c))
        self.point_of_rotation = tuple((rotation[0]*config.UNIT,
                                        rotation[1]*config.UNIT))
        self.color = color

    def render(self):
        vertex_list = pyglet.graphics.vertex_list(4, 'v2i', 'c3B')

        for i in range(len(self.coords)):
            vertex_list.vertices = self.opengl_coords()[i]
            vertex_list.colors = [self.color[0], self.color[1], self.color[2],
                                  self.color[0], self.color[1], self.color[2],
                                  self.color[0], self.color[1], self.color[2],
                                  self.color[0], self.color[1], self.color[2]]
            vertex_list.draw(pyglet.gl.GL_TRIANGLE_FAN)
            shade = [int(c * 0.8) for c in self.color]
            vertex_list.colors = [shade[0], shade[1], shade[2],
                                  shade[0], shade[1], shade[2],
                                  shade[0], shade[1], shade[2],
                                  shade[0], shade[1], shade[2]]
            pyglet.gl.glLineWidth(2)
            vertex_list.draw(GL_LINE_LOOP)

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

    def move_up(self):
        moveable = True
        for c in self.coords:
            if c[1] >= config.UPPER_BORDER*config.UNIT:
                moveable = False
        if moveable is True:
            tmp = self.coords
            self.coords = []
            for c in tmp:
                self.coords.append(tuple((c[0], c[1]+config.UNIT)))
            self.point_of_rotation = tuple(
                map(operator.add, self.point_of_rotation, (0, config.UNIT))
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
        self.point_of_rotation = tuple(map(operator.add,
                                           self.point_of_rotation,
                                           (0, -height)))

    def rotate_cw(self):
        tmp = self.coords
        self.coords = []
        for c in tmp:
            normalized_point = tuple(map(operator.sub, c,
                                         self.point_of_rotation))
            btm_right = tuple(map(operator.add,
                                  normalized_point,
                                  (config.UNIT, 0)))
            normalized_new_point = tuple((btm_right[1], -btm_right[0]))
            new_point = tuple(map(operator.add,
                                  normalized_new_point,
                                  self.point_of_rotation))
            self.coords.append(tuple((int(new_point[0]), int(new_point[1]))))
        for c in self.coords:
            if c[0] < config.LEFT_BORDER * config.UNIT:
                self.move_right()
            if c[0] >= config.RIGHT_BORDER * config.UNIT:
                self.move_left()
            if c[1] < config.LOWER_BORDER * config.UNIT:
                self.move_up()

    def rotate_ccw(self):
        tmp = self.coords
        self.coords = []
        for c in tmp:
            normalized_point = tuple(map(operator.sub, c,
                                         self.point_of_rotation))
            top_left = tuple(map(operator.add,
                                 normalized_point,
                                 (0, config.UNIT)))
            normalized_new_point = tuple((-top_left[1], top_left[0]))
            new_point = tuple(map(operator.add,
                                  normalized_new_point,
                                  self.point_of_rotation))
            self.coords.append(tuple((int(new_point[0]), int(new_point[1]))))
        for c in self.coords:
            if c[0] < config.LEFT_BORDER * config.UNIT:
                self.move_right()
            if c[0] >= config.RIGHT_BORDER * config.UNIT:
                self.move_left()
            if c[1] < config.LOWER_BORDER * config.UNIT:
                self.move_up()
