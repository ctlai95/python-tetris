import pyglet

import config
import renderer


class Square:
    """The Square class renders a square with the given Coordinates"""

    def __init__(self, coords):
        self.x = coords._x()
        self.y = coords._y()

    def tuple(self):
        return (self.x, self.y)

    def move_left(self):
        """Moves the square 1 unit to the left"""
        self.x -= 1

    def move_right(self):
        """Moves the square 1 unit to the right"""
        self.x += 1

    def move_down(self):
        """Moves the square 1 unit down"""
        self.y -= 1

    def move_up(self):
        """Moves the square 1 unit up"""
        self.y += 1

    def render_square(self, color):
        """Renders the square to the screen"""
        r = renderer.Renderer(self.x, self.y, color)
        r.draw()
