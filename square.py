import pyglet

import config
import renderer


class Square:
    """The Square class renders a square with the given Coordinates"""

    def __init__(self, point, length):
        self.x = point._x()
        self.y = point._y()
        self.length = length

    def tuple(self):
        return (self.x, self.y)

    def offset(self, x, y):
        self.x += x
        self.y += y

    def render_square(self, color):
        """Renders the square to the screen"""
        r = renderer.Renderer(self.x, self.y, self.length, color)
        r.draw()
