import logging

log = logging.getLogger(__name__)


class Point:
    """A point is a coordinate on the board with an x and y position"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def subtract(self, point):
        return Point(self.x - point.x, self.y - point.y)
