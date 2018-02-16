from src.renderer.renderer import Renderer


class Square:
    """The Square class renders a square with the given Coordinates"""

    def __init__(self, point, color):
        self.color = color
        self.x = point._x()
        self.y = point._y()

    def tuple(self):
        return (self.x, self.y)

    def offset(self, x, y):
        self.x += x
        self.y += y

    def render_square(self):
        """Renders the square to the screen"""
        r = Renderer(self.x, self.y, self.color)
        r.draw()
