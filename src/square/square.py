import logging

from src.renderer.renderer import Renderer

log = logging.getLogger(__name__)


class Square:
    """The Square class renders a square with the given Coordinates"""

    def __init__(self, point):
        self.x = point.x_value()
        self.y = point.y_value()

    def tuple(self):
        return (self.x, self.y)

    def offset(self, x, y):
        self.x += x
        self.y += y

    def render_square(self, color):
        """Renders the square to the screen"""
        r = Renderer(self.x, self.y, color)
        r.draw()
