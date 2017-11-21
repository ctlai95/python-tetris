import operator

import config
import point
import square
import utils


class Tetromino:
    """A tetromino is a piece which consists of exactly 4 squares"""

    def __init__(self, name, location):
        self.name = name
        self.loc = location  # of the bottomleft-most piece
        self.sqrs = self.populate_sqrs()
        self.color = config.COLORS[self.name]
        self.state = 0

    def populate_sqrs(self):
        """Returns the 4 squares as a list, according to name"""
        sqrs = []
        for i in range(4):
            sqrs.append(square.Square(point.Point(
                utils.tuple_add(self.loc._xy(), config.LAYOUTS[self.name][i]))))
        return sqrs

    def move_left(self):
        """Moves the tetromino 1 unit to the left"""
        self.loc = point.Point(
            utils.tuple_add(self.loc._xy(), (-1, 0)))
        for s in self.sqrs:
            s.move_left()

    def move_right(self):
        """Moves the tetromino 1 unit to the right"""
        self.loc = point.Point(
            utils.tuple_add(self.loc._xy(), (1, 0)))
        for s in self.sqrs:
            s.move_right()

    def move_down(self):
        """Moves the tetromino 1 unit down"""
        self.loc = point.Point(
            utils.tuple_add(self.loc._xy(), (0, -1)))
        for s in self.sqrs:
            s.move_down()

    def move_up(self):
        """Moves the tetromino 1 unit up"""
        self.loc = point.Point(
            utils.tuple_add(self.loc._xy(), (0, 1)))
        for s in self.sqrs:
            s.move_up()

    def offset(self, values):
        # TODO: make it so that movements are done by adding tuples
        pass

    def rotate_cw(self):
        """Rotates the tetromino by 90 degrees, clockwise"""
        # the point of rotation, relative to the map origin
        abs_rotation_pt = utils.tuple_add(
            self.loc._xy(), config.ROTATION_POINTS[self.name])
        for i in range(len(self.sqrs)):
            # the square's position relative to the point of rotation
            current_square = utils.tuple_subtract(
                self.sqrs[i].tuple(), abs_rotation_pt)
            # the square's bottom right point, which will be the new
            # square origin after the rotation
            btm_right = utils.tuple_add(
                current_square, (1, 0))
            # x -> y and y -> -x for rotation about the origin
            new_point = utils.tuple_add(
                (btm_right[1], -btm_right[0]), abs_rotation_pt)
            # replace the old square with the new square
            self.sqrs[i] = square.Square(
                point.Point((int(new_point[0]), int(new_point[1]))))

    def rotate_ccw(self):
        """Rotates the tetromino by 90 degrees, counter-clockwise"""
        # the point of rotation, relative to the map origin
        abs_rotation_pt = utils.tuple_add(
            self.loc._xy(), config.ROTATION_POINTS[self.name])
        for i in range(len(self.sqrs)):
            # the square's position relative to the point of rotation
            current_square = utils.tuple_subtract(
                self.sqrs[i].tuple(), abs_rotation_pt)
            # the square's bottom right point, which will be the new
            # square origin after the rotation
            top_left = utils.tuple_add(
                current_square, (0, 1))
            # x -> y and y -> -x for rotation about the origin
            new_point = utils.tuple_add(
                (-top_left[1], top_left[0]), abs_rotation_pt)
            # replace the old square with the new square
            self.sqrs[i] = square.Square(
                point.Point((int(new_point[0]), int(new_point[1]))))

    def render_tetromino(self):
        """Renders the tetromino to the screen"""
        for s in self.sqrs:
            s.render_square(self.color)
