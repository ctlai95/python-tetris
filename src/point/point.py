import logging

log = logging.getLogger(__name__)


class Point:
    """A point is a coordinate on the board with an x and y position"""

    def __init__(self, xy):  # xy is a tuple
        self.x = xy[0]
        self.y = xy[1]

    def x_value(self):
        """Returns the x position"""
        return self.x

    def y_value(self):
        """Returns the y position"""
        return self.y

    def xy_tuple(self):
        """Returns the x and y positions as a tuple"""
        return (self.x, self.y)
