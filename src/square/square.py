"""Square object in the game."""
import logging

from src.renderer.renderer import Renderer

log = logging.getLogger(__name__)


class Square:
    """A square object represents four sided shape in the game."""

    def __init__(self, point, color):
        """
        Initialize a Square object.

        Args:
            point (Point): The point representing the square's bottom left corner.
            color (int list): The color to render the square in [R, G, B]
        """
        self.x = point.x
        self.y = point.y
        self.color = color

    def offset(self, x, y):
        """
        Move the square by the given horizontal and vertical values.

        Args:
            x (int): The number of horizontal units to move (pos = right, neg = left).
            y (int): The number of vertical units to move (pos = up, neg = down).
        """
        self.x += x
        self.y += y

    def render_square(self):
        """Renders the square to the screen"""
        r = Renderer(self.x, self.y, self.color)
        r.draw()
