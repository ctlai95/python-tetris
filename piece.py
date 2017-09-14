import config


class Piece:
    def __init__(self, coords, origin):
        self.coords = []
        for c in coords:
            self.coords.append(tuple(x for x in c))
        self.origin = origin

    def opengl_coords(self, x, y):
        x *= config.UNIT
        y *= config.UNIT
        return (x, y, x + config.UNIT, y,
                x + config.UNIT, y + config.UNIT,
                x, y + config.UNIT)

    def move_left(self):
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0] - 1,
                              self.coords[i][1])
        self.origin = (self.origin[0] - 1, self.origin[1])

    def move_right(self):
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0] + 1,
                              self.coords[i][1])
        self.origin = (self.origin[0] + 1, self.origin[1])

    def move_down(self, distance):
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0],
                              self.coords[i][1] - distance)
        self.origin = (self.origin[0], self.origin[1] - distance)

    def move_up(self):
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0],
                              self.coords[i][1] + 1)
        self.origin = (self.origin[0], self.origin[1] + 1)

    def clockwise_rotation(self):
        for i in range(len(self.coords)):
            normalized_point = tuple(x - y for x, y in zip(self.coords[i],
                                                           self.origin))
            btm_right = tuple(sum(t) for t in zip(normalized_point, (1, 0)))
            new_point = tuple(sum(t) for t in zip(self.origin,
                              (btm_right[1], -btm_right[0])))
            self.coords[i] = (int(new_point[0]), int(new_point[1]))

    def counter_clockwise_rotation(self):
        for i in range(len(self.coords)):
            normalized_point = tuple(x - y for x, y in zip(self.coords[i],
                                                           self.origin))
            top_left = tuple(sum(t) for t in zip(normalized_point, (0, 1)))
            new_point = tuple(sum(t) for t in zip(self.origin,
                              (-top_left[1], top_left[0])))
            self.coords[i] = (int(new_point[0]), int(new_point[1]))
