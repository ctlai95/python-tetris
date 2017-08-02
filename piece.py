import pyglet
import config


class piece:
    def __init__(self, coords):
        self.coords = []
        for c in coords:
            self.coords.append(tuple(x * config.UNIT for x in c))
        self.size = len(coords)

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

    def move(self, key):
        if key == pyglet.window.key.MOTION_LEFT:
            moveable = True
            for c in self.coords:
                if c[0] <= config.LEFT_BORDER*config.UNIT:
                    moveable = False
            if moveable is True:
                tmp = self.coords
                self.coords = []
                for c in tmp:
                    self.coords.append(tuple((c[0]-config.UNIT, c[1])))
        if key == pyglet.window.key.MOTION_RIGHT:
            moveable = True
            for c in self.coords:
                if c[0]+config.UNIT >= config.RIGHT_BORDER*config.UNIT:
                    moveable = False
            if moveable is True:
                tmp = self.coords
                self.coords = []
                for c in tmp:
                    self.coords.append(tuple((c[0]+config.UNIT, c[1])))
        if key == pyglet.window.key.MOTION_UP:
            # TODO: t4 piece rotation
            print("💩")
        if key == pyglet.window.key.MOTION_DOWN:
            moveable = True
            for c in self.coords:
                if c[1] <= config.LOWER_BORDER*config.UNIT:
                    moveable = False
            if moveable is True:
                tmp = self.coords
                self.coords = []
                for c in tmp:
                    self.coords.append(tuple((c[0], c[1]-config.UNIT)))
        if key == pyglet.window.key.SPACE:
            height = config.UPPER_BORDER*config.UNIT
            for c in self.coords:
                if c[1] < height:
                    height = c[1]
            tmp = self.coords
            self.coords = []
            for c in tmp:
                self.coords.append(tuple((c[0], c[1]-height)))
