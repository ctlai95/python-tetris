from src.renderer import renderer


class Square:
    """The Square class renders a square with the given Coordinates"""

    def __init__(self, point):
        self.x = point._x()
        self.y = point._y()

    def tuple(self):
        return (self.x, self.y)

    def offset(self, x, y):
        self.x += x
        self.y += y

    def render_square(self, color):
        """Renders the square to the screen"""
        r = renderer.Renderer(self.x, self.y, color)
        r.draw()
