import operator

import config
import coordinate
import square


class Tetromino:
    """A tetromino is a piece which consists of exactly 4 squares"""

    def __init__(self, name, location):
        self.name = name
        self.loc = location  # of the bottomleft-most piece
        self.sqrs = self.populate_sqrs()
        self.color = config.COLORS[self.name]

    def populate_sqrs(self):
        """Returns the 4 squares as a list, according to name"""
        sqrs = []
        for i in range(4):
            sqrs.append(square.Square(coordinate.Coordinate(
                # element-wise tuple addition
                tuple(map(operator.add, self.loc._xy(),
                          config.LAYOUTS[self.name][i])))))
        return sqrs

    def move_left(self):
        """Moves the tetromino 1 unit to the left"""
        self.loc = coordinate.Coordinate(
            tuple(map(operator.add, self.loc._xy(), (-1, 0))))
        for s in self.sqrs:
            s.move_left()

    def move_right(self):
        """Moves the tetromino 1 unit to the right"""
        self.loc = coordinate.Coordinate(
            tuple(map(operator.add, self.loc._xy(), (1, 0))))
        for s in self.sqrs:
            s.move_right()

    def move_down(self):
        """Moves the tetromino 1 unit down"""
        self.loc = coordinate.Coordinate(
            tuple(map(operator.add, self.loc._xy(), (0, -1))))
        for s in self.sqrs:
            s.move_down()

    def rotate_cw(self):
        """Rotates the tetromino by 90 degrees, clockwise"""
        pass

    def render_tetromino(self):
        """Renders the tetromino to the screen"""
        for s in self.sqrs:
            s.render_square(self.color)
