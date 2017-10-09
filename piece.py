class Piece:
    def __init__(self, coords, rotation_point, color):
        self.coords = []
        for c in coords:
            self.coords.append(tuple(x for x in c))
        self.rotation_point = rotation_point
        self.color = color

    def move_left(self):
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0] - 1,
                              self.coords[i][1])
        self.rotation_point = (self.rotation_point[0] - 1,
                               self.rotation_point[1])

    def move_right(self):
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0] + 1,
                              self.coords[i][1])
        self.rotation_point = (self.rotation_point[0] + 1,
                               self.rotation_point[1])

    def move_down(self, distance):
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0],
                              self.coords[i][1] - distance)
        self.rotation_point = (self.rotation_point[0],
                               self.rotation_point[1] - distance)

    def move_up(self):
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0],
                              self.coords[i][1] + 1)
        self.rotation_point = (self.rotation_point[0],
                               self.rotation_point[1] + 1)

    def clockwise_rotation(self):
        for i in range(len(self.coords)):
            normalized_point = tuple(x - y for x,
                                     y in zip(self.coords[i],
                                              self.rotation_point))
            btm_right = tuple(sum(t) for t in zip(normalized_point, (1, 0)))
            new_point = tuple(sum(t) for t in zip(self.rotation_point,
                              (btm_right[1], -btm_right[0])))
            self.coords[i] = (int(new_point[0]), int(new_point[1]))

    def counter_clockwise_rotation(self):
        for i in range(len(self.coords)):
            normalized_point = tuple(x - y for x,
                                     y in zip(self.coords[i],
                                              self.rotation_point))
            top_left = tuple(sum(t) for t in zip(normalized_point, (0, 1)))
            new_point = tuple(sum(t) for t in zip(self.rotation_point,
                              (-top_left[1], top_left[0])))
            self.coords[i] = (int(new_point[0]), int(new_point[1]))
